import tkinter as tk
# from PIL import Image, ImageTk
from PIL import Image, ImageTk
# from pillow import Image, ImageTk
from tkinter import filedialog, messagebox


class Mygui():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("codemy tutorials")

        # to place an application icon
        # https://www.reddit.com/r/Tkinter/comments/zpwwm1/tkintertclerror_bitmap_myownico_not_defined/
        # doesnt work => maybe because of Spidey!!!
        self.im = Image.open('images/nutrition.png')
        self.photo = ImageTk.PhotoImage(self.im)
        self.root.wm_iconphoto(True, self.photo)

        self.root.geometry("800x600")

        self.btn_exit = tk.Button(self.root, text="close", command=self.close)
        self.btn_exit.pack()


        # show an image
        orig_img = Image.open('/media/datax/coding/images/stella-small.png')
        orig_photo = ImageTk.PhotoImage(orig_img)
        img_w = orig_photo.width()
        img_h = orig_photo.height()
        ratio = img_w/img_h
        width = 500
        height = width / ratio
        self.print_dimensions([img_w, img_h, ratio, width, height])
        img_resized = orig_img.resize((int(width), int(height)))
        self.photo = ImageTk.PhotoImage(img_resized)

        self.imglabel = tk.Label(image=self.photo)
        self.imglabel.pack()


        tk.mainloop()

    def close(self):
        self.root.destroy()

    def print_dimensions(self, img):
        print(img)

    def resize_image(self):
        pass

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


Mygui()