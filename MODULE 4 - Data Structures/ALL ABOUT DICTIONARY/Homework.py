x = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print("The Original Dictionary is:",str(x))
k = int(input("CHOOSE A VALUE"))
res = 0
for key in x:
    if x[key] ==k:
        res = res + 1
print(f"The frequency of {k} is:{res}")
