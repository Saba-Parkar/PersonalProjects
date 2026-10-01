import mysql.connector as s

#FROM CMD : pip install prettytable
from prettytable import PrettyTable

#PRE-INSTALLED
from datetime import date

db=s.connect(host="localhost",user="root",password="12345")
c=db.cursor()

dbs=s.connect(host="localhost",user="root",password="12345")
cr=dbs.cursor()

#--------------------------------------------- DROP AND RESET ----------------------------------------------------------------
##
##c.execute("CREATE DATABASE EMPLOYEE")
##cr.execute("create database cafe")
##
cr.execute("USE cafe")
c.execute("USE EMPLOYEE")
##
##cr.execute("drop database cafe")
##c.execute("drop database employee")
##
##cr.execute("drop table menu")
##cr.execute("drop table reviews")
##cr.execute("drop table customer")
##
##cr.execute("drop table histock")
##cr.execute("drop table stock")
##
##c.execute("DROP TABLE MANAGEMENT_DEPT")
##c.execute("DROP TABLE SERVICE_DEPT")
##c.execute("DROP TABLE DELIVERY_DEPT")
##c.execute("DROP TABLE BARISTA_DEPT")
##c.execute("DROP TABLE CLEANING_DEPT")
##c.execute("DROP TABLE FIRED_EMPLOYEES")
##

#------------------------------------------- MENU AND REVIEWS TABLES ------------------------------------------------------------------
##
##cr.execute("create table menu(Item_id integer PRIMARY KEY,Item_name varchar(50),Category varchar(25),Price decimal(5,2))""")
##cr.execute("insert into menu values(1,'Espresso','Beverage',10)")
##cr.execute("insert into menu values(2,'Tea','Beverage',6)")
##cr.execute("insert into menu values(3,'Latte americano','Beverage',10)")
##cr.execute("insert into menu values(4,'Brownie','Pastry',10)")
##cr.execute("insert into menu values(5,'Tiramisu','Pastry',15)")
##cr.execute("insert into menu values(6,'Strawberry cheese cake','Pastry',15)")
##cr.execute("insert into menu values(7,'Vanila Delight','Dessert',8)")
##cr.execute("insert into menu values(8,'Chocolate Chip Cookie Dough','Dessert',10)")
##cr.execute("insert into menu values(9,'Cookies and Cream','Dessert',10)")
##cr.execute("insert into menu values(10,'Muffins','Bakery and Snacks',4)")
##cr.execute("insert into menu values(11,'Cookies','Bakery and snacks',5)")
##cr.execute("insert into menu values(12,'Croissants','Bakery and snacks',8)")
##
##cr.execute("Create table Reviews( cname varchar(25),reviews varchar(100))")
##cr.execute("insert into Reviews values('Snoopy','Excellent Tiramisu cake')")
##
##cr.execute("create table customer(mname varchar(30) PRIMARY KEY,contactno int)")
##cr.execute("insert into customer values('Snoopy',055676767)")
##cr.execute("insert into customer values('Johnny',055232323)")

dbs.commit()

#---------------------------------------- STOCK AND SUPPLIER TABLES ---------------------------------------------------------------------
      
##cr.execute('create table histock (product varchar(35),quantity integer(5),category varchar(20),date date)')
##cr.execute("create table stock(product varchar(20),quantity integer(5),category varchar(20))")
##cr.execute('insert into stock values ("Coffee bags",20,"Beverages")')
##cr.execute('insert into stock values ("Tea bags",35,"Beverages")')
##cr.execute('insert into stock values ("Milk",49,"Beverages")')
##cr.execute('insert into stock values ("Sugar",37,"Beverages")')
##cr.execute('insert into stock values ("Cakes",15,"Bakery")')
##cr.execute('insert into stock values ("Pastries",20,"Bakery")')
##cr.execute('insert into stock values ("Cups",50,"Plastic")')
##cr.execute('insert into stock values ("Plates",40,"Plastic")')
##dbs.commit()

#-------------------------------------------- EMPLOYEE TABLES -----------------------------------------------------------------

