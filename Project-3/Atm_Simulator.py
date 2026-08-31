
class BankAccount:
    def __init__(self,balance,pin):
        self.__balance=balance
        self.__pin=pin
        self.__Transactions=[]

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,amount):
        if amount>=0:
            self.__balance=amount
        else:
            print("The amount cannot be negative")
    def verify_pin(self,entered_pin):
        return entered_pin==self.__pin

    def check_balance(self):
        print("Your Balance is :",self.balance)

    def deposit_amount(self,amount):
        if amount>0:
            self.balance+=amount
            print("Deposited Successfully")
            print("Your Updated Balance is:",self.balance)
            self.__Transactions.append({"Type":"Deposite",
                        "Amount": amount,
                        "Balance": self.balance})
        else:
            print("Amount Value is Invalid")
    def withdraw(self):
        try:
            amount=int(input("Enter the amount to withdraw: "))
        except ValueError:
            print("Enter the amount in Numbers")
            return
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print(f"Amount withdrawn successfully")
            print(f"Your Updated Balance is: {self.balance}")
            self.__Transactions.append({"Type":"Withdraw","Amount": amount,"Balance": self.balance})
        else:
            print("Invalid Balance")
    def mini_statements(self):
        if len(self.__Transactions)==0:
            print("No Transactions Are available")
        else:
            for trans in self.__Transactions:
                print(f"{trans['Type']}     "
                f"{trans['Amount']}     "
                f"Balance:{trans['Balance']}")
    def change_pin(self):
        try:
            current_pin = int(input("Enter your current PIN: "))
        except ValueError:
            print("Enter numbers only")
            return

        if current_pin != self.__pin:
            print("Incorrect current PIN")
            return

        try:
            new_pin = int(input("Enter your new PIN: "))
            confirm_pin = int(input("Confirm your new PIN: "))
        except ValueError:
            print("PIN must contain numbers only")
            return

        if new_pin != confirm_pin:
            print("New PIN and Confirm PIN do not match")
            return

        if new_pin == self.__pin:
            print("New PIN cannot be the same as your current PIN")
            return
        self.__pin = new_pin
        print("PIN changed successfully")
account=BankAccount(10000,12345)

attempt=3
while attempt>0:
    try:
        enter_pin=int(input("Enter the Pin: "))
    except ValueError:
        print("Enter Numbers only")
        continue
    if account.verify_pin(enter_pin):
        print("Pin verified Successfully")
        break
    else:
        attempt-=1
        print("Incorrect Pin")
        print("The Remaining attempts:",attempt)
if attempt==0:
        print("Your card has been blocked")
else:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit the Amount")
        print("3. Withdraw the Amount")
        print("4. Mini Statements")
        print("5. Change Pin")
        print("6. Exit")
        try:
            choice=int(input("Enter your Choice Between 1 to 6: "))
        except ValueError:
            print("Eneter Valid Choice Number")
            continue

        if choice==1:
            account.check_balance()
        elif choice==2:
            try:
                amount=int(input("Enter the amount you want to deposit: "))
                account.deposit_amount(amount)
            except ValueError:
                print("Enter the amount in numbers")
                continue
            
        elif choice==3:
            account.withdraw()
        elif choice==4:
            account.mini_statements()
        elif choice==5:
            account.change_pin()
            
        elif choice==6:
            print("Thanks for using the ATM simulator")
            break
        else:
            print("Invalid Choice")