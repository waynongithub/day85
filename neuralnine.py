# https://www.youtube.com/watch?v=ibf5cx221hk
# NeuralNine: Tkinter Beginner Course - Python GUI Developmen

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close without confirm", command=exit)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close", command=self.on_close)
        self.menubar.add_cascade(menu=self.filemenu, label='File')

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show message", command=self.show_message)
        self.menubar.add_cascade(menu=self.actionmenu, label='Action')

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="yoiur message", font=("Arial", 16))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=4, font=("Courier", 12))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Show msgbox", font=("Arial", 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="show message", font=("Arial", 16), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.btn_open_file = tk.Button(self.root, text="btn_open_file", font=("Arial", 16), command=self.open_file)
        self.btn_open_file.pack(padx=10, pady=10)

        self.clearbutton = tk.Button(self.root, text="Clear", font=("Arial", 14), command=self.clear_message)
        self.clearbutton.pack(padx=10, pady=10)

        self.canvas = tk.Canvas(width=200, height=224)
        # tomato_img = tk.PhotoImage(file="tomato.png")
        # canvas.create_image(100, 112, image=tomato_img)
        # # timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=("arial", 15, "bold"))
        # canvas.pack()


        self.root.protocol("WM_DELETE_WINDOW", self.on_close)


        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="message: ", message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        print(f"event.keysym={event.keysym}") # Return
        print(f"event.state={event.state}")  # 4
        if event.keysym == 'Return' and event.state == 4:
            self.show_message()

    def on_close(self):
        # if messagebox.askyesno(title="quit?", message="really want to quit?"):
        self.root.destroy()

    def clear_message(self):
        self.textbox.delete('1.0', tk.END)

    def open_file(self):
        filetypes = (
            ('img files', '.jpg .jpeg .png'),
            ('All files', '*.*')
        )

        filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir='/media/datax/coding/images',
            filetypes=filetypes)

        messagebox.showinfo(
            title='Selected File',
            message=filename
        )

        # tomato_img = tk.PhotoImage(file="tomato.png")
        tomato_img = tk.PhotoImage(file=filename)
        print(tomato_img)
        self.canvas.create_image(100, 112, image=tomato_img)
        # timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=("arial", 15, "bold"))
        self.canvas.pack()

MyGUI()