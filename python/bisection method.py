y=float(input("Enter the number : "))
z=y
x=0
ans=0
while abs(ans**2 - abs(y)) > 0.0001 and ans <= x:
    ans=(x+y)/2.0
    if ans**2 < z:
        x=ans
    else:
        y=ans
print("The square root of ",z," is ",ans)