import time

import mysql.connector

db=mysql.connector.connect( host = "localhost" , user = "root" , password = "1234", database="swapnildb")
print("connection sucessfully eshtablish ")
mycu=db.cursor()


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
        mycu.execute("UPDATE `swapnildb`.`admindb` SET `admin_password` = '{}' WHERE (`user_id` = '1');".format(new_pass))
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
    print("4.Cart In Product list")
    print("5.Bill for Cart item")
    print("6.UserChangePassword")
    print("7.Logout" )
    print("==================================================================================================================")


def cart_item_remove():
        if len(bucket) == 0:
             print("bucket is empty  first add product in cart then remove")
             UserMenuWindow()
             UserOptions()
        else:
            total_bill=0
            rem=str(input("enter product name"))
            print("------------------------------------------------------------------------------------------------------------")
            print("Sr.No\t\t\tProduct_Name\t\t\tProduct_Price\t\t\tProduct_Quantity\t\t\tTotal")
            print("------------------------------------------------------------------------------------------------------------")
            sr=1
            for k in bucket:
                a,b,c,d= k.values()
                if rem == a:
                    for x in range(len(bucket)):
                        if bucket[x]['Product_Name'] == a:
                            del bucket[x]
                            break
                else:
                    continue
                print(sr,"\t\t\t\t\t\t\t\t",a,"\t\t\t\t\t\t\t",b, "\t\t\t\t\t\t\t\t",c,"\t\t\t\t\t\t\t\t",d)
            print("------------------------------------------------------------------------------------------------------------")
            print("you delete product succesfully")
        print("-----------------------------------------------final  list-------------------------------------------------------")
        print("Sr.No\t\t\tProduct_Name\t\t\tProduct_Price\t\t\tProduct_Quantity\t\t\tTotal")
        print("------------------------------------------------------------------------------------------------------------")
        sr = 1
        total_bill = 0
        for t in bucket:
            p, q, r, s = t.values()
            total_bill = s + total_bill
            print(sr, "\t\t\t\t\t\t\t\t", p, "\t\t\t\t\t\t\t", q, "\t\t\t\t\t\t\t\t", r, "\t\t\t\t\t\t\t\t", s)
            sr=sr+1
        print("==============================================================================")
        print("Total bill", "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", total_bill)
        print("------------------------------------------------------------------------------------------------------------------")


def cart_item_show():
    if len(bucket) == 0:
        print("bucket is empty  first add product in cart ")
        UserMenuWindow()
        UserOptions()
    else:
            total_bill=0
            print("-----------------------------------------------------------------------------------------------------------")
            print("Sr.No\t\t\tProduct_Name\t\t\tProduct_Price\t\t\tProduct_Quantity\t\t\tTotal")
            print("-----------------------------------------------------------------------------------------------------------")
            sr = 1
            for i in bucket:
                a ,b,c,d = i.values()
                print(sr,"\t\t\t\t\t\t\t",a,"\t\t\t\t\t\t",b,"\t\t\t\t\t\t",c,"\t\t\t\t\t\t\t\t", d)
                sr=sr+1
            print("------------------------------------------------------------------------------------------------------------")
            for j in bucket:
                a,b,c,d = j.values()
                total_bill= d + total_bill
            print("Total bill","\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", total_bill)
            print("-------------------------------------------------------------------------------------------------------------")




bucket=[]
def AddProductInCart():
        mycu.execute("select * from productlist")
        sr = 1
        total=0
        sel = int(input("enter product_id ="))
        for l in mycu:
            if sel == l[0]:
                quan = int(input("enterthe quantity="))
                if quan <= l[3]:
                    print("Quantity available")
                else:
                    print ("you enter quantity is not avilable only avilable is ={}".format(l[3]))
                    break
                print("Product_Id\t\t\tProduct_Name\t\t\tProduct_Price\t\t\tProduct_Quantity\t\t\tTotal")
                total = l[2] * quan
                print( l[0],"\t\t\t\t\t\t\t", l[1] , "\t\t\t\t\t\t\t\t\t\t", l[2], "\t\t\t\t\t\t\t\t", quan, "\t\t\t\t\t\t\t", total)
                bucket.append({"Product_Name":l[1],"Product_Price":l[2],"Product_Quantity":quan,"Total":total})
                print("==================================================================")
                print("you add product to cart")
        moreadd = input("if  you want more product[Y/N] ")
        if moreadd == 'y' or moreadd == 'Y':
            AddProductInCart()
        elif moreadd == 'n' or moreadd == "N":
            UserMenuWindow()
        else:
            print("you enter wrong choice")


