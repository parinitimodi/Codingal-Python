def factorial(n):
    if (n == 0 or n == 1):
        return 1
    
    else:
        return n * factorial (n-1)
    
num = int(input("ENTER USER INPUT: "))

if num<0:
    print("FACTORIALS DONT EXIST FOR NEGATIVE NUMBERS")

else:
    print(f"The factorial of {num} is {factorial (num)}")