##c.execute("CREATE TABLE MANAGEMENT_DEPT(EMPLOYEE_ID int(6),NAME char(20),STATUS varchar(15),JOB_TITLE varchar(20),HIRE_DATE date,PHONE_NUMBER varchar(11),MONTHLY_SALARY int(10))")
##c.execute("INSERT INTO MANAGEMENT_DEPT VALUES('1001','Mia Ricky','Clocked-Out','Manager','2025-01-02','0552314364','40000')")
##c.execute("INSERT INTO MANAGEMENT_DEPT VALUES('1002','Kia Lolly','Clocked-Out','Asst.Manager','2025-06-14','0554254373', '20000')")
##c.execute("INSERT INTO MANAGEMENT_DEPT VALUES('1003','Textar Jess','Clocked-Out','Supervisor','2025-03-23','0583014234', '10000')")
##c.execute("INSERT INTO MANAGEMENT_DEPT VALUES('1004','Lara Chen','Clocked-Out','HR','2025-05-29','0555552233','18000')")
##c.execute("INSERT INTO MANAGEMENT_DEPT VALUES('1005','Sarah Lee','Clocked-Out','Branch Manager','2025-04-01','0555552244','80000')")
##
##
##c.execute("CREATE TABLE SERVICE_DEPT(EMPLOYEE_ID int(6),NAME char(20),STATUS varchar(15),JOB_TITLE varchar(30),HIRE_DATE date,PHONE_NUMBER varchar(11),MONTHLY_SALARY int(10))")
##c.execute("INSERT INTO SERVICE_DEPT VALUES('2001','Alice Joy','Clocked-Out','Waitress','2023-02-01','0551112233','3500')")
##c.execute("INSERT INTO SERVICE_DEPT VALUES('2002','Bella Ray','Clocked-Out','Waitress','2023-03-15','0551112244','3500')")
##c.execute("INSERT INTO SERVICE_DEPT VALUES('2003','Charlie Tan','Clocked-Out','Waiter','2023-02-10','0551112255','3500')")
##c.execute("INSERT INTO SERVICE_DEPT VALUES('2004','Diana Lee','Clocked-Out','Cashier','2023-05-20','0551112266','3000')")
##c.execute("INSERT INTO SERVICE_DEPT VALUES('2005','Ella Kim','Clocked-Out','Cashier','2023-06-25','0551112277','3000')")
##c.execute("INSERT INTO SERVICE_DEPT VALUES('2006','Fiona Yu','Clocked-Out','Customer Service Rep','2023-04-12','0551112288','4000')")
##c.execute("INSERT INTO SERVICE_DEPT VALUES('2007','Grace Lim','Clocked-Out','Front Counter Staff','2023-07-05','0551112299','3200')")
##c.execute("INSERT INTO SERVICE_DEPT VALUES('2008','Hannah Tan','Clocked-Out','Front Counter Staff','2023-08-18','0551112300','3200')")
##c.execute("INSERT INTO SERVICE_DEPT VALUES('2009','Ivy Ong','Clocked-Out','Front Counter Staff','2023-09-22','0551112311','3200')")
##
##
##c.execute("CREATE TABLE BARISTA_DEPT(EMPLOYEE_ID int(6),NAME char(20),STATUS varchar(15),JOB_TITLE varchar(30),HIRE_DATE date,PHONE_NUMBER varchar(11),MONTHLY_SALARY int(10))")
##c.execute("INSERT INTO BARISTA_DEPT VALUES('3001','Jack Lee','Clocked-Out','Head Barista','2021-01-01','0552222233','8000')")
##c.execute("INSERT INTO BARISTA_DEPT VALUES('3002','Kevin Tan','Clocked-Out','Senior Barista','2021-03-15','0552222244','6000')")
##c.execute("INSERT INTO BARISTA_DEPT VALUES('3003','Liam Wong','Clocked-Out','Senior Barista','2021-05-20','0552222255','6000')")
##c.execute("INSERT INTO BARISTA_DEPT VALUES('3004','Mia Tan','Clocked-Out','Latte Artist','2022-01-12','0552222266','4500')")
##c.execute("INSERT INTO BARISTA_DEPT VALUES('3005','Nina Lim','Clocked-Out','Latte Artist','2022-02-18','0552222277','4500')")
##c.execute("INSERT INTO BARISTA_DEPT VALUES('3006','Owen Lee','Clocked-Out','Latte Artist','2022-03-25','0552222288','4500')")
##c.execute("INSERT INTO BARISTA_DEPT VALUES('3007','Pia Chan','Clocked-Out','Junior Barista','2023-05-05','0552222299','3500')")
##c.execute("INSERT INTO BARISTA_DEPT VALUES('3008','Quinn Ong','Clocked-Out','Junior Barista','2023-06-15','0552222300','3500')")
##c.execute("INSERT INTO BARISTA_DEPT VALUES('3009','Ria Lim','Clocked-Out','Junior Barista','2023-07-20','0552222311','3500')")
##c.execute("INSERT INTO BARISTA_DEPT VALUES('3010','Sam Tan','Clocked-Out','Junior Barista','2023-08-25','0552222322','3500')")
##
##c.execute("CREATE TABLE CLEANING_DEPT(EMPLOYEE_ID int(6),NAME char(20),STATUS varchar(15),JOB_TITLE varchar(30),HIRE_DATE date,PHONE_NUMBER varchar(11),MONTHLY_SALARY int(10))")
##c.execute("INSERT INTO CLEANING_DEPT VALUES('4001','Tina Lee','Clocked-Out','Janitor','2021-01-02','0553332233','3000')")
##c.execute("INSERT INTO CLEANING_DEPT VALUES('4002','Uma Tan','Clocked-Out','Janitor','2021-02-15','0553332244','3000')")
##c.execute("INSERT INTO CLEANING_DEPT VALUES('4003','Vera Ong','Clocked-Out','Dishwasher','2022-03-10','0553332255','2800')")
##c.execute("INSERT INTO CLEANING_DEPT VALUES('4004','Will Lim','Clocked-Out','Dishwasher','2022-04-20','0553332266','2800')")
##c.execute("INSERT INTO CLEANING_DEPT VALUES('4005','Xena Chan','Clocked-Out','Dishwasher','2022-05-05','0553332277','2800')")
##c.execute("INSERT INTO CLEANING_DEPT VALUES('4006','Yara Yu','Clocked-Out','Dishwasher','2022-06-18','0553332288','2800')")
##c.execute("INSERT INTO CLEANING_DEPT VALUES('4007','Zoe Lim','Clocked-Out','Sanitation Staff','2023-01-12','0553332299','3200')")
##c.execute("INSERT INTO CLEANING_DEPT VALUES('4008','Adam Tan','Clocked-Out','Sanitation Staff','2023-02-20','0553332300','3200')")
##c.execute("INSERT INTO CLEANING_DEPT VALUES('4009','Brian Lee','Clocked-Out','Sanitation Staff','2023-03-28','0553332311','3200')")
##
##
##c.execute("CREATE TABLE DELIVERY_DEPT(EMPLOYEE_ID int(6),NAME char(20),STATUS varchar(15),JOB_TITLE varchar(30),HIRE_DATE date,PHONE_NUMBER varchar(11),MONTHLY_SALARY int(10))")
##c.execute("INSERT INTO DELIVERY_DEPT VALUES('5001','Carl Tan','Clocked-Out','Delivery Driver','2022-01-01','0554442233','4000')")
##c.execute("INSERT INTO DELIVERY_DEPT VALUES('5002','Derek Lim','Clocked-Out','Delivery Driver','2022-02-15','0554442244','4000')")
##c.execute("INSERT INTO DELIVERY_DEPT VALUES('5003','Ethan Ong','Clocked-Out','Delivery Driver','2022-03-20','0554442255','4000')")
##c.execute("INSERT INTO DELIVERY_DEPT VALUES('5004','Felix Lee','Clocked-Out','Delivery Driver','2022-05-05','0554442266','4000')")
##c.execute("INSERT INTO DELIVERY_DEPT VALUES('5005','Gina Tan','Clocked-Out','Delivery Driver','2022-06-18','0554442277','4000')")
##c.execute("INSERT INTO DELIVERY_DEPT VALUES('5006','Hugo Chan','Clocked-Out','Dispatch Assistant','2023-01-12','0554442288','3500')")
##c.execute("INSERT INTO DELIVERY_DEPT VALUES('5007','Iris Lim','Clocked-Out','Logistics Coordinator','2023-02-20','0554442299','5000')")
##
##c.execute("CREATE TABLE FIRED_EMPLOYEES(EMPLOYEE_ID int(6), NAME char(15), FEEDBACK varchar(500))")

db.commit()

#---------------------------------------------- MENU AND REVIEWS FUNCTIONS ---------------------------------------------------------------

