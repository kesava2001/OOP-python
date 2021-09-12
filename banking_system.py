# parent class user
# holds details about an user
# has a function to show user details
# child class bank
# stores details about the account balance
# stores details about the amount
# allows for deposits, withdraw, view_balance


class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_details(self):
        print("User Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
    
    def deposits(self, amount):
        self.balance += amount
        print("Account balance has been updated: $", self.balance)
    
    def withdraw(self, value):
        self.value = value
        if self.value > self.balance:
            print("Insufficient funds | Balance available: $", self.balance)
        else:
            self.balance -= self.value
            print("Account balance has been updated: $", self.balance)
            print(f"$ {self.value} is withdrawn")

    def view_balance(self):
        print(f"Current balance is $ {self.balance}")