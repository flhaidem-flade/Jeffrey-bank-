from flask import Flask, render_template_string, request, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)

BALANCE_FILE = "balance.txt"
HISTORY_FILE = "history.txt"


def load_balance():
    if os.path.exists(BALANCE_FILE):
        try:
            with open(BALANCE_FILE, "r") as f:
                return float(f.read())
        except:
            return 0.0
    return 0.0


def save_balance(balance):
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))


def add_history(text):
    with open(HISTORY_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {text}\n")


HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Jeffrey Bank</title>
</head>
<body style="font-family:Arial;background:#111;color:white;text-align:center;">

<h2>🏦 Jeffrey Bank Wallet</h2>

<h1 style="color:lightgreen;">₦{{balance}}</h1>

<form method="POST" action="/add">
<input name="amount" placeholder="Add money">
<button>Add</button>
</form>

<form method="POST" action="/spend">
<input name="amount" placeholder="Spend money">
<button>Spend</button>
</form>

<pre>{{history}}</pre>

</body>
</html>
"""


@app.route("/")
def home():
    balance = load_balance()

    history = ""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = f.read()

    return render_template_string(HTML, balance=balance, history=history)


@app.route("/add", methods=["POST"])
def add():
    amount = float(request.form["amount"])
    balance = load_balance()
    balance += amount
    save_balance(balance)
    add_history(f"Added ₦{amount}")
    return redirect(url_for("home"))


@app.route("/spend", methods=["POST"])
def spend():
    amount = float(request.form["amount"])
    balance = load_balance()
    if amount <= balance:
        balance -= amount
        save_balance(balance)
        add_history(f"Spent ₦{amount}")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
