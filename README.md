# 💰 Flask Expense Tracker

An interactive and secure expense tracking web app built with **Flask**, **Pandas**, **Matplotlib**, **Jinja2**, and **JavaScript**. It lets users log their daily expenses, visualize spending trends, manage savings goals, and view insightful dashboards.
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

- **Backend:** Flask, Pandas, Jinja2
- **Frontend:** HTML, CSS, JavaScript
- **Visualization:** Matplotlib
- **Encryption:** Self-made `simple_encrypter` module

---

## 📸Dashboard preview:

| Chart                                  | Description                |
| -------------------------------------- | -------------------------- |
| ![Pie Chart](static/charts/pie.png)    | Expense by category        |
| ![Trend Line](static/charts/trend.png) | Daily spending trend       |
| ![Bar Chart](static/charts/plot.png)   | Daily spending % of budget |


## 🕹 Demo link
Try the app using this link: <a href='https://bba18d20-6366-4132-9e3d-35a8b34cc7be-00-2z4simwq327lt.janeway.replit.dev:5000/'>Expense Tracker</a>

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/flask-expense-tracker.git
cd flask-expense-tracker
```
### 2. Install Requirements
```bash
pip install flask pandas matplotlib jinja2
```
### 3. Create Required Files
<strong>Ensure you have:</strong><br>

- `Expenses.csv` and `Classified.csv` in the root directory

- A templates/ folder with:

  - home.html
  - login.html
  - signup.html
  - options.html
  - categories.html
  - dashboard.html
  - change.html
  - template.html

- A static/ folder with:
  - `login.css`
  - charts/ folder for saving generated charts
### 4. Run the App
```bash
python main.py
```
Then visit:
📍 <a href='http://localhost:5000'>http://localhost:5000</a>

---

## 📂 Project Structure

Web-Expense-Tracker/<br>
├── main.py<br>
├── simple_encrypter.py<br>
├── Classified.csv<br>
├── Expenses.csv<br>
├── templates/<br>
│ ├── home.html<br>
│ ├── login.html<br>
│ ├── signup.html<br>
│ ├── options.html<br>
│ ├── categories.html<br>
│ ├── change.html<br>
│ └── template.html<br>
├── static/<br>
│ ├── login.css<br>
│ └── charts/<br>
│ ├── pie.png<br>
│ ├── trend.png<br>
│ └── plot.png

---

## 🔐 About `simple_encrypter`
Handles encryption and decryption of passwords and income using symmetric encryption.
If you are intrested, I have a repo only for it here: 
<a href='https://github.com/kevin-ehab/simple-encrypter'>simple-encrypter</a>

---

## 🙌 Credits
Developed by <strong>Kevin Ehab</strong><br>
Feel free to fork, contribute, or suggest features!
