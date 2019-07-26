LB=int(input("enter the lb value:"))
UB=int(input("enter the ub value:"))
res=" ".join([str(i) for i in range(LB,UB+1) if i%9==0 and i%5!=0])
print(res)