def owner_menu():
    while True:
            print("\n<< MAIN MENU >>\n")
            print("1. View")
            print("2. Add Item")
            print("3. Update Item")
            print("4. Delete Item")
            print("5. Exit")
            ch=input("Enter your choice:")

            if ch=="1":
                Main_menu()
            elif ch=="2":
                Add_item()
            elif ch=="3":
                Update_item()
            elif ch=="4":
                Delete_item()
            elif ch=="5":
                print("Exiting :( ")
                break
            else:
                print("Enter a valid number")

def Main_menu():
    print()
    
    cr.execute("Select * from menu")
    d=cr.fetchall()
    columns=("S.NO","ITEM","CATEGORY","PRICE")
    table=PrettyTable(columns)
             
    for i in d:
        table.add_row(i)
    print(table)

def Add_item():
    while True:
        id=int(input("Enter Item id:"))
        cr.execute("SELECT * FROM menu WHERE Item_id=%s",(id,))
        d=cr.fetchone()
        if d!=None:
            print("Item id already exists")
            break

        name=input("Enter Item name:").title()
        category=input("Enter Category:").title()
        price=float(input("Enter Price:"))
        cr.execute("INSERT INTO menu VALUES(%s,%s,%s,%s)",(id,name,category,price))
        dbs.commit()
        print("Item added successfully!")
        e=input("would you like to add more items (yes/no):").lower()
        if e=="no":
             print("Returning..")
             break

def Update_item():

    while True :
        print("\n1.Update price\n2.Update name\n3.Exit")
        ch=input("enter your choice")

        
        if ch=="1":
            id=int(input("Enter item id:"))
            price=float(input("Enter new price:"))
            cr.execute("SELECT * FROM menu WHERE Item_id=%s",(id,))
            d=cr.fetchone()
            if not d:
                print("Item id doesnt exist")
                break

            else:
                cr.execute("UPDATE Menu SET Price=%s WHERE Item_id=%s",(price,id))
                dbs.commit()
                print("Item updated")
            
        elif ch=="2":
            
            id=int(input("Enter item iD:"))
            name=input("Enter new item name:")
            
            cr.execute("SELECT * FROM menu WHERE Item_id=%s",(id,))
            d=cr.fetchone()
            if not d:
                print("Item id doesnt exist")
                break

            else:
                cr.execute("UPDATE Menu SET Item_name=%s WHERE Item_id=%s",(name,id))
                dbs.commit()
                print("Item name updated")
                
        elif ch=="3":
            print("exiting")
            break
        else :
            print("Invalid choice")
            
            
            
def Delete_item():
    id=int(input("enter id to be deleted"))
    cr.execute("SELECT * FROM menu WHERE Item_id=%s",(id,))
    d=cr.fetchone()
    if not d:
        print("Item id doesnt exist")
        return
    else:
        cr.execute("DELETE FROM MENU WHERE item_id=%s",(id,))
        print("Item successfully deleted!")
    dbs.commit()
        
    
def view():
    print("\n<< REVIEWS >>\n")
    cr.execute("Select * from reviews")
    d=cr.fetchall()
    for i in d:
        print(i[0],"-",i[1])

def menu():
    while True:
        print("1.View Menu")
        print("2.Search item\n3.Exit")
        ch=int(input("\nEnter your choice :"))
        if ch==1:
            Main_menu()
        elif ch==2:
            searchmenu()
        elif ch==3:
            print("Exiting")
            return
        else:
            print("Invalid choice")
        
def searchmenu():
    s=input("\nEnter item to search :").title()
    cr.execute("SELECT * FROM MENU WHERE Item_name=%s",(s,))
    a=cr.fetchall()                
    if not a:
         print("Invalid item")
         return
    columns=("ITEM ID","ITEM NAME","CATEGORY","PRICE")
    table=PrettyTable(columns)
    for i in a:
         table.add_row(i)
    print(table)



def sl():
    name=input("Enter your name :").strip().title()
    cr.execute("SELECT * FROM CUSTOMER WHERE mname=%s",(name,))
    a=cr.fetchall()
    
    if a!=[]:
        print("\nCustomer name taken\nPlease choose another name or add full name")
        return
    try:
        no=int(input("\nEnter contact no :"))
    except:
        print("Invalid contact no.")
        return
    print("Your password is :customer123")
    cr.execute("INSERT INTO CUSTOMER values(%s,%s)",(name,no))
    print("Sign-up successful,Please login before placing order")
    dbs.commit()

def place():
    print("Login to place order.")
    print("\n1.Log in \n2.Exit")
    ch=int(input("Enter the option of your choice: "))
    
    if ch==1:
        name=input("Enter your name: ")
        password=input("Enter your password: ")
        if password=="customer123":
            cr.execute("SELECT * FROM CUSTOMER WHERE mname=%s",(name,))
            a=cr.fetchall()
            if a == []:
                print("Not signed up")
                return 
            else:
                print("Welcome",name, "!")
                order()    
        else:
            print("Wrong password")
            return
        
    elif ch==2:
        print("Exiting")
        return
    
def order ():
    Main_menu()
    total=0
    products=[]
    while True:
        order=input("Enter Item name to buy:").title()
        cr.execute("SELECT * FROM MENU WHERE Item_name=%s",(order,))
        d=cr.fetchall()
        if not d:
            print("\nItem doesnt exist")
            print("Would u still like to continue your order?")
            print("1.Yes\n2.No")
            c=int(input("Enter option of your choice:"))
            if c==1:
                print("Continuing order...")
            elif c==2:
                return
            else:
                print("Invalid choice please try again")
    
        else:
            quantity=int(input("Enter quantity: "))
            mprice=d[0][3]
            pp=quantity*mprice
            print("Price for item added :",pp)
            total+=quantity*mprice
            print("Current total amount :",total)
            prod=[order,quantity,pp]
            products.append(prod)
        o=input("\nWould you like to add more (yes/no)?")
        if o=="no":
            print("ITEM X QUANTITY\t\tAMOUNT")  
            for i in products:
                print(i[0],"x",i[1],"\t\t",i[2])
            print("TOTAL BILL AMOUNT :",total)
            print("Order complete!\nPlease pay at the Cash Counter")
            break

def add():
    name=input("Enter name :")
    review=input("Enter review :")
    cr.execute("insert into Reviews values(%s,%s)",(name,review))
    print("\nWe appreciate your review ! Thanks for visiting :D")
    dbs.commit()


def review():
    while True:
        print("\n1.Add a review\n2.Show all reviews\n3.Exit")
        ch=int(input("Enter choice : "))
        if ch==1:
            add()
        elif ch==2:
            view()
        elif ch==3:
            print("EXITING!!")
            break

        else:
            print("Invalid choice")

