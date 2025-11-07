a=[]
n=int(input("Enter the limit : "))
print("Enter the numbers : ")
for i in range(1,n+1):
    num=int(input())
    a.append(num)
print("The largest number is :",max(a))