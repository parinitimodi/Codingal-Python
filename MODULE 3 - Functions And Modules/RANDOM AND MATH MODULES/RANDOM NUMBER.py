import random
num = int(input("Enter A Number: "))
num2 = (random.randint(0,11))

print("The number entered by you is ",num,"and the number entered by the computer is ",num2,".")

if(num == num2):
    print("Hence, the numbers are matching!!")

else: 
    print(" Hence, the numbers are not matching")