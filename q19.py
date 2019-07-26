products={}
while True:
    print("1.add product 2.view all 3.search by id 4.exit")
    ch=int(input("enter the choice:"))
    if ch==1:
        pid=input("enter the product id:")
        pname=input("enter the product name:")
        products[pid]=pname
    elif ch==2:
        if len(products)==0:
            pass
        
