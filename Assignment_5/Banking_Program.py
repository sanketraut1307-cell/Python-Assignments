

class Bank:

    def __init__(self, bal):
        self.balance = bal

    def deposit(self):
        amount = float(input("Enter Deposit Amount: "))
        self.balance = self.balance + amount
        print("Deposited")

    def withdraw(self):
        amount = float(input("Enter Withdraw Amount: "))

        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdraw Successful")
        else:
            print("No Balance")

    def check(self):
        print("Balance:", self.balance)

    def receipt(self, name, acc):

        print("\n------ BANK RECEIPT ------")
        print("Name       :", name)
        print("Account No :", acc)
        print("Final Bal  :", self.balance)
        print("Status     : Completed")
        print("--------------------------")


# Main Program

name = input("Enter Name: ")
acc = input("Enter Account No: ")

b = float(input("Enter Current Balance: "))

obj = Bank(b)


while True:
    print("\n1 Deposit")
    print("2 Withdraw")
    print("3 Check Balance")
    print("4 Exit")
    ch = int(input("Enter Choice: "))

    if ch == 1:
        obj.deposit()
        obj.receipt(name, acc)

    elif ch == 2:
        obj.withdraw()
        obj.receipt(name, acc)

    elif ch == 3:
        obj.check()
        obj.receipt(name, acc)
    
    elif ch == 4:
        break

    else:
        print("Wrong Choice!")
        print(" - Final Receipt - ")
        obj.receipt(name, acc)
    c=input("Do you want to continue (yes/no)? - ")
    if c == "yes":
        continue
    else:
        break
print()
print(" - Final Receipt - ")
obj.receipt(name, acc)


