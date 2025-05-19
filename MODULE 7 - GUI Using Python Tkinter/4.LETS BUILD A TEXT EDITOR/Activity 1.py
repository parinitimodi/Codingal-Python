from tkinter import*
from tkinter.filedialog import askopenfilename, asksaveasfilename 
root = Tk()
root.title("Demo Project")
root.geometry("400x300")
root.rowconfigure(0, minsize = 800, weight = 1)
root.columnconfigure(1, minsize = 800, weight = 1)
def openfile():
    filepath = askopenfilename(filetypes = [("Text Files","*.*"),("All Files","*.*")])
    if not filepath:
        return
    texteditor.delete(1.0,END)
    with open(filepath,"r") as inputfile:
       txt = inputfile.read() 
       texteditor.insert(END,txt) 
       inputfile.close()

    root.title(f"Condingal's Text Editor - {filepath}")
def savefile():
    filepath = asksaveasfilename(defaultextension= "txt",filetypes = [("Text Files","*.*"),("All Files","*.*")])
    if not filepath:
        return
    with open(filepath,"w") as outputfile:
        txt = texteditor.get(1,0,END)
        outputfile.write(txt)
    root.title(f"Condingal's Text Editor - {filepath}")
texteditor = Text(root)
frbuttons = Frame(root, relief = RAISED, bd = 2)
btnopen = Button(frbuttons, text = "Open", command = openfile)
btnsave = Button(frbuttons, text = "Save as...", command = savefile)
btnopen.grid(row = 0, column = 0, sticky = "ew", padx = 5, pady = 5)
btnsave.grid(row = 1, column = 0, sticky = "ew", padx = 5)
frbuttons.grid(row = 0,column = 0, sticky = "ns")
texteditor.grid(row = 0,column = 0, sticky = "nsew")
root.mainloop()