def customer():        
    while True:
        print()
        print("\n<< CUSTOMER >>")
        print()
        print("Welcome to ASD Cafe !\n1.Main Menu\n2.Sign Up\n3.Place Order\n4.Review\n5.Exit")
        print()
        chc=int(input("Select Option :"))
        print()
        
        if chc==1:
            menu()
        elif chc==2:
            name=sl()
        elif chc==3:
            place()
        elif chc==4:
            review()
        elif chc==5:
            print("Exiting!")
            print("Thank you for visiting ASD cafe\nDo write us a review :D\n")
            break
        else:
            print("Invalid choice")
            
          



#---------------------------------------------- STOCK AND SUPPLIER FUNCTIONS ---------------------------------------------------------------


def admin_stock():
    while True:
        print("\n<< STOCKS>> \n")
        print("1.View stock")
        print("2.Remove stock quantity")
        print("3.Add new item")
        print("4.Update item name")
        print("5.Remove item from stock")
        print("6.View previous stock history")
        print("7.Exit")
        ch=int(input("\nEnter the number of your choice:"))

        if ch==1:
            st_view()

        elif ch ==2:
            remove_stock()

        elif ch==3:
            add_item()

        elif ch==4:
            update_item()

        elif ch==5:
            remove_item()

        elif ch==6:
            hi_view()

        elif ch==7:
            break

        else:
            print("Invalid choice please try again")


def remove_stock():
    
    cat=s_cat()
    if cat==None :
        return
    cr.execute("SELECT product,quantity FROM stock WHERE category=%s",(cat,))
    data=cr.fetchall()
    
    if len(data)==0:
        print("No products in this category currently.\n")
        return

    columns=("PRODUCT","QUANTITY")
    table=PrettyTable(columns)

    for i in data:
        table.add_row(i)
    print(table)
        
    prod=input("\nEnter the product name to remove quantity:")
    cr.execute("SELECT quantity FROM stock WHERE product=%s AND category=%s", (prod,cat))
    sdata=cr.fetchone()
    
    if sdata is None:
        print("Item not found in stock.\n")
        return 

    qty=int(input("\nEnter quantity to remove:"))
    
    if qty > sdata[0]:
        print("Quantity higher than stock.\nUnable to remove stock")
        return 
    
    cr.execute("UPDATE stock SET quantity=quantity-%s WHERE product=%s AND category=%s",(qty,prod,cat))
    dbs.commit()
    print("Stock removed and updated !.\n")
    
    cr.execute("SELECT product,quantity FROM stock WHERE category=%s",(cat,))
    data=cr.fetchall()
    columns=("PRODUCT","QUANTITY")
    table=PrettyTable(columns)

    for i in data:
        table.add_row(i)
    print(table)


def add_item():
    cat=s_cat()
    if cat==None :
        return
    prod=input("Enter the name of the new product :")
    cr.execute("SELECT * FROM stock WHERE product=%s AND category=%s",(prod,cat))
    data=cr.fetchone()
    if data != None:
        print("\nItem already exists in this category.")
        return None
        
    cr.execute("INSERT INTO stock (product,quantity,category) VALUES (%s,%s,%s)",(prod,0,cat))
    dbs.commit()
    print("\nNew item added !.")
    cr.execute("SELECT product,quantity FROM stock WHERE category=%s",(cat,))
    data=cr.fetchall()
    columns=("PRODUCT","QUANTITY")
    table=PrettyTable(columns)

    for i in data:
        table.add_row(i)
    print(table)

def update_item():
    cat=s_cat()
    if cat==None :
        return
    cr.execute("SELECT product,quantity FROM stock WHERE category=%s",(cat,))
    data=cr.fetchall()
    if data == None:
        print("No items in this category.")
        return None
    columns=("PRODUCT","QUANTITY")
    table=PrettyTable(columns)
    for i in data:
        table.add_row(i)
    print(table)
    old=input("Enter item name to change:")
    name=input("Enter new item name:")
    cr.execute("SELECT * FROM stock WHERE PRODUCT=%s and category=%s",(old,cat))
    data=cr.fetchone()
    
    if data == None :
        print("Item does not exist")
        return

    else:
        cr.execute("UPDATE stock SET PRODUCT=%s WHERE PRODUCT=%s and category=%s",(name,old,cat))
        dbs.commit()
        print("Item name updated")

def remove_item():
    cat=s_cat()
    if cat==None :
        return
    cr.execute("SELECT product,quantity FROM stock WHERE category=%s",(cat,))
    data=cr.fetchall()
    if len(data)==0:
        print("\nNo products in this category currently.")
        return
    
    columns=("PRODUCT","QUANTITY")
    table=PrettyTable(columns)

    for i in data:
        table.add_row(i)
    print(table)

        
    prod=input("\nEnter the name of the product to remove completely :")
    cr.execute("SELECT * FROM stock WHERE product=%s AND category=%s",(prod,cat))
    data=cr.fetchone()
    if data==None:
        print("\nItem not found in stock.")
        return 
    
    cr.execute("DELETE FROM stock WHERE product=%s AND category=%s",(prod,cat))
    dbs.commit()
    print("\nItem removed from stock list.")
    
    cr.execute("SELECT product,quantity FROM stock WHERE category=%s",(cat,))
    data=cr.fetchall()
    columns=("PRODUCT","QUANTITY")
    table=PrettyTable(columns)

    for i in data:
        table.add_row(i)
    print(table)

def st_view():
    cat=s_cat()
    if cat==None :
        return
        
    cr.execute("SELECT product,quantity FROM stock WHERE category=%s", (cat,))
    data=cr.fetchall()

    columns=("PRODUCT","QUANTITY")
    table=PrettyTable(columns)

    for i in data:
        table.add_row(i)
    print(table)


def hi_view():
    cat=s_cat()
    if cat==None :
        return
    cr.execute("SELECT product,quantity,date FROM histock WHERE category=%s",(cat,))
    data=cr.fetchall()
    
    if len(data)==0:
        print("\nNo previous stock history currently.")
        return
    print("\nPrevious history of supplies to cafe:\n")

    columns=("PRODUCT","QUANTITY","DATE")
    table=PrettyTable(columns)

    for i in data:
        table.add_row(i)
    print(table)

def s_cat():
    
    print("1.Bakery")
    print("2.Beverages")
    print("3.Plastic")
    print("4.Return back")

    c=int(input("Enter the number of category: "))
    if c==1:
        cat="Bakery"
    elif c==2:
        cat="Beverages"
    elif c==3:
        cat="Plastic"
    elif c==4:
        return None
    else:
        print("Invalid category selected")
        return None
    return cat

