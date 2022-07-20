import mysql.connector

db=mysql.connector.connect( host = "localhost" , user = "root" , password = "1234", database="swapnildb")
print("connection sucessfully eshtablish ")
mycu=db.cursor()

def data_fetch_admin():
    db = mysql.connector.connect(host="localhost", user="root", password="1234", database="swapnildb")
    mycu = db.cursor()
    mycu.execute("select* from admindb")#select the table
    for admin_name in mycu:#admindb table row select and each row can be print
        return admin_name[2]



def data_fetch_user():
    db = mysql.connector.connect(host="localhost", user="root", password="1234", database="swapnildb")
    mycu = db.cursor()
    mycu.execute("select* from userdb")#select the table
    for userdb_name in mycu:#admindb table row select and each row can be print
        return userdb_name[2]


def AdminMenuWindow():
    print("=========================================AdminMenu===============================================================")
    print("1.Display Product", "    " ,"2.Add Product", "    ", "3.Remove Product", "    " ,"4.Products goods available", "   " , "5.AdminChangePassword", "    " ,"6.Logout"   )
    print("==================================================================================================================")

def AdminProductMenuWindow():
        mycu.execute("select * from productlist")
        print("========================Product List================================")
        print("Product_Id\t\t\tProduct_Name\t\t\tProduct_Price\t\t\tProduct_Available")
        print("==================================================================")
        for d in mycu:
            p, q, r, s = d
            print(p, "\t\t\t\t\t\t\t\t", q, "\t\t\t\t\t\t\t\t", r, "\t\t\t\t\t\t", s)
        print("==================================================================")


def AdminProductAdd_inTable_lastRecord():
    mycu.execute("select * from productlist")
    print("====================Last Record In Stoke=============================")
    print("Product_Id\t\t\tProduct_Name\t\t\tProduct_Price\t\t\tProduct_Available")
    print("==================================================================")
    l = []
    for d in mycu:
        l.append(d)
    p, q, r, s = l[-1]
    print(p, "\t\t\t\t\t\t\t\t", q, "\t\t\t\t\t\t\t\t", r, "\t\t\t\t\t\t", s)
    print("==================================================================")

def AdminProduct_AddinTable():
    n = int(input("Enter the no.of.items need to be added : "))
    for i in range(n):
        product_id = input("enter product_id: ")
        product_name = input("Enter product_Name: ")
        product_prise = int(input("Enter product_ Price : "))
        product_available = int(input("Enter product_Available : "))
        query = (
            "INSERT INTO `swapnildb`.`productlist` (`product_id`, `product_name`, `product_prise`, `product_available`) VALUES ('{0}', '{1}', '{2}', '{3}'); ".format(
                product_id, product_name, product_prise, product_available))
        mycu.execute(query)
        db.commit()
        print("successful insert")

def RemoveProducts():
    pro_id=int(input("enter Product_id"))
    mycu.execute("delete from productlist where product_id={};".format(pro_id))
    db.commit()
    print("your product_id={} item delete from stock".format(pro_id))


def AdminProductAvailableInStock():
    mycu.execute("select * from productlist")
    print("============Available  In Stoke==============")
    print("Product_Name\t\t\tProduct_Available")
    print("===========================================")
    total=0
    count=0
    for d in mycu:
        p, q, r, s=d
        print(q, "\t\t\t\t\t\t\t\t", s,)
        total+=s
        count+=1
    print("===========================================")
    print("count=",count, "\t\t\t\t\t\t","Total=", total)
    print("===========================================")


def AdminChangePassword():
    old_pass = input("Enter old password=")
    mycu.execute("select * from admindb")
    for i in mycu:
        id, username, p = i
    if (old_pass == p):
        new_pass = input("Enter new password")
        mycu.execute(
            "UPDATE `swapnildb`.`admindb` SET `admin_password` = '{}' WHERE (`user_id` = '1');".format(new_pass))
        db.commit()
        print("your password change successfully")
    else:
        print("you enter wrong password")




