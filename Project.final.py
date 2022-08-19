                                                                                          #BANK MANAGEMENT SYSTEM

from prettytable import PrettyTable
import mysql.connector

mydatabase=mysql.connector.connect(host="localhost",user="root",password="135413")

mycursor=mydatabase.cursor()

mycursor.execute("create database if not exists BMS")
mycursor.execute("use BMS")
mycursor.execute("create table if not exists signup(username varchar(30),password varchar(30))")



def signup():
    username=input("USERNAME:")
    password=input("PASSWORD:")
    mycursor.execute("insert into signup values('''+username+''','''+password+''')")
    mydatabase.commit()
    print("\t\t\t****************************+++SIGNUP SUCESSFULLY+++****************************")
    print("Now Please Login to continue")
    login()


def login():
    username=input("USERNAME:")
    password=input("PASSWORD:")

    mycursor=mydatabase.cursor()
    mycursor.execute(" select username from signup ")
    user1=mycursor.fetchall()
    mydatabase.commit()
    user2=[]
    for i in range(len(user1)):
        user2.append(user1[i][0])

    mycursor=mydatabase.cursor()
    mycursor.execute(" select password from signup ")
    pwd1=mycursor.fetchall()
    pwd2=[]
    for i in range(len(pwd1)):
        pwd2.append(pwd1[i][0])
    mydatabase.commit()

    if(username not in user2) or (password not in pwd2):
        print("Wrong Username or Password! Try Again")
        f=1
        while True:
            f=int(input("Press 1 for trying again \nPress 2 for exit:"))
            if f==1:
                login()
            else:
                 exit()

    else:
        mycursor=mydatabase.cursor()
        mycursor.execute("select username from signup from where username="+username+"")
        user=mycursor.fetchone()
        mycursor.execute("select password from signup from where password="+password+"")
        pwd=mycursor.fetchone()
        print("\t\t\t****************************+++LOGIN SUCESSFULLY+++****************************")
        mydatabase.commit()
        while True:
            print(' Press I for open new account')
            print(' Press 2 for deposite amount')
            print(' Press 3 for withdraw amount')
            print(' Press 4 for balance enquiry')
            print(' Press 5 for customer details')
            print(' Press 6 for information updation')
            print(' Press 7 for close account')
            print(' Press 8 for to show data/information')
            print(' Press any key for EXIT')
            a=int(input('Enter your Value:'))

            if a==1:
                openacc()

            elif(a==2):
                dep()

            elif(a==3):
                withdraw()


            elif(a==4):
                bal_enq()

                

            elif(a==5):
                cust_det()
                 
            elif(a==6):
                 update()
                 
            elif(a==7):
                close()
                
            elif(a==8):
                show()
                
            else:
                  
                  print('\t\t\t\tTHANK YOU')
                  break
                

def openacc():
    name=input('Enter full name of owner:')
    acc_no=int(input('enter account number:'))
    address=input('enter permanent address of owner:')
    contact_no=int(input('enter contact number of owner:'))
    total_balance=int(input('Enter how much balance you want to deposite:'))
    data1=(name,acc_no,address,contact_no,total_balance)
    data2=(name,acc_no,total_balance)
    mycursor.execute("create table if not exists acc(name varchar(30),acc_no int,address varchar(30),contact_no int,total_balance int)")
    mycursor.execute("create table if not exists amount(name varchar(30),acc_no int,total_balance int)")
    sqll='insert into acc values(%s,%s,%s,%s,%s)'
    sq12='insert into amount values(%s,%s,%s)'
    c=mydatabase.cursor()
    mycursor.execute(sqll,datal)
    mycursor.execute(sq12,data2)
    mydatabase.commit()
    print('"')
    print('\t\t\t-----****data entered sucessfully & Account Open****-----')
    print('"')
    print('__________________________________________________________________________________________________________________________')



def dep():
    name=input('enter your name:')
    acc_no=input('enter account number:')
    dep_am=input('enter how much amount you deposite:')
    c=mydatabase.cursor()
    mycursor.execute('update acc set total_balance=total_balance+'+dep_am+ ' where acc_no='+acc_no+';')
    mydatabase.commit()
    mycursor.execute("select total_balance from acc where acc_no="+str(acc_no)) 
    myresult=mycursor.fetchall()
    t=PrettyTable(['total_balance'])
    for total_balance in myresult:
                     t.add_row([total_balance])
    print('\t\t\t-----**** Available Balance After Deposit ****-----')
    print(t)
    print('__________________________________________________________________________________________________________________________')



