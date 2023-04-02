# class Account():
#     def __init__(self):
#         pass
        
#         print("what is your account number?")
#         # get the account number
#         # get the account holder name
#         # get their current balance
#         # get their rate of interest
#         # if they would like to withdraw
#         # if they would like to deposit


#///////#

class Account:
    def __init__(self, accNum, balance):
        self.accNum = accNum
        self.balance = balance

    def getAccNum(self):
        return self.accNum

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False


class SavingsAccount(Account):
    def __init__(self, accNum, balance, minBalance):
        super().__init__(accNum, balance)
        self.minBalance = minBalance

    def getMinBalance(self):
        return self.minBalance

    def withdraw(self, amount):
        if amount > 0 and self.balance - amount >= self.minBalance:
            self.balance -= amount
            return True
        else:
            return False


class ChequingAccount(Account):
    def __init__(self, accNum, balance, overdraftLimit):
        super().__init__(accNum, balance)
        self.overdraftLimit = overdraftLimit

    def getOverdraftLimit(self):
        return self.overdraftLimit

    def withdraw(self, amount):
        if amount > 0 and self.balance + self.overdraftLimit >= amount:
            self.balance -= amount
            return True
        else:
            return False


class Bank:
    def __init__(self):
        self.accounts = []
        self.accounts.append(SavingsAccount(10001, 5000, 1000))
        self.accounts.append(SavingsAccount(10002, 10000, 2000))
        self.accounts.append(ChequingAccount(20001, 5000, 1000))
        self.accounts.append(ChequingAccount(20002, 10000, 2000))
        self.accounts.append(Account(30001, 500))

    def searchAccount(self, accNum):
        for account in self.accounts:
            if account.getAccNum() == accNum:
                return account
        return None


class Program:
    def __init__(self):
        self.bank = Bank()

    def showMainMenu(self):
        while True:
            print("1. Open Account (Bonus)")
            print("2. Select Account")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.openAccount()
            elif choice == "2":
                self.selectAccount()
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def showAccountMenu(self, account):
        while True:
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit Account")
            choice = input("Enter your choice: ")
            if choice == "1":
                print("Balance:", account.getBalance())
            elif choice == "2":
                amount = input("Enter amount to deposit: ")
                try:
                    amount = float(amount)
                    if account.deposit(amount):
                        print("Deposit successful. New balance:", account.getBalance())
                    else:
                        print("Invalid amount. Please try again.")
                except ValueError:
                    print("Invalid amount. Please try again.")
            elif choice == "3":
                amount = input("Enter amount to withdraw: ")
                try:
                    amount = float(input("Enter the amount to deposit: "))
                    account.deposit(amount)
                    print("Deposit successful. New balance:", account.getBalance())
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")

program = Program()
program.showMainMenu()

                

