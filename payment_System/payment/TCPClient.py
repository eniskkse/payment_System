import importlib
from . import TCPServer



class navigator():


    def __init__(self):
        self.transfer_another_bank=1
        self.mydbs=TCPServer.Customer.server(self)
        self.decider()
        

    def decider(self):
        print("Please enter your Account number and password.")
        self.Account=input()
        self.password=input()
        self.sql="Select Name,Balance,Bank from customers where (Account=%s and password=%s)"
        self.want=self.Account, self.password
        self.cursor.execute(self.sql,self.want)
        self.result=self.cursor.fetchone()
        self.question()


    def question(self):
        if bool(self.result)==False:
            print("Wrong account number or password!")
            
        else:
            print(self.result)
            print(f"Welcome {self.result[0]},Your balance {self.result[1]}.How can we help?")
            print("""
            Send money to my own account==> press(1),
            withdraw money from my own account==> press(2)
            or transfer money to someone else's account==> press(3)""")
            self.process=input()
            if self.process=="1":
                self.send_my_own()

            if self.process=="2":
                self.withdraw()

            if self.process=="3":
                self.send_someone()


    def send_my_own(self):
        print("What is the amount you want to deposit?")
        self.entry=int(input())
        self.newresult=int(self.result[1])+self.entry
        self.newresult=str(self.newresult)
        print(f"The money transfer is successful. Your new balance:{self.newresult}")
        self.complete()
        print("Would you like to take another action?(press anything)")
        returnques=input()
        if bool(returnques)==True:
            return navigator()


    def withdraw(self):
        print("what is the amount you want to withdraw?")
        self.entry=int(input())
        if self.entry > int(self.result[1]):
            print("You exceeded your balance!")

        elif self.entry <= int(self.result[1]):
            self.newresult=int(self.result[1])-self.entry
            self.newresult=str(self.newresult)
            print(f"The money transfer is successful. Your new balance:{self.newresult}")
            self.complete()
            print("Would you like to take another action?(press anything)")
            returnques=input()
            if bool(returnques)==True:
                return navigator()


    def send_someone(self):
        self.sql="Select Bank From customers where Account=%s"
        print("Enter the account number you want to send.\n")
        self.entry=(input(),)
        self.cursor.execute(self.sql,self.entry)
        self.result1=self.cursor.fetchone()

        if self.result1==self.result[2]:
            self.entry1=int(input("How much is the amount to be sent?\n"))
            if self.entry1 <= int(self.result[1]):
                self.newresult=int(self.result[1])-self.entry1
                print(f"The money transfer is successful. Your new balance:{self.newresult}")
                self.send_someone_complete()
                self.complete()
                print("Would you like to take another action?(press anything)")
                returnques=input()
                if bool(returnques)==True:
                    return navigator()


            elif self.entry1 > int(self.result[1]):
                print("You do not have sufficient funds in your account. Operation failed!")
                print("Would you like to take another action?(press anything)")
                returnques=input()
                if bool(returnques)==True:
                    return navigator()

        elif self.result1 != self.result[2]:
            self.entry1=int(input("How much is the amount to be sent?\n"))
            if self.entry1 <= (int(self.result[1])-self.transfer_another_bank):
                self.newresult=int(self.result[1])-self.entry1-self.transfer_another_bank
                print(f"The money transfer is successful. Your new balance:{self.newresult}")
                self.send_someone_complete()
                self.complete()
                print("Would you like to take another action?(press anything)")
                returnques=input()
                if bool(returnques)==True:
                    return navigator()


            elif self.entry1 > int(self.result[1]-self.transfer_another_bank):
                print("You do not have sufficient funds in your account. Operation failed!")
                print("Would you like to take another action?(press anything)")
                returnques=input()
                if bool(returnques)==True:
                    return navigator()


    def complete(self):
        self.sql1="Update customers Set Balance=%s where Account=%s"
        self.Values=(self.newresult,self.Account)
        self.cursor.execute(self.sql1,self.Values)
        try:
            self.mydb.commit()
        except mysql.connector.Error as err:
            print("Error",err)
        finally:
            self.mydb.close()


    def send_someone_complete(self):
        self.sql1="Select Balance From customers where Account=%s"
        self.cursor.execute(self.sql1,self.entry)
        self.result=self.cursor.fetchone()
        self.result1=int(self.result[0])
        self.sql="Update customers Set Balance=%s where Account=%s"
        self.values1=self.result1 + self.entry1
        self.values2=self.values1,self.entry[0]
        self.cursor.execute(self.sql,self.values2)
        self.mydb.commit()
        


navigator()