def supplier():
    while True:
        print("\n[ SUPPLIER ]")
        print("\n1.View current stock")
        print("2.Login as supplier")
        print("3.Exit")
        choice=int(input("\nEnter the number of your choice :"))
        
        if choice==1:
            st_view()
            
        elif choice==2:
            s_login()

        elif choice==3:
            break

        else:
            print("Invalid choice please try again")


def supply():
    cat=s_cat()
    if cat==None :
        return
    cr.execute("SELECT product,quantity FROM stock WHERE category=%s",(cat,))
    data=cr.fetchall()
    if len(data)==0:
        print("\nNo products in this category currently.")
        return
    
    columns=("PRODUCT","QUANTITY")
    table=PrettyTable(columns)

    for i in data:
        table.add_row(i)
    print(table)

        
    prod=input("\nEnter the name of the product to supply :")
    cr.execute("SELECT quantity FROM stock WHERE product=%s AND category=%s",(prod,cat))
    sdata=cr.fetchone()
    if sdata==None:
        print("Item not found in stock.")
        return 
        
    qty=int(input("\nEnter the quantity of product to supply:"))
    s_date=date.today()
    cr.execute("UPDATE stock SET quantity=quantity+%s WHERE product=%s AND category=%s",(qty, prod,cat))
    cr.execute("INSERT INTO histock (product, quantity, category, date) VALUES (%s,%s,%s, %s)",(prod,qty,cat,s_date))
    dbs.commit()
    print("\nStock updated :D")
    
    cr.execute("SELECT product,quantity FROM stock WHERE category=%s",(cat,))
    data=cr.fetchall()
    
    columns=("PRODUCT","QUANTITY")
    table=PrettyTable(columns)

    for i in data:
        table.add_row(i)
    print(table)



def s_login():
    pw=input("Enter the password for supplier to login:")
    if pw=="supplierpassword":
        while True:
            print("1.View current stock")
            print("2.Supply stock to cafe")
            print("3.View previous stock history")
            print("4.Logout\n")
            choice=int(input("Enter the number of your choice:"))

            if choice==1:
                st_view()

            elif choice==2:
                supply()

            elif choice==3:
                hi_view()

            elif choice==4:
                break

            else:
                print("\nIncorrect option please try again")
            
    else:
        print("\nIncorrect password")
        print("1.Try password again")
        print("2.Return")
        choice=int(input("Enter option of ur choice:"))

        if choice==1:
            s_login()

        elif choice==2:
            supplier()

        else:
            print("\nIncorrect option please try again")



#----------------------------------------------------- EMPLOYEE AND ABOUT US FUNCTIONS ---------------------------------------------------------------------


def actions(table):
    while True:
        print("\nSELECT ACTION :\n1.SEARCH\n2.HIRE\n3.FIRE\n4.EDIT\n5.VIEW LIST\n6.BACK\n")
        ch=int(input("Enter choice :"))

        if ch==1:
            search(table)    

        elif ch==2:
            hire(table)
            
        elif ch==3:
            fire(table)
            
        elif ch==4:
            edit(table)

        elif ch==5:
            showlist(table)
            
        elif ch==6:
            break
        else :
            print("Invalid choice.Please chose a valid option (1/2/3/4/5/6)")


            
def showlist(table):
    c.execute("SELECT * FROM {} ORDER BY EMPLOYEE_ID ASC".format(table))
    view=c.fetchall()
    columns=("EMPLOYEE_ID","NAME","STATUS","JOB_TITLE","HIRE_DATE","PHONE_NUMBER","MONTHLY_SALARY")

    table=PrettyTable(columns)

    for i in view:
        table.add_row(i)
    print(table)
    
def search(table):
    n=int(input("Enter employee ID :"))
    c.execute("SELECT * FROM {} WHERE EMPLOYEE_ID=%s".format(table),(n,))
    v=c.fetchall()
    
    if len(v)!=0:
        columns=("EMPLOYEE_ID","NAME","STATUS","JOB_TITLE","HIRE_DATE","PHONE_NUMBER","MONTHLY_SALARY")
        emp=PrettyTable(columns)
        
        for i in v:
            emp.add_row(i)
        print(emp)

    else:
        print("Employee does not exsist,Try again.")


def hire(table):

    
    emp_id=input("Enter employee ID :")
    c.execute("SELECT * FROM {} WHERE EMPLOYEE_ID=%s".format(table),(emp_id,))
    check=c.fetchall()

    if not check:
        emp_name=input("Enter employee name :")
        emp_title=input("Enter employee's Job Title :")
        emp_number=input("Enter employee's number :")
        emp_salary=input("Enter employee's salary: ")

        emp_status="Clocked-Out"

        today=date.today()

        c.execute("INSERT INTO {} VALUES (%s,%s,%s,%s,%s,%s,%s)".format(table),(emp_id,emp_name,emp_status,emp_title,today,emp_number,emp_salary))
        c.execute("DELETE FROM FIRED_EMPLOYEES WHERE EMPLOYEE_ID=%s",(emp_id,))
        db.commit()

    else:
        print("Employee id already exsists")
    

def fire(table):

    nf=int(input("Enter employee ID :"))
    c.execute("SELECT * FROM {} WHERE EMPLOYEE_ID={}".format(table,nf))
    vf=c.fetchall()
    msg=input("Enter employee Feedback :")

    if len(vf)!=0:
        name=vf[0][1] 
        c.execute("DELETE FROM {} WHERE EMPLOYEE_ID={}".format(table,nf))
        c.execute("INSERT INTO FIRED_EMPLOYEES VALUES({},'{}','{}')".format(nf,name,msg))
        db.commit()
        print("\nEmployee",name,"has been fired.")

    else:
        print("Employee does not exist, Try again.")

        
        
