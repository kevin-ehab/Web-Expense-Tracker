import simple_encrypter
import datetime

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
classified = pd.read_csv('Classified.csv')
expenses = pd.read_csv('Expenses.csv')

from jinja2 import FileSystemLoader, Environment
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/options')
def options_page():
    return render_template('options.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/categories')
def categories_page():
    return render_template('categories.html')

@app.route('/change')
def change_page():
    return render_template('change.html')

@app.route('/login2', methods=['POST'])
def login():
    global classified, account
    data = request.get_json()
    account = data.get('account')
    entered_password = data.get('password')
    if account in classified['account'].values:
            user_data = classified[classified['account'] == account].iloc[0]
            decrypted_password = simple_encrypter.decrypt({'code': user_data['password_code'],
                                                            'key': user_data['password_key']})
            if decrypted_password != entered_password:
                return jsonify({'message': "Wrong password", "redirect": 0})
            else:
                return jsonify({'message': "Logged in successfully!", 'redirect': 1})
    else:
        return jsonify({'message': "Account not found. Sign up.", "redirect": 0})


@app.route('/signup2', methods = ['POST'])
def signup():
    global classified, account
    data = request.get_json()
    account = data.get('account')
    if account in classified['account'].values:
        return jsonify({'message': "account already exists. Login.", 'redirect': 2})
    password = data.get('password')
    if len(password) < 8:
        return jsonify({'message' : "Password is too short. It should be at least 8 charachters long",
                        'redirect':0})
    try:
        income = int(data.get('income'))
        saving = int(data.get('saving'))
    except:
        return jsonify({'message': "Monthly income and saving goal must be numbers", 'redirect':0})
    income = simple_encrypter.encrypt(str(income))
    password = simple_encrypter.encrypt(password)
    saved = {
        "account": account,
        "password_code": password['code'],
        "password_key": password['key'],
        "income_code": income['code'],
        "income_key": income['key'],
        "saving": saving
    }
    classified = pd.concat([classified, pd.DataFrame([saved])], ignore_index=True)
    classified.to_csv('Classified.csv', index=False)
    return jsonify({'message': 'Account added', 'redirect': 1})

@app.route('/categories2', methods=['POST'])
def categories():
    global expenses
    date = datetime.date.today().strftime(r'%Y-%m-%d')
    if date in expenses['date'].values:
        return jsonify({'message': "Already entered data for today", 'redirect':1})
    data = request.get_json()
    food = data.get('food')
    transportation = data.get('transportation')
    shopping = data.get('shopping')
    bills = data.get('bills')
    entertainment = data.get('entertainment')
    healthcare = data.get('healthcare')
    try:
        food = int(data.get('food')) if food.strip() else 0
        transportation = int(data.get('transportation')) if transportation.strip() else 0
        shopping = int(data.get('shopping')) if shopping.strip() else 0
        bills = int(data.get('bills')) if bills.strip() else 0
        entertainment = int(data.get('entertainment')) if entertainment.strip() else 0
        healthcare = int(data.get('healthcare')) if healthcare.strip() else 0 
    except:
        return jsonify({'message': "Entries must be numbers", 'redirect':0})
    total = food + transportation + shopping + bills + entertainment + healthcare
    data = {
        'account': account,
        'date': date,
        'food': food,
        'transportation': transportation,
        'shopping': shopping,
        'bills': bills,
        'entertainment': entertainment,
        'healthcare': healthcare,
        'total': total
    }
    expenses = pd.concat([expenses, pd.DataFrame([data])], ignore_index=True)
    expenses.to_csv('Expenses.csv', index=False)
    return jsonify({"message": 'Entries saved successfully!', 'redirect':1})

@app.route('/change2', methods=['POST'])
def change():
    global classified
    data = request.get_json()
    income = data.get('income')
    if income.strip() == '':
        income = int(simple_encrypter.decrypt({'code': classified[classified['account'] == account]['income_code'].iloc[0],
                                            'key': classified[classified['account'] == account]['income_key'].iloc[0]}))
    saving = data.get('saving')
    if saving.strip() == '':
        saving = int(classified[classified['account'] == account]['saving'].iloc[0])
    try:
        income = int(income)
        saving = int(saving)
        if saving >= income:
            return jsonify({'message':'Saving goal exceeds income', 'redirect':0})
        if saving < 0 or income < 0:
            return jsonify({'message':"negative numbers aren't allowed", 'redirect':0})
        income = str(income)
    except:
        return jsonify({'message':'income and saving must be numbers', 'redirect':0})
    encrypted_budget = simple_encrypter.encrypt(income)
    classified.loc[classified['account'] == account, 'income_code'] = encrypted_budget['code']
    classified.loc[classified['account'] == account, 'income_key'] = encrypted_budget['key']
    classified.loc[classified['account'] == account, 'saving'] = saving
    classified.to_csv('Classified.csv', index=False)
    return jsonify({'message':'Saved successfully', 'redirect':1})

