list1 = [10,20,30,40]
list2 = [100,200,300,400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)
stocks = ["reliance","sensex","godrejtata"]
prices = [2983,2746,1936]
newdict = {stocks:prices for stocks,
           prices in zip(stocks,prices)}
print((newdict))