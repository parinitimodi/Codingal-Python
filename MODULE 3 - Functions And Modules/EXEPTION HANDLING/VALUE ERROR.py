try:
    num = int(input("Enter a number"))
    print(num)
except ValueError as ex:
    print("Exception : ",ex)

print("I am outside the Try Block.")