def edit(table):
    id=input("Enter Employee ID to edit :")
    c.execute("SELECT * FROM {} WHERE EMPLOYEE_ID=%s".format(table),(id,))
    rec=c.fetchall()

    if len(rec)!=0:
        while True:  
            print("\nChoose a field to edit :")
            print("1.Employee ID")
            print("2.Name")
            print("3.Job Title")
            print("4.Phone Number")
            print("5.Salary")
            print("6.GO BACK")
            ch=int(input("\nEnter choice :"))

            if ch==1:
                newid=input("Enter new Employee ID :")
                c.execute("UPDATE {} SET EMPLOYEE_ID=%s WHERE EMPLOYEE_ID=%s".format(table),(newid,id))
                id=newid  

            elif ch==2:
                newname=input("Enter new Name :")
                c.execute("UPDATE {} SET NAME=%s WHERE EMPLOYEE_ID=%s".format(table),(newname,id))

            elif ch==3:
                newtitle=input("Enter new Job Title :")
                c.execute("UPDATE {} SET JOB_TITLE=%s WHERE EMPLOYEE_ID=%s".format(table),(newtitle,id))

            elif ch==4:
                newphone=input("Enter new Phone Number :")
                c.execute("UPDATE {} SET PHONE_NUMBER=%s WHERE EMPLOYEE_ID=%s".format(table),(newphone,id))

            elif ch==5:
                newsalary=input("Enter new Salary :")
                c.execute("UPDATE {} SET MONTHLY_SALARY=%s WHERE EMPLOYEE_ID=%s".format(table),(newsalary,id))

            elif ch==6:
                break
            else:
                print("Invalid choice.")
                continue 

            db.commit()
            print("Field has been updated successfully!")

           
            print("\nEdit another field ?\n1.Yes\n2.No")
            chh=int(input("Enter choice (1/2):"))
            
            if chh==2:
                break
            elif chh==1:
                continue
            else :
                print("Please chose a number (1/2):D")
    else:
        print("Employee does not exist.Try again :D")

def clocksystem(empid   ,table):

    c.execute("SELECT * FROM FIRED_EMPLOYEES WHERE EMPLOYEE_ID={}".format(empid))
    fdata=c.fetchall()
    if len(fdata)!=0:
        print("\nSorry !",fdata[0][1],"you have been fired.")
        print("Thank you for working with ASD CAFE !")
        print()
        print("Performance Feedback:",fdata[0][2])
        print()
        return

    c.execute("SELECT STATUS,NAME FROM {} WHERE EMPLOYEE_ID={}".format(table,empid))
    sn=c.fetchall()
    
    if len(sn)!=0:
        status=sn[0][0]
        name=sn[0][1]

        while True :
                
            print("\nWelcome",name,"would you like to :")
            print("""
1.CLOCK-IN
2.CLOCK-OUT
3.GO BACK""")
            act=int(input("\nEnter choice :"))
        
            if act==1:
                
                if status=="Clocked-In":
                    print("\nYou are already CLOCKED-IN,",name,"\n")
                else:
                    c.execute("UPDATE {} SET STATUS='Clocked-In' WHERE EMPLOYEE_ID={}".format(table,empid))
                    db.commit()
                    
                    status="Clocked-In"  
                    print("\nWelcome",name,"You have CLOCKED-IN successfully.\nHave a great shift!\n")
                    
            elif act==2:
                
                if status=="Clocked-Out":
                    print("\nYou are already CLOCKED-OUT",name,"\n")
                else:
                    c.execute("UPDATE {} SET STATUS='Clocked-Out' WHERE EMPLOYEE_ID={}".format(table,empid))
                    db.commit()
                    
                    status="Clocked-Out"  
                    print("\nGoodbye",name,"\nYou have CLOCKED-OUT successfully.\n")
                    
            elif act==3:
                break
            
    else :
        print("You are not an employee here :[\n")


def owneremp():
    
    while True:
        print("""\n<< EMPLOYEE LIST >>

EMPLOYEE DEPARTMENTS:

1.MANAGEMENT DEPARTMENT
2.SERVICE DEPARTMENT
3.BARISTA DEPARTMENT
4.CLEANING DEPARTMENT
5.DELIVERY DEPARTMENT
6.GO BACK
    """)

        ch=int(input("CHOICE :"))

        if ch==1:
            table="MANAGEMENT_DEPT"
            showlist(table)
            actions(table)

        elif ch==2:
            table="SERVICE_DEPT"
            showlist(table)
            actions(table)

        elif ch==3:
            table="BARISTA_DEPT"
            showlist(table)
            actions(table)

        elif ch==4:
            table="CLEANING_DEPT"
            showlist(table)
            actions(table)

        elif ch==5:
            table="DELIVERY_DEPT"
            showlist(table)
            actions(table)
            
        elif ch==6:
            break

def emp():
    while True:
        print("""

    [ EMPLOYEE ]

Choose the department you work in :

1.MANAGEMENT DEPARTMENT
2.SERVICE DEPARTMENT
3.BARISTA DEPARTMENT
4.CLEANING DEPARTMENT
5.DELIVERY DEPARTMENT
6.GO BACK

    """)

        ch=int(input("CHOICE :"))

        if ch==1:
            table="MANAGEMENT_DEPT"
            empid=int(input("Enter your employee id :"))
            clocksystem(empid,table)
            

        elif ch==2:
            table="SERVICE_DEPT"
            empid=int(input("Enter your employee id :"))
            clocksystem(empid,table)
            

        elif ch==3:
            table="BARISTA_DEPT"
            empid=int(input("Enter your employee id :"))
            clocksystem(empid,table)
            

        elif ch==4:
            table="CLEANING_DEPT"
            empid=int(input("Enter your employee id :"))
            clocksystem(empid,table)
            

        elif ch==5:
            table="DELIVERY_DEPT"
            empid=int(input("Enter your employee id :"))
            clocksystem(empid,table)
            
        elif ch==6:
            break

