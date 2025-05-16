from tkinter import*
import datetime

root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

frame = Frame(master = root, height = 200, width = 360, bg = "#fa87ec")

lbl1 = Label(frame, text = "Name", bg = "#f705db", fg = "white", width = 12)
lbl2 = Label(frame, text = "Year", bg = "#f705db", fg = "white", width = 12)
lbl3 = Label(frame, text = "Month", bg = "#f705db", fg = "white", width = 12)
lbl4 = Label(frame, text = "Date", bg = "#f705db", fg = "white", width = 12)

nameentry = Entry(frame)
yearentry = Entry(frame)
monthentry = Entry(frame)
dateentry = Entry(frame)

def calculate():
    name = nameentry.get()
    year = int(yearentry.get())
    today = datetime.date.today()
    age = today.year +-+ year
    greet = "Hey "+name
    message = " \nYour age is: "+str(age)
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(bg = "#f5bae2", fg = "black")

btn = Button(text = "Calculate Age", command = calculate, bg = "#fa05ab")

frame.place(x = 20, y = 0)
lbl1.place(x = 20, y = 20)
nameentry.place(x = 150, y = 20)
lbl2.place(x = 20, y = 50)
yearentry.place(x = 150, y = 50)
lbl3.place(x = 20, y = 80)
monthentry.place(x = 150, y = 80)
lbl4.place(x = 20, y = 110)
dateentry.place(x = 150, y = 110)
btn.place(x = 140, y = 210)
textbox.place(y = 250)
root.mainloop()
