def biggest(num1,num2,num3):
    if num1>num2 and num1>num3:
        max=num1
    elif num2>num3:
        max=num2
    else:
        max=num3
    return max

num1=int(input("enter the numberr1:"))
num2=int(input("enter the numberr2:"))
num3=int(input("enter the numberr3:"))
print(biggest(num1,num2,num3))