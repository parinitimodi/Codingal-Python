from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Demo Project")
root.configure(bg="Light Blue")
root.geometry("600x500")

title1 = Label(root,
               text="💖 DENOMINATION 💖",
               bg="Light Blue",
               fg="#ff69b4",
               font=("Arial Rounded MT Bold", 24, "bold"))
title1.place(relx=0.5, rely=0.08, anchor=CENTER)

title2 = Label(root,
               text="✨ CALCULATION ✨",
               bg="Light Blue",
               fg="#1e90ff",
               font=("Arial Rounded MT Bold", 24, "bold"))
title2.place(relx=0.5, rely=0.18, anchor=CENTER)

label1 = Label(root,
               text="Hii, Welcome To Denomination Calculation Application!!!! :D",
               bg="Light Blue",
               font=("Arial", 10, "bold"),
               fg="grey")
label1.place(relx=0.5, rely=0.75, anchor=CENTER)

def msg():
    MsgBox = messagebox.askquestion("ALERT!!", "Do you want to calculate your denomination?")
    if MsgBox == "yes":
        topwin()

button1 = Button(root, text="Let's Get Started!!", command=msg, bg="white", fg="black")
button1.place(relx=0.5, rely=0.85, anchor=CENTER)

def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg="Light Blue")
    top.geometry("600x350+50+50")

    label = Label(top, text="Enter The Total Amount", bg="Light Blue", font=("Arial", 12, "bold"))
    label.place(x=50, y=30)

    entry = Entry(top)
    entry.place(x=250, y=30)

    lbl = Label(top, text="Here are the number of notes for the denomination calculation of your input",
                bg="light grey", font=("Arial", 10, "bold"), wraplength=500)
    lbl.place(x=50, y=70)

    l1 = Label(top, text="2000", bg="light grey", font=("Arial", 10, "bold"))
    l1.place(x=100, y=120)
    l2 = Label(top, text="500", bg="light grey", font=("Arial", 10, "bold"))
    l2.place(x=100, y=160)
    l3 = Label(top, text="100", bg="light grey", font=("Arial", 10, "bold"))
    l3.place(x=100, y=200)

    t1 = Entry(top)
    t1.place(x=200, y=120)
    t2 = Entry(top)
    t2.place(x=200, y=160)
    t3 = Entry(top)
    t3.place(x=200, y=200)

    def calculator():
        try:
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("ERROR!!", "Please Enter A Valid Number...")

    btn = Button(top, text="CALCULATE", command=calculator, bg="brown", fg="white")
    btn.place(x=250, y=250)

root.mainloop()
