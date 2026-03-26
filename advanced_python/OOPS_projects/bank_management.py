class bank_management:
    def __init__(self, name, balance):
        print("hello ", name, ", your account's balance is ", balance, ".", "\n", sep="")
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("amount deposited succesfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("amount withdrawed succesfully")
        else:
            print("Invalid amount")


acc = bank_management("Saurav", 15000)
print("*"*30, "1. Check Balance", "2. Deposit", "3. Withdraw", "4. Exit", "*"*30, sep="\n")
print()

while True:
    choice = int(input("Enter choice : "))

    if choice == 1:
        print("balance is", acc.check_balance())
    elif choice == 2:
        amount = int(input("Enter amount : "))
        acc.deposit(amount)
    elif choice == 3:
        amount = int(input("Enter amount : "))
        acc.withdraw(amount)
    elif choice == 4:
        print("Thank you for using our service.")
        break
    else:
        print("Invalid choice number, please try again")

    print("*"*30)
