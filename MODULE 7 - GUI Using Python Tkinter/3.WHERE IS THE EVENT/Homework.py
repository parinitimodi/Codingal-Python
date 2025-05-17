import tkinter as tk
from tkinter import messagebox

def converttocm():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        resultlabel.config(text=f"{inches} inches = {cm:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("300x150")

tk.Label(root, text="Enter length in inches:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

convertbutton = tk.Button(root, text="Convert", command=converttocm)
convertbutton.pack(pady=5)

resultlabel = tk.Label(root, text="")
resultlabel.pack(pady=5)

root.mainloop()