def Bill_final():
    cart_item_show()
    choice = input("Do you want buy any thing else[ y/ n ]")
    if choice == 'y' or choice =='Y':
        UserMenuWindow()
        UserOptions()
    elif choice =='n' or choice == 'N':
        cart_item_show()
        for i in bucket:
            a, b, c, d = i.values()
            mycu.execute("select * from productlist")
            for j in mycu:
                p,q,r,s=j
                if a == q:
                    update=s-c
                    mycu.execute("UPDATE `swapnildb`.`productlist` SET `product_available` = '{}' WHERE (`product_name` = '{}');".format(update,a))
                    db.commit()
                    break
        print("Thanks for Pay Successfully")
        bucket.clear()
        UserMenuWindow()
        UserOptions()
        login()
    else:
        print("you enter wrong choice plz enter correct choice ")




def UserChangePassword():
    old_pass = input("Enter old password=")
    mycu.execute("select * from userdb")
    for i in mycu:
        id, username, p = i
    if (old_pass == p):
        new_pass = input("Enter new password")
        mycu.execute("UPDATE `swapnildb`.`userdb` SET `usedb_password` = '{}' WHERE `userdb_name` = '{}';".format(new_pass , username))
        print("your password change successfully")
    else:
        print("you enter wrong password")





def UserOptions():
    user_choice = int(input("Please enter user choice : "))
    if user_choice == 1:
        AdminProductMenuWindow()
        UserMenuWindow()
        UserOptions()
    elif user_choice == 2:
        AdminProductMenuWindow()
        AddProductInCart()
        UserOptions()
    elif user_choice== 3:
        cart_item_show()
        cart_item_remove()
        UserOptions()
    elif user_choice  ==4:
        cart_item_show()
        UserMenuWindow()
        UserOptions()
    elif user_choice == 5:
        Bill_final()
        UserOptions()
    elif user_choice  ==6:
        UserChangePassword()
        login()
        UserOptions()
    elif user_choice  == 7:
            yes = input("You are sure to logout User login(y/n) ")
            if yes =='y' or yes == 'Y':
                login()
            else:
                UserMenuWindow()
                UserOptions()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        UserOptions()



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
                mycu.execute("SELECT * FROM swapnildb.admindb;")
                admin_username = input("Admin_Username ")
                admin_password = input("Admin_password : ")
                for i in mycu:
                    id,aname,apwd= i
                    if admin_password == apwd and admin_username ==aname:
                        print("you are successfully  Admin login")
                        print ("\b                                                 **********`•.,¸¸,.•´¯   🎀  welcome {}  🎀   ¯´•.,¸¸,.•`************                  \n\n".format(admin_username))
                        AdminMenuWindow()
                        AdminOptions()
                    else:
                        print("you are not login please re-enter admin_user and password ")
                        print("=====================================================================")
                #cheking of user login
            elif tp == 'u' or tp =='U':
                mycu.execute("SELECT * FROM swapnildb.userdb;")
                user_name = input("User_Username :")
                user_password = input(" User_password : ")
                for i in mycu:
                    id,uname,upwd = i
                    if (user_password == upwd) and (user_name == uname):
                        print("you are successfully User login")
                        print("\b                                                 **********`•.,¸¸,.•´¯   🎀  welcome {}  🎀   ¯´•.,¸¸,.•`************                  \n\n".format(user_name))
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