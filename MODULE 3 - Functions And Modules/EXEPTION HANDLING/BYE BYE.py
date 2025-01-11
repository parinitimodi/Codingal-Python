
try:
    value = int(input("enter a number/value: "))
    print(value)



    if(value%2 == 0):
        while value>0:
            print("BYE!!")
        
    else:
        print("Okay we wont run it forever")
    


except Exception as ex:
    print("exception is ",ex)
    

    

