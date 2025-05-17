from tkinter import*

root = Tk()
root.title("Buttons")
root.geometry("400x400")

def handlekeypress(event):
    print(event.char)

root.bind("<Key>",handlekeypress)

def handleclick(event):
    print("\n Button was clicked!!")

button = Button(text = "CLICK ME!!")

button.pack()


button.bind("<Button>",handleclick)

root.mainloop()