try:
    age = input("ENTER A NUMBER: ")


    print ("AGE = ",age)

    if (age>0 and age<=100):
        print ("The age entered is correct")
    else:
        print("!There is some mistake in the age entered as this age is not valid!")

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
