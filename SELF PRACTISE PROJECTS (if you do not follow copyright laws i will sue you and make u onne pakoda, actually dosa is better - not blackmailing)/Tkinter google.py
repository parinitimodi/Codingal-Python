import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Simple Tkinter App")

# Create a label widget
label = tk.Label(window, text="Hello, World!")
label.pack(pady=20)  # Add padding for better appearance

# Run the Tkinter event loop
window.mainloop()
