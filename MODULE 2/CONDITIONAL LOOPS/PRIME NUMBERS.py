lower = int(input("ENTER A LOWER RANGE "))
upper = int(input("ENTER A UPPER RANGE "))

print("PRIME NUMBERS BETWEEN", lower , " AND", upper ,"IS/ARE:")

for num in range(lower, upper + 1):
    if num>1:
        for i in range(2,num):
            if (num%i) == 0:
                break
        else:
            print(num)
          
