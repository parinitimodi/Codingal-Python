import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(entryprincipal.get())
        rate = float(entryrate.get())
        time = float(entrytime.get())

        simple_interest = (principal * rate * time) / 100
        compoundamount = principal * ((1 + rate / 100) ** time)
        compoundinterest = compoundamount - principal

        labelresult.config(
            text=f"Simple Interest: ₹{simple_interest:.2f}\nCompound Interest: ₹{compoundinterest:.2f}"
        )
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numeric values.")

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("300x300")

tk.Label(root, text="Principal (₹):").pack(pady=5)
entryprincipal = tk.Entry(root)
entryprincipal.pack()

tk.Label(root, text="Rate of Interest (%):").pack(pady=5)
entryrate = tk.Entry(root)
entryrate.pack()

tk.Label(root, text="Time Period (years):").pack(pady=5)
entrytime = tk.Entry(root)
entrytime.pack()

tk.Button(root, text="Calculate", command=calculate_interest).pack(pady=10)

labelresult = tk.Label(root, text="", fg="blue")
labelresult.pack(pady=10)

root.mainloop()