from tkinter import*
root = Tk()
root.title("Demo Project")
root.geometry("400x300")

nums = [[9,8,7], [6,5,4], [3,2,1], ["#",0,"*"]]

for i in range(4):
    root.columnconfigure(i,weight = 1,minsize = 75)
    root.rowconfigure(i,weight = 1,minsize = 50)
for i in range (4):
    for j in range (3):
        frame = Frame(master = root,
                      relief = RAISED,
                      borderwidth = 4,
                      bg = "#a4fcb0" )
        frame.grid(row = i,column = j,sticky = "nsew")
        lbl = Label(master = frame,text = nums[i][j], bg ="#9deefa",font = ("Harlow Solid Italic",20))
        lbl.pack(expand = True,fill = "both",padx = 5,pady = 5)
root.mainloop()