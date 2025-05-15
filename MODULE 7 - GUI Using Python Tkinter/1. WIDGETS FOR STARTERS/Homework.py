import tkinter as tk
from tkinter import ttk

def calculate_product():
    try:
        num1 = float(entrynum1.get())
        num2 = float(entrynum2.get())
        result = num1 * num2
        labelresult.config(text=f"The product is: {result}")
    except ValueError:
        labelresult.config(text="Invalid input. Please enter numbers.")

# Create the main window
root = tk.Tk()
root.title("Number Product Calculator")

# Create widgets
labelnum1 = ttk.Label(root, text="Enter the first number:")
labelnum1.grid(row=0, column=0, padx=10, pady=5)

entrynum1 = ttk.Entry(root)
entrynum1.grid(row=0, column=1, padx=10, pady=5)

labelnum2 = ttk.Label(root, text="Enter the second number:")
labelnum2.grid(row=1, column=0, padx=10, pady=5)

entrynum2 = ttk.Entry(root)
entrynum2.grid(row=1, column=1, padx=10, pady=5)

buttoncalculate = ttk.Button(root, text="Calculate", command=calculate_product)
buttoncalculate.grid(row=2, column=1, padx=10, pady=10)

labelresult = ttk.Label(root, text="")
labelresult.grid(row=3, column=1, padx=10, pady=5)

# Run the application
root.mainloop()