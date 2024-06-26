class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            print("Invalid amount. Please enter a positive number.")
            return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Insufficient funds or invalid amount. Please check your balance.")
            return False
    
    def check_balance(self):
        return self.balance


class ATM:
    def __init__(self, account):
        self.account = account
    
    def display_menu(self):
        print("\n=== ATM Menu ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1/2/3/4): ")
            
            if choice == '1':
                print(f"Your current balance is: ${self.account.check_balance()}")
            elif choice == '2':
                amount = float(input("Enter amount to deposit: $"))
                if self.account.deposit(amount):
                    print(f"Deposit of ${amount} successful.")
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: $"))
                if self.account.withdraw(amount):
                    print(f"Withdrawal of ${amount} successful.")
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option (1/2/3/4).")



if __name__ == "__main__":

    account = BankAccount(initial_balance=1000)
    

    atm = ATM(account)
    

    atm.run()
