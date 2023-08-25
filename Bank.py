from random import randrange
class Account():
    
    def __init__(self, account_number, account_holder, initial_balance):
        #digits = randrange(0,1000)
        if initial_balance < 500.0:
            print("Ou dwe met 500 goud pou pi piti sou kont ou an ")
        else:
            self.account_number = account_number
            self.account_holder = account_holder
            self.initial_balance = initial_balance
        #self.account_number = "000" + str(digits)
    def deposit(self, amount):
        self.amount = amount
        self.initial_balance += amount   
    def withdraw(self, amount):
        if amount > self.initial_balance:
            print("Kòb ou mete a twòp, ou pa gen tout sa !!!")
        else:
            self.amount = amount
            self.initial_balance -= amount
    def get_balance(self):
        print("Ou gen ",self.initial_balance,"goud sou kont ou")
    
    def __str__(self):
       return f"\nAccount Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: {self.initial_balance} Goud"
    
# Kreye yon kont
account1 = Account("00340203", "Lub Lorry", 10000.00)

# Depo
account1.deposit(500.00)

# Retrè
account1.withdraw(200.00)

# Verifye balans
balance = account1.get_balance()

# Afiche enfòmasyon sou kont lan
print(account1)

# try :
#     data = open("name.txt", "r")
#     data.close()
# except FileNotFoundError:
#     data = open("name.txt", "w")
#     data.write(str(account1))
#     data.close()

# Mwen tap eseye met chak idantifyan yo nan yon fichye apre pou m fè konparezon ak sak te la deja yo yon fason pou idantifyan yo te ka inik menm pa reyisi fè l pou moman 