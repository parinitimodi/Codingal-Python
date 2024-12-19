rows = int(input("ENTER USER INPUT : "))
num = 1

print("FLOYDS TRIANGLE")

for i in range(rows + 1):
    for j in range(i + 1):
        print(num, end = '  ')
        num=num+1
    print()