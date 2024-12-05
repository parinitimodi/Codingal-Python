
unit = int(input("ENTER:"))
if (unit<50):
    print("PER UNIT COST IS 2.6 AND TAX = 25")
    amount = unit*2.6 + 25
    print (amount)
elif (unit>50 and unit<100):
    print("PER UNIT COST = 3.25 AND TAX = 35 ")
    amount = unit*3.25 + 35
    print(amount)
elif (unit>100 and unit<200):
    print("PER UNIT COST = 5.26, AND TAX = 45 ")
    amount = unit*5.26 + 45
    print(amount)
else:
    print("the cost of the unit is 8.45, and the tax is 75.")
    amount = unit*8.45 + 75
    print(amount)