@app.route('/dashboard2')
def view_data():
    global expenses, account
    income = int(simple_encrypter.decrypt({'code': classified[classified['account'] == account]['income_code'].iloc[0],
                                           'key': classified[classified['account'] == account]['income_key'].iloc[0]}))
    
    saving = classified.loc[classified['account'] == account, 'saving'].iloc[0]
    expenses = pd.read_csv('Expenses.csv')
    extracted_df = expenses[expenses['account'] == account]

    days = len(pd.unique(extracted_df['date']))
    if days > 30:
        days = 30
    if days == 1:
        return jsonify({'message':'You need to enter more days to view the dashboard'})
    extracted_df = extracted_df.tail(days)

    total_sum = sum(extracted_df['total'])
    food = sum(extracted_df['food'])
    transportation = sum(extracted_df['transportation'])
    shopping = sum(extracted_df['shopping'])
    bills = sum(extracted_df['bills'])
    entertainment = sum(extracted_df['entertainment'])
    healthcare= sum(extracted_df['healthcare'])

    sum_by_categories = {"food":food, 
                         "transportation":transportation,
                         "shopping": shopping,
                         "bills":bills,
                         "entertainment":entertainment,
                         "healthcare": healthcare}
    max_category = max(sum_by_categories, key=sum_by_categories.get)
    max_category = max_category.title()

    biggest_day = extracted_df[extracted_df['total'] == extracted_df['total'].max()]['date'].iloc[0]
    smallest_day = extracted_df[extracted_df['total'] == extracted_df['total'].min()]['date'].iloc[0]

    daily_spending = round(total_sum / days)

    if daily_spending > (income - saving)/30:
        decrease = round(((daily_spending - (income - saving)/30) / daily_spending) * 100)
        message = '⚠️ Be carful. You need to spend less to reach your saving goal, '
        message += f'which is <strong>{saving}</strong>. '
        message += f'So decrease your spending by {decrease}% !'
    else:
        message = f'✅ You are on the right track to achieving your saving goal! Which is {saving}'
    #pie chart:
    plt.figure(figsize=(6, 6))
    plt.pie(sum_by_categories.values(), labels=sum_by_categories.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Expenses by Category')
    plt.savefig(os.path.join('static', 'charts', 'pie.png'))
    plt.close()
    
    #trend chart:
    plt.figure(figsize=(8, 6))
    plt.plot(extracted_df['date'], extracted_df['total'])
    plt.axhline(daily_spending, color="#00039e", linestyle='--',
                 linewidth=2, label=f'Average spending: ({daily_spending})')
    plt.axhline(round(income/30), color="#b30000", linestyle='--',
                linewidth=2, label=f'Suggested spending: ({round(income/30)})')
    plt.xticks(rotation=90)
    plt.title('Expense Trend Over Time')
    plt.savefig(os.path.join('static', 'charts','trend.png'))
    plt.close()

    #plot chart (total / budget percentage per day)
    plt.figure(figsize=(8,6))
    percent = extracted_df['total'] / income* 100
    plt.bar(extracted_df['date'], percent, color='#e67e22')
    plt.gca().set_yticks(plt.gca().get_yticks())  # Re-assert y-ticks
    plt.gca().set_yticklabels([f'{int(y)}%' for y in plt.gca().get_yticks()])
    plt.xticks(rotation=90)
    plt.title('Date VS Spending Percentage')
    plt.savefig(os.path.join('static', 'charts', 'plot.png'))
    plt.close()
    #table:
    html_table = extracted_df.to_html()
    #All the data:
    data = {
        'account': account,
        'biggest_day': biggest_day,
        'budget': income,
        'saving': saving,
        'smallest_day': smallest_day,
        'total_sum': total_sum,
        'days': days,
        'food': food,
        'transportation': transportation,
        'shopping': shopping,
        'bills': bills,
        'entertainment': entertainment,
        'healthcare': healthcare,
        'max_category': max_category,
        'daily_spending': daily_spending,
        'html_table': html_table,
        'message': message,
        'trend': os.path.join('static', 'charts', 'trend.png'),
        'plot': os.path.join('static', 'charts','plot.png'),
        'pie': os.path.join('static', 'charts', 'pie.png')
    }
    #rendering:
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')
    html = template.render(data)

    with open(os.path.join('templates', 'dashboard.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    return jsonify({'message':"Dashboard generated successfully"})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
