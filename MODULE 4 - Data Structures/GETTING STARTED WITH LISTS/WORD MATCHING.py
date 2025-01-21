
def list2 (numberofcharacters):
    a = 0
    b = []
    for i in numberofcharacters:
        if len(i)>1 and i[0]== i[-1]:
            a = (a+1)
            b.append(i)
    print ("List of words with the First and the Last chearacter SAME is",b,".")
    return (a)
list = list2(["mom","dad","y","lolipop","football", "dance","j"])
print("The number of words having the First and the Last character SAME is",list,".")

