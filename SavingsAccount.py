from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    interest = 0.02

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)

    def deposit(self):
        amount = float(input("Enter amount to deposit:"))
        self.current_balance += amount
        total_interest = round(self.current_balance * self.interest)
        self.current_balance += total_interest
        print("Total interest:", total_interest)
        print("New balance:", self.current_balance)
        return

    def withdraw(self):
        amount = float(input("Enter amount to withdraw:"))
        if amount > self.current_balance:
            print("Insufficient balance")
            return
        self.current_balance -= amount
        total_interest = round(amount * self.interest)
        self.current_balance -= total_interest

        print("New balance:", self.current_balance)
        return



