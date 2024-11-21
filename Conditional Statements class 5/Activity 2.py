Costprice = int(input("Enter cost price input:"))
Sellingprice = int(input("Enter selling price input:"))
amount = Sellingprice - Costprice
amount2 = Costprice - Sellingprice
#Enter the prices
if (Costprice>Sellingprice):
 print ("Ram suffered a loss!!")
 print ("Amount of loss is",amount2)
else :
  print ("Ram profited!!")
  print ("Amount of profit is",amount)
