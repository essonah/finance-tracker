from expense import Expense
from datetime import datetime
import calendar


def main():

    print("Running Expense Tracker")
    expense_file_name="expenses.csv"
    # get user to input expense
    expense =getUserExpense()
    budget= 2000
    #write their expense into a file
    expenseIntoFile(expense, expense_file_name)

    # read file and summarize expenses.
    summarize_Expenses(expense_file_name, budget)

def getUserExpense():
    print(" 📌 Getting user expense: ")
    expense_name= input("Enter expense name: ")
    expense_amount= float(input("Enter expense amount: "))
  
  
 
    expense_categories= [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "⚜️ Miscellanous",
        "🎭 Entertainment/Fun"

    ]
    while True:
        print("Select a category :")

        for i, category_name in enumerate(expense_categories):
            print(f" {i +1}. { category_name}")
       

            value_range= f"[1- {len(expense_categories)}]"
        try:
            selected_index=int(input(f"Select a category number {value_range} :"))-1
        except Exception:
            pass

        if selected_index in range(len(expense_categories)):
            selected_category= expense_categories[selected_index]
            new_expense= Expense(name=expense_name, amount= expense_amount,category =selected_category)
            return new_expense
        else:
            print("Invalid category, Try again")

def expenseIntoFile(expense: Expense, expense_file_name):
    print(f" 📌 Saving User Expense: {expense} to {expense_file_name}")
    with open(expense_file_name, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")
   
def summarize_Expenses(expense_file_name, budget):
    print("📌 Summarize expenses")
    expenses:list[Expense]=[]
    with open(expense_file_name,"r") as f:
        lines= f.readlines()
        for line in lines:
            expense_name, expense_amount,expense_category = line.strip().split(",")
            line_expense= Expense(
                name = expense_name,
                amount = float(expense_amount), 
                category= expense_category,
                )
           
            expenses.append(line_expense)
  
    amount_by_category={}

    for expense in expenses:
        key= expense.category
        if key in amount_by_category:
            amount_by_category[key]+= expense.amount
        else:
            amount_by_category[key]= expense.amount
    print("Expenses by category")

    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")
    
    total_spent= sum([expense.amount for expense in expenses])
    print(f"You spent ${total_spent:.2f} this month!")

    remaining_budget= budget - total_spent
    print(f"You remaining buget is: ${remaining_budget:.2f}")
         
   
    # Get the current date
    today = datetime.today()
    
        # Get the last day of the current month
    _, last_day = calendar.monthrange(today.year, today.month)
    
        # Calculate the remaining days
    remaining_days = last_day - today.day
    
    
    daily_budget= remaining_budget/remaining_days
    print(f"Budget per day: $ {daily_budget}")
if __name__ == "__main__":
    main()