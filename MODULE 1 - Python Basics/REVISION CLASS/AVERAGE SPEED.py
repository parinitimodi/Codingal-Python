cyclistA = 10
cyclistB = int(input("ENTER USER INPUT"))
cyclistC = 30

sum = cyclistA + cyclistB + cyclistC

average = sum/3
print (average)

if cyclistA>average:
    print("The speed of cyclistA is greater than average")
elif cyclistB>average:
    print("The speed of cyclistB is greater than average")
else:
    print("The speed of cyclistC is greater than average")
