




import json
from datetime import datetime
class expensetracker:
    def __init__(self, balance = 0):
        self.balance = balance

    def expense(self, e):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('tracker.json', 'r+') as file:
            raw_data = json.load(file)
            data = raw_data[-1]
            amount = data.get("amount")
            new_expense = amount["Expense"] + e
            new_balance = amount["Balance"] - e
            updated_data = { "id": timestamp,
                            "amount":{
                            "Income": amount["Income"],
                            "Expense": new_expense,
                            "Balance": new_balance
                            } }
            raw_data.append(updated_data)
            file.seek(0)
            json.dump(raw_data, file, indent=4)
            print({f"-{e}, remaining balance: {new_balance}"})


    def income(self, i):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('tracker.json', 'r+') as file:
            raw_data = json.load(file)
            data = raw_data[-1]
            amount = data.get("amount")
            new_income = amount["Income"] + i
            new_balance = amount["Balance"] + i
            updated_data = { "id": timestamp,
                            "amount":{
                            "Income": new_income,
                            "Expense": amount["Expense"],
                            "Balance": new_balance
                            }}
            raw_data.append(updated_data)
            file.seek(0)
            json.dump(raw_data, file, indent=4)
            print({f"+{i}, remaining balance: {new_balance}"})
    
    def view_history(self):
        with open('tracker.json', 'r+') as file:
            raw_data = json.load(file)
        for i in range(len(raw_data)):
            data = raw_data[i]
            amount = data.get("amount")
            print(f"Date:{data["id"]}  | Expenses : -{amount["Expense"]}  | Income : +{amount["Income"]}  |  Balance : {amount["Balance"]}")
        

l = expensetracker(0)
while True:
    n = input("Select the below options \n Click 1 to add expense \n Click 2 to add income \n click 3 to view history")
    if n == "1":
        i=int(input("Enter the expense amount"))
        l.expense(i)

    elif n =="2":
        i=int(input("Enter the income amount"))
        l.income(i)
    elif n =="3":
        l.view_history()

    else:
        break




