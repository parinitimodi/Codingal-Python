string = input("ENTER A STRING ")
char = input("ENTER A CHARACTER ")

i = 0
count = 0

while (i<len(string)):
    if(string[i] == char):
        count = count + 1
    i = i +1

print("TOTAL NUMBER OF TIMES",char,"HAS APPEARED IN",string,"IS",count)

