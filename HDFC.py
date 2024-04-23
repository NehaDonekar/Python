class HDFC:
    ROI=9.5 #class variable 

    def __init__(self,Name,Amount): #constructor
        self.AccountHolder=Name
        self.balance=Amount #instance variable
        print("Welcome",self.AccountHolder)
        print("Account gets sucessfully created with initaial balace:",self.balance)

    def DisplayBalance(self): #instance method
        print("Hello",self.AccountHolder)
        print("Your account balance is:",self.balance)

    @classmethod #light exa
    def DisplayBankInfo(cls): #class mothod
        print("Welcome to HDFC bank portal")
        print("Our bank is pvt ltd bank")
        print("We provide the rate of intrest on saving account is:",cls.ROI)

    @staticmethod
    def DisplayKYCInfo():
        print("According to the rulesof RBI u should provide below documents for KYC")
        print("Your Adhar card")
        print("Your Pan card")
        print("Your Passport size photo")

    def Withdraw(self,Amount): #instance method
        if self.balance<Amount:
            print("Sorry you do not have enough money in your account")
        else:
            self.balance=self.balance-Amount
            print("Amount withdraw sucessfully") 

    def Deposit(self,Amount): #instance method
        self.balance=self.balance+Amount
        print("Amount deposited sucessfully")          

def main():
    print("ROI of HDFC bank is:",HDFC.ROI)

    HDFC.DisplayBankInfo()

    HDFC.DisplayKYCInfo()

    print("creating new account..")
    obj1 = HDFC("neha",5000)   #__init__(adress,5000) 

    print("creating new account..")
    obj2 = HDFC("harshal",3000)  #__init__(address,3000)

    print("performing operation on obj1")
    obj1.Deposit(2000)
    obj1.DisplayBalance()

    obj1.Withdraw(1000)
    obj1.DisplayBalance()

    print("performing operation on obj2")
    obj2.Deposit(4000)
    obj2.DisplayBalance()

    obj2.Withdraw(500)
    obj2.DisplayBalance()

if __name__=="__main__":
    main()    