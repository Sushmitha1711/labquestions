'''sum of digits'''

'''n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)''''


''''single digit sum'''
tnum=num=int(input("enter a number:"))
sum=0
while num>9:
    sum=(num%10+num//10)
    num=sum

print(f"sum of digits of {tnum} is:{num}")