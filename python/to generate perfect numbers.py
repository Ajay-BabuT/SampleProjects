x=int(input("Enter the limit : "))
print("Perfect Numbers : ")
for num in range(1, x):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        print(num)