def aboutus():
    
    while True :
        print(r"""
                                                                                  [ ABOUT US ]
                                                                                
                                                                            1.BRANCHES AND CONTACT INFO
                                                                            2.STAFF 
                                                                            3.LATEST UPDATES
                                                                            4.REVIEWS
                                                                            5.RETURN TO HOME PAGE
""")
        ch=int(input("                                                            SELECTION :"))
        
            
        if ch==1:
                
            print(r"""
═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                    << 📍 ASD CAFE - OUR BRANCHES 📍 >>
═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

1. [MAIN BRANCH] NEW YORK, USA – Times Square

   🏠 Address : 123 Broadway, Manhattan, NY 10036
   📞 Phone   : +1 212-555-1234
   ⏰ Hours   : 7:00 AM – 10:00 PM
   💺 Seating : 80 indoor seats, 20 outdoor
   🌐 Wi-Fi   : Free high-speed Wi-Fi
   📝 Description : Located in the heart of Manhattan, perfect for a quick coffee break or meeting with friends.
   🍰 Specialty   : Classic American Coffee, Artisan Pastries, Nitro Cold Brew

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
2. TOKYO, JAPAN – Shibuya

   🏠 Address : 2-24-12 Shibuya, Tokyo 150-0002
   📞 Phone   : +81 3-1234-5678
   ⏰ Hours   : 7:30 AM – 11:00 PM
   💺 Seating : 60 indoor seats, 10 bar seats
   🌐 Wi-Fi   : Fast and free Wi-Fi
   📝 Description : Modern, minimalist café in Shibuya. Tech-friendly spot for students and professionals.
   🍰 Specialty   : Matcha Lattes, Mochi Desserts, Cold Brew

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
3. MUMBAI, INDIA – Colaba

   🏠 Address : 12 Marine Drive, Colaba, Mumbai, Maharashtra 400001
   📞 Phone   : +91 22 1234 5678
   ⏰ Hours   : 6:30 AM – 9:30 PM
   💺 Seating : 70 indoor, 40 outdoor with sea view
   🌐 Wi-Fi   : Free Wi-Fi
   📝 Description : Stunning café with a view of the Arabian Sea. Perfect for tourists and locals to relax and enjoy coffee.
   🍰 Specialty   : Masala Chai, Samosa Snacks, Cold Coffees

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
4. DUBAI, UAE – Downtown Dubai

   🏠 Address : Burj Khalifa Blvd, Dubai Mall, Dubai
   📞 Phone   : +971 4 123 4567
   ⏰ Hours   : 7:00 AM – 12:00 AM
   💺 Seating : 100 indoor, 30 outdoor
   🌐 Wi-Fi   : Free premium Wi-Fi
   📝 Description : Elegant and luxurious, perfect for business meetings or relaxing after shopping. Offers signature
      drinks with a local twist.
   🍰 Specialty   : Arabic Coffee, Signature Dates Dessert, Specialty Lattes

══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
    """)
                
            
        elif ch==2:
            print("""

===========================================================================================================================================================
                        🏆 ASD CAFE – STAFF PAGE 🏆
===========================================================================================================================================================


    >> OWNER <<
                                                                                                                     ⠀⣀⣀⣀⡀⠀⠀
    👤 Name: Sabdhami Jhonny                                                                                     ⢀ ⢔⡽⠟⠛⠉⠙⠛⠻⣄⠀⣀⣤⣶⠶⣦⣄⠀⠀⠀⠀⠀
    📍 Position: Founder & CEO                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                            ⠀⣠⠷⠋⠀⠀⠀⠀⠀⠀⠀⠀⣿⣸⠁⠀⠀⠀⠈⠻⣿⡄⠀⠀⠀               
    📧 Email: sabdhami.jhonny@asdcafe.com                                                                      ⢸⣿⠃⠀⠀⠀⠀⠀⢸⡀⠀⣼⢸⣇⠀⠀⠀⠀⠀⠀⢸⣷                                                       
                                                                                                               ⢸⣿⡀⠀⠀⠀⠀⠀⠀⠙⠋⠁⠀⠙⠛⠋⠀⠀⠀⠀⣼⡏⠀⠀⠀
    ---------------- Employee of the Month -----------------------------------------------------------          ⢿⢷⣱⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣮⡿⠋⠀        
                                                                                                                 ⠙⠽⣿⣾⣿⣤⣶⣤⣀⠀⠀⠀⡠⣪⠷⠛⠁⠀⠀⠀                                                              
    📌 New York, USA                                                                                                 ⠉⠉⠙⣛⣿⣦⣀⣀⣿⡃⠀⠀⠀⠀⠀                                                            
       - Jane Smith                                                                                                ⢀⣤⠖⠋⠉⠀⠀⠹⣷⣿⡏⠈⠉⠓⢦⡄⠀⠀⠀⠀
    📌 Paris, France                                                                                               ⣾⡁⠀⠀⠀⠀⠀⠀⠘⡏⠓⠀⠀⠀⠀⣿⣿⠀
       - Pierre Dupont ⠀                                                                                          ⢨⣛⣦⣤⣀⣀⣀⠀⠀⢀⣀⣀⣠⡤⣾⣫⣴⠾⠿⣷⡄⠀⠀
    📌 Tokyo, Japan                                                                                               ⠘⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣷⢇⣿⣿⠁⠀⠀⣽⡏
       - Yuki Tanaka     ⠀⠀                                                                                       ⢀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣸⣿⠇⢀⣠⡾⠋⠀
    📌 Mumbai, India                                                                                         ⢀⣠⡶⠉⠀ ⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠚⠉⠱⣦⣄⠀
       - Aarav Patel                                                                                         ⣾⣿⡄⠀⠀⠀ ⠘⢷⣭⣟⣛⣿⣿⢿⣛⣫⣵⠞⠀⠀⠀⠀⣸⡿⣷
    📌 Dubai, UAE                                                                                             ⠙⢿⣿⣶⣤⣄⣀⠀⠀⠈⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⢠⣾⣿⡿⠀
       - Fatima Al Zarooni                                                                                      ⠈⠉⠛⠛⠿⠿⠿⠿⠿⣿⣿⣿⠿⠿⠿⠿⠛⠛⠛⠉                                                                                         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                              
                                                                                                                
                                                                                                               
    ----------------- Employee of the Year -----------------------------------------------------------         
                                                                                                                ⠀
    📌 New York, USA                                                                                              ⠀⠀⠀
      - Michael Brown                                                                                                   ⠀⠀⠀⠀
    📌 Paris, France                                                                                                ⠀
      - Claire Monet                                                                                                
    📌 Tokyo, Japan                                                                                                  
      - Kenji Sato                                                                                                   
    📌 Mumbai, India                                                                                             ⠀⠀
      - Priya Sharma                                                                                            
    📌 Dubai, UAE                                                                                               
      - Ahmed Al Farsi                                                                                          
                                                                                                                ⠀⠀

    -----------------  ASD Employee of the Month -------------------------------------------------------- 

    🏅 Dhanman Jhonny

    ----------------- ASD Employee of the Year ----------------------------------------------------------

    🏅 Lucas Carter
    

    -----------------  Main Branch Staff ----------------------------------------------------------------

    👤 Branch Manager: Sarah Lee
    👤 Assistant Manager: David Kim
    👤 Barista Lead: Mia Tan
    👤 Customer Relations: Alice Joy

====================================================================================================================================
    """)

        elif ch==3:
            print("""
=========================================================================================================================================================
                        📢 ASD CAFE – LATEST UPDATES 📢
=========================================================================================================================================================


------------ New Branch Openings --------------------------------------------------------------------------------------------------------------

🏢 Mumbai, India – Circular Quay Inspired
   - Opening Date: 15th November 2025
   - Features: Rooftop seating, specialty lattes, live music on weekends
   - Contact: +91 22 1234 5678

-------------- Menu Updates -------------------------------------------------------------------------------------------------------------------

☕ Coffee Menu:
   - Nitro Cold Brew now available in all branches!
   - Seasonal Pumpkin Spice Latte returns this November 🍂
🥐 Pastry Menu:
   - New croissant flavors: Chocolate Almond & Blueberry Cheesecake
   - Artisan Muffins: Banana Walnut & Lemon Poppy Seed
   

------------- Promotions & Offers -------------------------------------------------------------------------------------------------------------

🎁 Holiday Special: Buy 2 coffees, get 1 free – valid until 31st Dec 2025
👫 Referral Bonus: Invite a friend, get 15% off your next order


--------------- Events & Workshops ------------------------------------------------------------------------------------------------------------

🎨 Latte Art Workshop – New York, USA
   - Date: 10th December 2025
   - Register online: www.asdcafe.com/workshops
🎶 Live Jazz Night – Paris, France
   - Every Friday from 7 PM – 10 PM

-----------------Staff Announcements ----------------------------------------------------------------------------------------------------------

🏆 Congratulations to the new Employee of the Month across all branches!
🎉 Welcome our new baristas joining Tokyo & Dubai branches

-------------------------------------------------------------------------------------------------------------------------------------------------

=============================================================================================================================================================
""")
        elif ch==4:
            view()

        elif ch==5:
            break
                    

