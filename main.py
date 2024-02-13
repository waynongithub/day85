# from tkinter import Tk
import tkinter as tk
from tkinter import filedialog





root = tk.Tk()

root.title("watermarker")
root.geometry("800x600")

# first argument is the parent = root
label = tk.Label(root, text="choose image file", font=("Arial", 16))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=("Arial", 12))
textbox.pack(padx=10, pady=10)

entry = tk.Entry(root, font=("Courier", 12))
entry.pack(padx=10, pady=10)

button = tk.Button(root, text="push it", font=("Courier", 12))
button.pack(padx=10, pady=10)

# img = tk.Image(root)
# dlg = tk.filedialog

# with grid
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="btn1", font=("Arial", 14))
btn2 = tk.Button(buttonframe, text="btn2", font=("Arial", 14))
btn3 = tk.Button(buttonframe, text="btn3", font=("Arial", 14))
btn4 = tk.Button(buttonframe, text="btn4", font=("Arial", 14))
btn5 = tk.Button(buttonframe, text="btn5", font=("Arial", 14))
btn6 = tk.Button(buttonframe, text="btn6", font=("Arial", 14))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill="x")

btnClose = tk.Button(root, text="Close", font=("Arial", 15))
btnClose.place(x=400, y=400, width=100, height=20)

root.mainloop()
