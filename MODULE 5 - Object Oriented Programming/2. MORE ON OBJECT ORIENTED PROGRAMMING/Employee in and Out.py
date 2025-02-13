class Employee:
    def __init__(self):
        print("Employee created.....")
    def __del__(self):
        print("Destruction called.....")
def createobj():
    print ("Making object.....")
    obj = Employee()
    print("Function end.....")
    return obj
print("Callinng createobj() function.....")
createobj()
print("Program End.....")