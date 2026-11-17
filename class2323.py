class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,balance):
        if balance >= 0 :
            self.__balance=balance
        else :
            print("Invalid")

account1234=BankAccount(500)
print(account1234.get_balance())
account1234.set_balance(12566)
print(account1234.get_balance())
