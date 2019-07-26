'''simple interest''''


principle=int(input("enter the principle amount:"))
roi=int(input("enter the rate of interest:"))
time=float(input("enter the time:"))
simpleinterest=(principle*time*roi)/100
print(f"simple interest:{simpleinterest}")