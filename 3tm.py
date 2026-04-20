from datetime import datetime
import json, os

accounts = {
    "1234567890": {
        "name": "Twink",
        "bank": "State Bank of India",
        "dob": "67",
        "pin": "1234",
        "balance": 50000,
        "transactions": []
    }
}

def get_account(acc_no, pin):
    acc = accounts.get(acc_no)
    if acc and acc["pin"] == pin:
        return acc
    return None

def add_transaction(acc, type_, amount):
    acc["transactions"].append({
        "type": type_,
        "amount": amount,
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

def mini_statement(acc):
    last3 = acc["transactions"][-3:]
    if not last3:
        print("No transactions found.")
    for t in last3:
        print(f"  {t['datetime']} | {t['type']} | ₹{t['amount']}")

def main():
    print("=== ATM Management System ===")
    acc_no = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    acc = get_account(acc_no, pin)
    if not acc:
        print("Invalid credentials!"); return

    print(f"\nWelcome, {acc['name']}")
    print(f"Bank: {acc['bank']} | DOB: {acc['dob']}\n")

    while True:
        print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Mini Statement\n5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            print(f"Balance: ₹{acc['balance']}")

        elif choice == "2":
            amt = int(input("Deposit amount: "))
            acc["balance"] += amt
            add_transaction(acc, "Deposit", amt)
            print(f"₹{amt} deposited. New Balance: ₹{acc['balance']}")

        elif choice == "3":
            amt = int(input("Withdraw amount: "))
            if amt > acc["balance"]:
                print("Insufficient funds!")
            else:
                acc["balance"] -= amt
                add_transaction(acc, "Withdrawal", amt)
                print(f"₹{amt} withdrawn. New Balance: ₹{acc['balance']}")

        elif choice == "4":
            print("--- Mini Statement (Last 3 Transactions) ---")
            mini_statement(acc)

        elif choice == "5":
            print("see ya"); break

        else:
            print("think again")

main()