# when admin login sucessful  you come to that point
def AdminOptions():
        choice = int(input("Please enter user choice : "))
        if choice == 1:
            AdminProductMenuWindow()
            # print("\n===================================================\n")
            AdminMenuWindow()
            # print("\n===================================================\n")
            AdminOptions()
        elif choice == 2:
            AdminProductAdd_inTable_lastRecord()
            AdminProduct_AddinTable()
            AdminProductMenuWindow()
            AdminMenuWindow()
            AdminOptions()
        elif choice == 3:
            AdminProductMenuWindow()
            RemoveProducts()
            AdminMenuWindow()
            AdminOptions()
        elif choice == 4:
            AdminProductAvailableInStock()
            AdminMenuWindow()
            AdminOptions()
        elif choice == 5:
            AdminChangePassword()
            login()
            AdminOptions()
        elif choice  == 6:
            yes = input("You are sure to logout admin login(y/n) ")
            if yes =='y' or yes == 'Y':
                login()
            else:
                AdminMenuWindow()
                AdminOptions()
        else:
            print("\nInvalid Choice. Please enter valid choice")
            AdminOptions()
#===========================================================================================================================
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#===========================================================================================================================
def UserMenuWindow():
    print("=========================================User Menu===============================================================")
    print("1.Display Product")
    print("2.Add Product in Cart")
    print("3.Remove Product from Cart")
    print("4.Bill for Cart item")
    print("5.UserChangePassword")
    print("6.Logout" )
    print("==================================================================================================================")

bucket=[]
def AddProductInCart():

def UserOptions():
    user_choice = int(input("Please enter user choice : "))
    if user_choice == 1:
        AdminProductMenuWindow()
        UserMenuWindow()
        UserOptions()
    elif user_choice == 2:
        pass
    else:
        print("\nInvalid Choice. Please enter valid choice")




""" main login flow"""
#heading of project
print('=========================================================================================================\n')

print("""🍇  🎀 🍇  🎀🍇  🎀🍇  🎀🍇  🎀🍇  🎀🍇  🎀🍇  🎀 𝒟_𝓂𝒶𝓇𝓉 𝑀𝒶𝓃𝒶𝑔𝑒𝓂𝑒𝓃𝓉 𝒮𝓎𝓈𝓉𝑒𝓂  🎀  🍇🍇  🎀🍇  🎀🍇  🎀🍇  🎀🍇  🎀🍇  🎀🍇  🎀🍇  🎀\n""")

print('==========================================================================================================')
while True:
    def login():
            # time.sleep(2)
            print('==========================================================================================================')
            print ("\b                              **********`•.,¸¸,.•´¯   🎀  𝒮𝐸𝐿𝐸𝒞𝒯 𝒰𝒮𝐸𝑅 𝒯𝒴𝒫𝐸𝒮  🎀   ¯´•.,¸¸,.•`************                  \n")
            print("                                     *(𝟙) 𝔸𝕕𝕞𝕚𝕟 𝕃𝕠𝕘𝕚𝕟         [𝔽𝕠𝕣 𝕤𝕖𝕝𝕖𝕔𝕥 𝔸𝕕𝕞𝕚𝕟 𝕡𝕣𝕖𝕤𝕤 𝕒/𝔸\n")
            print("                                     *(𝟚) 𝕌𝕤𝕖𝕣 𝕃𝕠𝕘𝕚𝕟            [𝔽𝕠𝕣 𝕤𝕖𝕝𝕖𝕔𝕥 𝕌𝕤𝕖𝕣 𝕡𝕣𝕖𝕤𝕤 𝕦/𝕌]\n")
            print("                                     *(𝟛) 𝔼𝕩𝕚𝕥                       [𝕋𝕪𝕡𝕖 𝔼 𝕥𝕠 𝕖𝕩𝕚𝕥 𝕥𝕙𝕖 𝔻𝕞𝕒𝕣𝕥 𝕒𝕡𝕡𝕝𝕚𝕔𝕒𝕥𝕚𝕠𝕟]\n")
            print('==========================================================================================================')
            # time.sleep(2)
            tp = input("\n Choice Login Type  =")
            # checking of admin login
            if tp == 'a' or tp=='A' :
                admin_username = input("Admin_Username ")
                admin_password = input("Admin_password : ")
                apwd=data_fetch_admin()
                if admin_password == apwd:
                    print("you are successfully  Admin login")
                    print("*****************************************************************welcome to Admin Account**************************************************************")
                    AdminMenuWindow()
                    AdminOptions()
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
                    print("************************************************************* welcome to User Account********************************************************************")
                    UserMenuWindow()
                    UserOptions()
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