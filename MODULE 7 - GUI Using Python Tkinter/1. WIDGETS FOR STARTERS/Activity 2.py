from tkinter import*
from datetime import date
root = Tk()
root.title("Demo Project")
root.geometry("400x300")
lbl = Label(text = "Hey There!!",fg = "white", bg ="#072F5F",height = 1,width = 300)
namelbl = Label(text = "Full Name",bg = "#3895B3")
nameentry = Entry()
def display():
    name = nameentry.get()
    global message
    message = "Welcome To The Application!!""\n""Today's Date Is: "
    greet = "Hello" +name+ "\n"
    textbox.insert(END,greet) 
    textbox.insert(END,message)
    textbox.insert(END,date.today())
textbox = Text()

btn = Button(text = "Begin",command = display, height = 1, bg = "#1261A0",fg = "white")

lbl.pack()
namelbl.pack()
nameentry.pack()
btn.pack()
textbox.pack()
root.mainloop()