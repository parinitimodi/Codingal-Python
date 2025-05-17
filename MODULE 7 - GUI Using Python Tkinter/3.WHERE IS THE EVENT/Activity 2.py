from tkinter import*
from tkinter import messagebox
root = Tk()
root.title("Buttons")
root.geometry("400x400")
def msg():
    messagebox.showwarning("ALERT!!", "STOP, VIRUS FOUND!!")
button = Button(root, text = "Scan For VIRUS", command = msg)
button.place(x = 50, y = 90)
root.mainloop()