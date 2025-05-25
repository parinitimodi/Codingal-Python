from tkinter import*
from tkinter import messagebox
root = Tk()
root.title("Password Strength Checker")
root.configure(bg = "#62f55d")
root.geometry("400x300")
def checkstrength():
    password = passwordentry.get()
    length = len(password)
    
    if length == 0:
        resultlabel.config(text="Please enter a password", foreground="black")
    elif length < 6:
        resultlabel.config(text="Strength: Weak", foreground="red")
    elif 6 <= length <= 10:
        resultlabel.config(text="Strength: Medium", foreground="orange")
    else:
        resultlabel.config(text="Strength: Strong", foreground="green")



titlelabel = Label(root, text="Enter Your Password", font=("Helvetica", 14), bg="light green")
titlelabel.pack(pady=10)

passwordentry = Entry(root, show="*", width=30)
passwordentry.pack(pady=5)

checkbutton = Button(root, text="Check Strength", command=checkstrength)
checkbutton.pack(pady=10)

resultlabel = Label(root, text="", font=("Helvetica", 12), bg="light green")
resultlabel.pack(pady=10)

root.mainloop()