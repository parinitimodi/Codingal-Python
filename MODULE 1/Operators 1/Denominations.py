Amount = int(input("Please enter the amount:"))
#The notes
Note_1 = Amount//100
Note_2 = (Amount%100)//50
Note_3 = ((Amount%100)%50)//10
#Denominations = 
print("Notes of 100 rupees",Note_1)
print("Notes of 50 rupees",Note_2)
print("Notes of 10 rupees",Note_3)