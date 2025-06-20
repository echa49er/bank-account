class BankAccount:
    name = "My Very Cool & Real Bank You Should Do Business With"
    __accountNumber = None
    __routingNumber = None

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.accountNumber = account_number
        self.routing_number = routing_number

    def deposit(self):
        amount = float(input("Enter amount to deposit:"))
        self.current_balance += amount
        print("New balance:", self.current_balance)
        return

    def withdraw(self):
        amount = float(input("Enter amount to withdraw:"))
        if amount > self.current_balance:
            print("Insufficient balance")
            return
        self.current_balance -= amount
        print("New balance:", self.current_balance)
        return

    def printCustomerInfo(self):
        print(BankAccount.name)
        print("Customer name:", self.customer_name)
        print("Current balance:", self.current_balance)
        print("Minimum balance:", self.minimum_balance)
        print("Routing number:", self.routing_number)
        print("Account number:", self.accountNumber)



customer1 = BankAccount("Ronaldo", 7123.25, 5000, 123456789, 221133)
customer1.deposit()
customer1.withdraw()
customer1.printCustomerInfo()

customer2 = BankAccount("Beth", 425.33, 25, 987654321, 987897)
customer2.deposit()
customer2.withdraw()
customer2.printCustomerInfo()