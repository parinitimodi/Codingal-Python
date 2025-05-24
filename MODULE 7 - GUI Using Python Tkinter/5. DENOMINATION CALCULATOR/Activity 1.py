from tkinter import*
root = Tk()
root.title("Demo Project")
root.geometry("400x300")
def toplevel():
    top = Toplevel()
    top.title("Toplevel")
    l2 = Label(top, text = "This is a Toplevel Window...")
    l2.pack()
    top.mainloop()

l = Label(root,text = "This is a Root Window...")
btn = Button(root, text = "Click to open", command = toplevel)
l.pack()
btn.pack()
root.mainloop()