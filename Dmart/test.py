import mysql.connector
bucket=[]
db=mysql.connector.connect( host = "localhost" , user = "root" , password = "1234", database="swapnildb")
print("connection sucessfully eshtablish ")
mycu=db.cursor()


def AdminProductMenuWindow():
    mycu.execute("select * from productlist")
    print("========================Product List================================")
    print("Product_Id\t\t\tProduct_Name\t\t\tProduct_Price\t\t\tProduct_Available")
    print("==================================================================")
    for d in mycu:
        p, q, r, s = d
        print(p, "\t\t\t\t\t\t\t\t", q, "\t\t\t\t\t\t\t\t", r, "\t\t\t\t\t\t", s)
    print("==================================================================")

def UserMenuWindow():
    print("=========================================User Menu===============================================================")
    print("1.Display Product")
    print("2.Add Product in Cart")
    print("3.Remove Product from Cart")
    print("4.Bill for Cart item")
    print("5.UserChangePassword")
    print("6.Logout" )
    print("==================================================================================================================")



def cart_item_remove():
    total_bill=0
    remove=str(input("enter product name"))
    print("------------------------------------------------------------------------------------------------------------")
    print("Sr.No\t\t\tProduct_Name\t\t\tProduct_Price\t\t\tProduct_Quantity\t\t\tTotal")
    print("------------------------------------------------------------------------------------------------------------")
    sr=1
    for k in bucket:
        a,b,c,d= k.values()
        if remove == a:
            k.items()
            continue
        print(sr,"\t\t\t\t\t\t\t\t",a,"\t\t\t\t\t\t\t",b, "\t\t\t\t\t\t\t\t",c,"\t\t\t\t\t\t\t\t",d)
        sr=sr+1
    print("------------------------------------------------------------------------------------------------------------")
    for j in bucket:
        a, b, c, d = j.values()
        if remove == a:
            j.items()
            continue
        total_bill = d + total_bill
    print("Total bill", "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", total_bill)
    print("------------------------------------------------------------------------------------------------------------------")




def cart_item_show():
    total_bill=0
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
                    print ("you enter quantity is not avilable")
                    pass
                    AdminProductMenuWindow()
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

AdminProductMenuWindow()
AddProductInCart()
cart_item_show()
cart_item_remove()