def withdraw():
    name=input('enter your name:')
    acc_no=input('enter account number:')
    dep_am=input('enter how much amount you withdraw:')
    c=mydatabase.cursor()
    mycursor.execute("update acc set total_balance=total_balance-"+dep_am+' where acc_no='+acc_no+';')
    mydatabase.commit()
    mycursor.execute("select total balance from ace where acc_no="+str(ace_no)) 
    myresult=mycursor.fetchall()
    t=PrettyTable(['total_balance'])
    for total_balance in myresult:
        t.add_row([total_balance])
    print('\t\t\t-----**** Available Balance After Withdraw ****-----')
    print(t)
    print('__________________________________________________________________________________________________________________________')



def bal_enq():
    acc_no=int(input('enter your account number:'))
    c=mydatabase.cursor()
    mycursor.execute('select total_balance from acc where acc_no='+str(acc_no))
    myresult=mycursor.fetchall()
    t=PrettyTable(['total_balance'])
    for total_balance in myresult:
        t.add_row([total_balance])
    print("\t\t\t-----**** Balance Enquiry Successfully Printed ****-----")
    print(t)
    print('__________________________________________________________________________________________________________________________')



def cust_det():
    acc_no=int(input('enter your account number:'))
    c=mydatabase.cursor()
    mycursor.execute("select * from acc where acc_no="+str(acc_no))
    myresult=mycursor.fetchall()
    t=PrettyTable(['name','acc_no', 'address','contact_no','total_balance'])
    for name,acc_no,address,contact_no,total_balance in myresult:
        t.add_row([name,acc_no,address,contact_no,total_balance])
    print('\t\t\t-----**** Customers Details ****-----')
    print(t)
    print('__________________________________________________________________________________________________________________________')



def update():
    acc_no=input('enter account number:')
    new_cont=input('enter new contact number:')
    c=mydatabase.cursor()
    mycursor.execute('update acc set contact_no='+new_cont+' where acc_no='+acc_no+';')
    mydatabase.commit()
    mycursor.execute('select * from acc where acc_no='+str(acc_no))
    myresult=mycursor.fetchall()
    t=PrettyTable(['name','acc_no', 'address', 'contact_no','total_balance'])
    for name,acc_no,address,contact_no,total_balance in myresult:
        t.add_row([name,acc_no,address,contact_no,total_balance])
    print('\t\t\t-----**** Information Updated Successfully ****-----')
    print(t)



def close():
    name=input('enter account holder name:')
    acc_no=int(input('enter account number:'))
    c=mydatabase.cursor()
    mycursor.execute('delete from ace where acc_no='+str(acc_no))
    mydatabase.commit()
    print('\t\t\t-----**** Account Deleted/Closed Succcesfully ****-----')
    print('__________________________________________________________________________________________________________________________')



def show():
    mycursor=mydatabase.cursor()
    mycursor.execute("select * from acc")
    myresult=mycursor.fetchall()
    t=PrettyTable(['name','acc_no', 'address', 'contact_no','total_balance'])
    for name,acc_no,address,contact_no,total_balance in myresult:
        t.add_row([name,acc_no,address,contact_no,total_balance])
    print("\t\t\t-----**** All Information ****-----")
    print(t)
    print('__________________________________________________________________________________________________________________________')



#STARTING POINT

print('\t\t\t|______________________________________________________________________________________|\t\t')
print('\t\t\t|______________________________________________________________________________________|\t\t')
print('\t\t\t|-------------------->>>>>BANK MANAGEMENT SYSTEM<<<<<-----------------------|\t\t')
print('\t\t\t|______________________________________________________________________________________|\t\t')
print('\t\t\t|------------------------>>>>>MADE BY KRISH GAUR<<<<<-------------------------|\t\t')
print('\t\t\t|______________________________________________________________________________________|\t\t')


print("\t1:SIGNUP\n\n\t2:LOGIN")
ch=int(input("\n\n\tSIGNUP / LOGIN(1,2):"))
if ch==1:
    signup()
elif ch==2:
    login()
else:
    print("Wrong Entry")



    

                
        


    
    
