def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
limit = int(input("Enter the limit: "))
print("Fibonacci sequence:")
for i in range(limit):
    print(fibo(i))