#-------------------------------------------------- MAIN CALLING FUNCTIONS ----------------------------------------------------------

def main():
    while True:
        print(r"""

                   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                 ⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⢻⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠙⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠘⢿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡆⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠃⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠃⠀⠀⠀⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⣀⣀⣀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⠀⣀⡤⠤⠒⠒⠋⠉⠉⠻⣧⠀⠀⠀⠈⠉⠁⠀⠀⠀⠢⢄⠀⠀⠀⠀⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⣾⣿⠀⠀⠀⠀⣀⣀⣀⣀⣤⣽⣦⣄⣀⣀⣀⣀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⣿⣿⣿⠷⠾⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠶⠚⠀⠀⠀⠀⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⢿⣿⡏⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⣸⠛⠻⣷⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⠸⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠀⢠⣿⠇⠀⠀
                                                                    ⠀⠀⠀⠀⠀⠀⠀⣹⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣎⣠⣴⠿⠃⠀⠀⠀
                                                                    ⠀⢀⣠⠔⠒⠈⠉⠀⠹⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠛⠛⠉⠒⠢⣄⠀⠀
                                                                    ⠀⣿⡁⠀⠀⠀⠀⠀⠀⠈⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⡃⠀⠀⠀⠀⠀⠀⠀⡟⠀
                                                                    ⠀⠙⠻⣶⣀⠀⠀⠀⠀⠀⠀⠈⠙⠲⠦⣤⣄⣀⣀⣀⣤⣤⣾⣯⡵⠞⠋⠀⠀⠀⣀⠟⠀⠀⠀⠀
                                                                    ⠀⠀⠀⠀⠉⠛⠻⠿⠿⠶⠶⠤⠤⠤⣄⣀⣀⣀⣀⣀⣀⣀⣀⡠⠤⠤⠤⠴⠖⠉⠀⠀⠀⠀⠀⠀


                                          .o.        .oooooo..o oooooooooo.          .oooooo.         .o.       oooooooooooo oooooooooooo 
                                         .888.      d8P'    `Y8 `888'   `Y8b        d8P'  `Y8b       .888.      `888'     `8 `888'     `8 
                                        .8"888.     Y88bo.       888      888      888              .8"888.      888          888         
                                       .8' `888.     `"Y8888o.   888      888      888             .8' `888.     888oooo8     888oooo8    
                                      .88ooo8888.        `"Y88b  888      888      888            .88ooo8888.    888    "     888    "    
                                     .8'     `888.  oo     .d8P  888     d88'      `88b    ooo   .8'     `888.   888          888       o 
                                    o88o     o8888o 8""88888P'  o888bood8P'         `Y8bood8P'  o88o     o8888o o888o        o888ooooood8 
                                                                                                                                          

                                                                                                                                     
                                          ,---.            ,--.  ,--.                      ,--.  ,--.           ,---.  ,--.                  
                                         /  O  \ ,--.,--.,-'  '-.|  ,---.  ,---. ,--,--, ,-'  '-.`--' ,---.    '   .-' `--' ,---.  ,---.     
                                        |  .-.  ||  ||  |'-.  .-'|  .-.  || .-. :|      \'-.  .-',--.| .--'    `.  `-. ,--.| .-. |(  .-'     
                                        |  | |  |'  ''  '  |  |  |  | |  |\   --.|  ||  |  |  |  |  |\ `--.    .-'    ||  || '-' '.-'  `)    
                                        `--' `--' `----'   `--'  `--' `--' `----'`--''--'  `--'  `--' `---'    `-----' `--'|  |-' `----'     
                                                                                                                           `--'                                                                                                                                            
                                                            ,------.         ,--.,--.       ,--.       ,--.   
                                                            |  .-.  \  ,---. |  |`--' ,---. |  ,---. ,-'  '-. 
                                                            |  |  \  :| .-. :|  |,--.| .-. ||  .-.  |'-.  .-' 
                                                            |  '--'  /\   --.|  ||  |' '-' '|  | |  |  |  |   
                                                            `-------'  `----'`--'`--'.`-  / `--' `--'  `--'   
                                                                                     `---'
                                                                                     
                                                Authentic taste. Delightful moments. Welcome to Authentic Sips Delight !

                                                                             << HOME PAGE >>

                                                                                1.OWNER
                                                                                2.EMPLOYEE
                                                                                3.CUSTOMER
                                                                                4.SUPPLIER
                                                                                5.ABOUT US
                                                                                6.EXIT
                                                                                
""")
        
        ch=int(input("                                                                             CHOOSE YOUR OPTION :"))
        
        if ch==1:
            owner()
        elif ch==2:
            emp()
        elif ch==3:
            customer()
        elif ch==4:
            supplier()
        elif ch==5:
            aboutus()
        elif ch==6:
            return
        else:
            print("Incorrect option.Try again")
            

def owner():

    while True:
        print("""
[ OWNER ]

1.MENU
2.EMPLOYEE LIST 
3.STOCKS 
4.REVIEWS
5.EXIT """)

        cho=int(input("\nSelect Option :"))

        if cho==1:
            owner_menu()
        elif cho==2:
            owneremp()
        elif cho==3:
            admin_stock()
        elif cho==4:
            view()
        elif cho==5:
            break
       
main()
       
            
