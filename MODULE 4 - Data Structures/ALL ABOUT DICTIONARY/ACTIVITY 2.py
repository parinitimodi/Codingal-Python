testdic = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print("The Original Dictionary is:",str(testdic))
k = 5
res = 0
for key in testdic:
    if testdic[key] ==k:
        res = res + 1
print(f"The frequency of {k} is:{res}")






