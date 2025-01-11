import os
print("Do you want to shut down your system?")
answer = input("yes or no")

if (answer == "yes"):
    os.system("shutdown /s /t 1")

else:
    print("Okay, we wont shutdow your system  ")



