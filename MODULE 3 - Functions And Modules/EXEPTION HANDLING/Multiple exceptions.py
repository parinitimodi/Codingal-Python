try:
    num1 = int(input("ENTER A NUMBER: "))
    num2 = int(input("ENTER A 2nd NUMBER: "))

    result = num1/num2

    print ("Result = ",result)
    print ("Result = ",result1)

except ZeroDivisionError:
    print("Division by 0 is not allowed")

except ValueError:
    print("Please enter a numerical value")

except Exception as ex:
    print("Exception is ",ex)

except:
    print("Some Error Occured")

finally:
    print("I will execute no matter what!!")
