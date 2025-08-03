# 💰 Flask Expense Tracker

An interactive and secure expense tracking web app built with **Flask**, **Pandas**, **Matplotlib**, and **JavaScript**. It lets users log their daily expenses, visualize spending trends, manage savings goals, and view insightful dashboards.
<p align="center">
  <img src="static/logo.png" alt="Description" width="300"/>
</p>

---

## ✨ Features:

- 🔒 Encrypted account credentials and budgets
- 🧾 Daily expense logging by category
- 📈 Dashboard with:
  - Pie chart (category distribution)
  - Line graph (spending trends)
  - Bar chart (budget % per day)
- 💬 Insight messages to guide your saving behavior
- 📊 Automatically generated expense tables
- ⚙️ Change income or saving goal from settings
- 🗃 Data stored in `Expenses.csv` and `Classified.csv`

---

## 🛠 Tech Stack:

- **Backend:** Python(Flask, Pandas)
- **Frontend:** HTML, CSS, JavaScript
- **Visualization:** Matplotlib
- **Encryption:** Self-made `simple_encrypter` module

---

## 📸Dashboard preview:

| Chart                                  | Description                |
| -------------------------------------- | -------------------------- |
| ![Pie Chart](https://github.com/user-attachments/assets/80ec048c-c322-4b57-bd61-923001247d63)    | Expense by category        |
| ![Trend Line](https://github.com/user-attachments/assets/b80696e8-4616-465f-a8fc-d89d31310240) | Daily spending trend       |
| ![Bar Chart](https://github.com/user-attachments/assets/db75b6e7-a097-40e8-beef-45f4628a3c86)   | Daily spending % of budget |

---

## 🕹 Demo link
Try the app using this link: [Expense Tracker](https://web-expense-tracker-production.up.railway.app/)

---

## 📕Guide
1. open the demo link
2. click `sign up`
3. add your email password income and saving goal and click sign up
4. add your expenses by clicking on `add data` (do this daily)
5. click `generate dashboard` and see the insights and info about your spending patterns
6. if you want to change the entered income or saving goal, click on the last button and change them.

---

## 🚀 Running it locally

if you want to use the app but you are worried about the security of the site, here is how to run it locally!

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/flask-expense-tracker.git
cd flask-expense-tracker
```
### 2. Install Requirements
```bash
pip install flask pandas matplotlib
```
### 3. Create Required Files
<strong>Ensure you have this folder structure:</strong><br>
<pre>
📁Web-Expense-Tracker
│   Classified.csv
│   Expenses.csv
│   main.py
│   Procfile
│   README.md
│   requirements.txt
│   simple_encrypter.py
│
├───static
│   │   categories.js
│   │   change.js
│   │   home.js
│   │   login.css
│   │   login.js
│   │   logo.png
│   │   options.js
│   │   signup.js
│   │
│   └───charts
│           pie.png
│           plot.png
│           trend.png
│
└───templates
        categories.html
        change.html
        error.html
        home.html
        login.html
        options.html
        signup.html
        template.html
</pre>
### 4. Run the App
```bash
python main.py
```
Then visit:
📍 <a href='http://localhost:5000'>http://localhost:5000</a>

---

## 🔐 About `simple_encrypter`
Handles encryption and decryption of passwords and income using symmetric encryption.
If you are intrested, I have a repo only for it here: 
<a href='https://github.com/kevin-ehab/simple-encrypter'>simple-encrypter</a>

---

## 🙌 Credits
Developed by <strong>Kevin Ehab</strong>
