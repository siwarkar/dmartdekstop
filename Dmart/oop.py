import time
dmt = [{'id' : 1,'Name':'sugar','price':40},{'id' : 2,'Name':'tea','price':500},
        {'id' : 3,'Name':'liril','price':70},
        {'id' : 4,'Name':'rin','price':10},{'id' : 5,'Name':'vim','price':10},
        {'id' : 6,'Name':'rin poder','price':180},{'id' : 7,'Name':'saffola gold','price':1300},
        {'id' : 8,'Name':'rice','price':58},
        {'id' : 9,'Name':'wheat','price':30},{'id' : 10,'Name':'almond','price':900},
        {'id' : 11,'Name':'kaju','price':1200},{'id' : 12,'Name':'suace','price':120}]

udmt = dmt
trolly = []
def Menulist():
    print('----------------------------------Menu List----------------------------------------------')
    print('1.AddProduct,\n2.buy \n3.exist')
    print('--------------------------------------------------------------------------------------')

def Display_product():
    print("product_id", "\t\t\t","ProductName","\t\t\t","product_price" )
    for i in dmt:
        p, q, r = i.values()
        print(p, "\t\t\t\t\t\t\t", q, "\t\t\t\t\t\t\t", r)

def Display_update_product():
    print("product_id", "\t\t\t","ProductName","\t\t\t","product_price'\t\t\t", "Total" )
    for i in trolly:
        p, q, r,s = i.values()
        print(p, "\t\t\t\t\t\t\t", q, "\t\t\t\t\t\t\t", r,"\t\t\t\t",s)


def BuyProduct_IN_trunk():
    total=0
    n=int(input("choice="))
    if n ==1:
        cho = int(input("enter the product_Id"))
        for c in dmt:
            if c["id"] == cho:
                 q=int(input("enter quantity youwant="))
                 total = q * c["price"]
                 c.update({"total":total})
                 trolly.append(c)
                 print(trolly)

nm = input('enter your name:')
# time.sleep(1)
print('------------------------------------')
print('Welcome to Dmart',nm)
print('-------------------------------------')
# time.sleep(2)
print('what you want to buy')
print('-------------------------------------')
while True:
    def login():
        Display_product()
        Menulist()
        BuyProduct_IN_trunk()
        Display_update_product()


    login()



