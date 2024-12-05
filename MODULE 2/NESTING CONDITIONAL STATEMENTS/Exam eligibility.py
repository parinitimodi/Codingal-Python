
medical_cause = input("DID YOU HAVE A MEDICAL REPORT Yes or No:")

if (medical_cause == "Yes"):
    print ("YOU ARE ALLOWED!!")
else:
    attendence = int(input("ENTER ATTENDENCE"))

    if attendence>=75:
        print("YOU ARE ALLOWED!!")
    else:
        print("YOU ARE NOT ALLOWED :I")
        