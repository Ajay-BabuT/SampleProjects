try:
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    c=a/b
    print("Result is",c)
    d=[10,20,30,40,50]
    i=int(input("Enter index (upto 4): "))
    print(d[i])
except ZeroDivisionError:
    print("Division by zero not possible")
except OverflowError:
    print("Value out of range")
except ValueError:
    print("Please enter integer value")
except IndexError:
    print(i," is out of range")
except RuntimeError:
    print("Something else went wrong")
finally:
    print("Bye...")
