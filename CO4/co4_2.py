class Bank:
    def __init__(self,bal=0):
        self.bal=bal
        name=input("enter name:")
        print("Account for",name,"is created")    
    def deposit(self):
        amount=int(input("enter amount to deposit"))
        self.bal=self.bal+amount
        print("balance:",self.bal)
    def withdraw(self):
        amount=int(input("enter amount to withdraw"))
        if(amount>self.bal):
            print("Insufficient Balance!")
            print("Your Remaining Balance=",self.bal)
        else:
            self.bal=self.bal-amount
    def enquiry(self):
        print("Your Balance =",self.bal)
b1= Bank()
b1.deposit()
b1.withdraw()
b1.enquiry()


        
