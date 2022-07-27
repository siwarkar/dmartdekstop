import mysql.connector


db=mysql.connector.connect( host = "localhost" , user = "root" , password = "1234", database="swapnildb")
print("connection sucessfully eshtablish ")
mycu=db.cursor()


def data_fetch_admin():
    print("Admin ->connection sucessfully eshtablish ")
    mycu.execute("select* from admindb")#select the table
    for admin_name in mycu:#admindb table row select and each row can be print
        return admin_name[2]
data_fetch_admin()


def data_fetch_user():
    print("User ->connection sucessfully eshtablish")
    mycu.execute("select* from userdb")#select the table
    for userdb_name in mycu:#admindb table row select and each row can be print
        return userdb_name[2]
data_fetch_user()


def adminLoginWindow():
    print("=====================")
    print("1.Display Menu")
    print("2.Add Product")
    print("3.Remove Product")
    print("4.Products goods available")
    print("5.Total Income")
    print("6.Logout")
    print("=====================")

def adminDisplayMenuWindow():
    mycu.execute("select * from productlist")
    print("==================================================================")
    print("Product_Id\t\t\tProduct_Name\t\t\tProduct_Price\t\t\tProduct_Available")
    print("==================================================================")
    for d in mycu:
        p, q, r, s = d
        print(p, "\t\t\t\t\t\t\t\t", q, "\t\t\t\t\t\t\t\t", r, "\t\t\t\t\t\t", s)
    print("==================================================================")


def adminOptions():
        choice = int(input("Please enter user choice : "))
        if choice == 1:
            adminDisplayMenuWindow()
            print("\n===================================================\n")
            adminLoginWindow()
            print("\n===================================================\n")
            adminOptions()
        else:
            print("\nInvalid Choice. Please enter valid choice")
            print("\n===================================================\n")
            adminLoginWindow()
            print("\n===================================================\n")
adminOptions()



#design of dmart
print('==========================================================')
    # time.sleep(2)
print("*****************D_mart Management System*********************")
    # time.sleep(2)
print('==========================================================')

while True:
    def login():
            # time.sleep(2)
            print ("\b     SELECT USER TYPES")
            # time.sleep(2)
            tp = input("*(1) Admin Login\t[For select Admin press a/A]:"
                         "\n*(2) User Login\t [For select User press u/U]:"
                         "\n*(3) Exit\t[Type E to exit the Dmart application]\n Choice Login Type  =")
            # checking of admin login
            if tp == 'a' or tp=='A' :
                admin_username=input("Admin_Username ")
                admin_password = input("Admin_password : ")
                apwd=data_fetch_admin()
                if admin_password == apwd:
                    print("you are successfully  Admin login")
                    adminLoginWindow()
                    adminOptions()

                else:
                    print("you are not login please re-enter admin_user and password ")
                    print("=====================================================================")
                #cheking of user login
            elif tp == 'u' or tp =='U':
                user_name=input("User_Username")
                user_password = input(" User_password : ")
                upwd = data_fetch_user()
                if (user_password == upwd):
                    print("you are successfully User login")
                    print("=====================================================================")
                    adminLoginWindow()
                    adminOptions()
                else:
                    print("you are not login please User_name and password ")
                    print("=====================================================================")
             #exit option  coding
            elif tp== 'e' or tp  == 'E':
                print('Thank you for shopping with us ')
                print('Visit again...!!!!!')
                exit(code=exit())
            else:
                print("Invalid user type. Enter valid choice type")
                print("=====================================================================")

    login()