try:
    age = int(input("ENTER A NUMBER: "))


    print ("AGE = ",age)

except ZeroDivisionError:
    print("YOU CANT BE 0 YEARS OLD")

except ValueError:
    print("Please enter a numerical age value")

except Exception as ex:
    print("Exception is ",ex)

except:
    print("Some Error Occured")

finally:
    if (age%2 == 0):
        print("Youre age is even!")

    else:
        print("Youre age is odd!")
