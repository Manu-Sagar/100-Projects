class Expense:
    def __init__(self, category, amount):
        self.__category = category
        self.__amount = amount

    def get_category(self):
        return self.__category

    def get_amount(self):
        return self.__amount

    def display_expense(self):
        print("Category:",self.__category, "| Amount: Rs.",self.__amount)

class ExpenseTracker:
    def __init__(self):
        self.__expenses = []

    def add_expense(self):
        while True:
            category=input("Enter expense category: ").strip()

            if category=="":
                print("Category cannot be empty.")
            else:
                break

        while True:
            try:
                amount=float(input("Enter expense amount:"))
                if amount<=0:
                    print("Amount must be greater than 0.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")

        expense=Expense(category,amount)

        self.__expenses.append(expense)

        print("Expense added successfully")

    def view_expenses(self):
        if len(self.__expenses)==0:
            print("No expenses found.")
            return

        print("\n====EXPENSES===")

        for expense in self.__expenses:
            expense.display_expense()

    def calculate_total(self):
        if len(self.__expenses)==0:
            print("No expenses found.")
            return

        total = 0
        for expense in self.__expenses:
            total+=expense.get_amount()

        print("Total Expense: Rs.", total)

    def find_highest_expense(self):
        if len(self.__expenses)==0:
            print("No expenses found.")
            return

        highest=self.__expenses[0]

        for expense in self.__expenses:
            if expense.get_amount()>highest.get_amount():
                highest=expense

        print(f"Highest Expanse: Category:{highest.get_category()}, Amount: Rs.{highest.get_amount()}")

def display_menu():
    print("\n====STUDENT EXPENSE TRACKER===")
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.Calculate Total")
    print("4.Find Highest Expense")
    print("5.Exit")

def main():
    tracker = ExpenseTracker()

    while True:

        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice=="1":
            tracker.add_expense()

        elif choice=="2":
            tracker.view_expenses()

        elif choice=="3":
            tracker.calculate_total()

        elif choice=="4":
            tracker.find_highest_expense()

        elif choice=="5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()