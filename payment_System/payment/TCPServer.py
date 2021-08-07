import mysql.connector


class Customer():

    def __init__(self,mylist):
        self.mylist=mylist
        self.server()
        self.insert()

    def server(self):
        self.mydb=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="9889",
            database="customer"
        )
        self.cursor=self.mydb.cursor()
        self.cursor.execute("CREATE DATABASE CUSTOMER")
        self.cursor.execute("CREATE TABLE customers (Bank VARCHAR(256), Name VARCHAR(256), Account VARCHAR(256), Balance VARCHAR(256), CardNumber VARCHAR(256), Password VARCHAR(256))")
        ###When opening the program for the second time, you should comment the lines.==>(line 18,19) 
        #Otherwise, it will give an error because it will try to recreate the database and table.
    
    def insert(self):
        self.VALUES=self.mylist
        self.sql="INSERT INTO customers (Bank,Name,Account,Balance,CardNumber,Password) VALUES(%s,%s,%s,%s,%s,%s)"
        self.cursor.executemany(self.sql,self.VALUES)
        self.mydb.commit()
        self.mydb.close()


def new_customer_insert():
    list=[]
    print("Fill in the information to add new customers.")
    Bank=input("Bank?")
    Name=input("Name?")
    Account=input("Account number?")
    Balance=input("Balance")
    Card_Number=input("Card Number?")
    Password=input("Password?")
    list.append((Bank,Name,Account,Balance,Card_Number,Password))
    answer=input("Do you want to insert new customer? y/n")

    if answer=="y":
        return new_customer_insert()

    if answer=="n":
        print("Recording...")
        Customer(list)



def create_customers():
    list=[("İng Bank","Fatih Yalçın","56789134","57935","913648","1857"),
    ("Ziraat Bank","Esmer Gürsoy","12784394","47359","378426","2973"),
    ("Vakıf Bank","Osman Gültekin","73565549","1000","943586","1771"),
    ("Qnb Bank","Caner Erik","64665891","5000","189732","7492")]
    
    Customer(list)

#If the program is run as the main program, the customer adds only
#adding new customers with the following function
if __name__ == "__main__":
    create_customers()
    new_customer_insert()