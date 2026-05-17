from datetime import datetime
import os

BALANCE_FILE = "balance.txt"
HISTORY_FILE = "history.txt"


# ---------- LOAD BALANCE ----------
def load_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as f:
            try:
                return float(f.read())
            except:
                return 0.0
    return 0.0


# ---------- SAVE BALANCE ----------
def save_balance(balance):
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))


# ---------- ADD HISTORY ----------
def add_history(text):
    with open(HISTORY_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {text}\n")


# ---------- MAIN PROGRAM ----------
balance = load_balance()

while True:
    print("\n====== WALLET APP ======")
    print("1. Add Money")
    print("2. Spend Money")
    print("3. Check Balance")
    print("4. View History")
    print("5. Exit")

    choice = input("Choose: ")

    # ADD MONEY
    if choice == "1":
        amount = float(input("Amount to add: ₦"))

        balance += amount
        save_balance(balance)
        add_history(f"Added ₦{amount}")

        print("Money added successfully!")

    # SPEND MONEY
    elif choice == "2":
        amount = float(input("Amount to spend: ₦"))

        if amount > balance:
            print("❌ Not enough balance!")
        else:
            balance -= amount
            save_balance(balance)
            add_history(f"Spent ₦{amount}")
            print("Money spent successfully!")

    # CHECK BALANCE
    elif choice == "3":
        print(f"\n💰 Current Balance: ₦{balance}")

    # VIEW HISTORY
    elif choice == "4":
        print("\n===== HISTORY =====")
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as f:
                print(f.read())
        else:
            print("No history yet.")

    # EXIT
    elif choice == "5":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice, try again.")
