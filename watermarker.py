import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import filedialog, messagebox
from tkinter.colorchooser import askcolor
from pathlib import Path
from tkinter import ttk


class Watermarker():
    # TODO pics folder is hard coded

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("watermarker")
        self.root.bind("<KeyPress>", self.keyboard_shortcuts)
        # to place an application icon
        # https://www.reddit.com/r/Tkinter/comments/zpwwm1/tkintertclerror_bitmap_myownico_not_defined/
        # doesnt work => maybe because of Spidey, but it places an icon on the taskbar
        self.im = Image.open('images/nutrition.png')
        self.photo = ImageTk.PhotoImage(self.im)
        self.root.wm_iconphoto(True, self.photo)

        self.root.geometry("800x600")
        self.root.minsize(width=800, height=600)
        self.root.maxsize(width=800, height=600)

        # NON-CONTROL PROPERTIES =======================
        self.fullname = None
        self.path = None
        self.filename = None

        self.image = None
        self.photo = None
        self.watermarked_image = None

        self.color = (255, 255, 255)

        # menu bar ================
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        # accelerator is for right alignment:
        # https://stackoverflow.com/questions/38034416/align-shortcut-info-to-right-in-tkinter-menu
        self.filemenu.add_command(label="Open image file", command=self.open_file, accelerator="Ctrl+O")
        self.filemenu.add_command(label="Save file", command=self.save_file, accelerator="Ctrl+S", state='disabled')
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close", command=self.close)
        self.menubar.add_cascade(menu=self.filemenu, label='File')

        # self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        # self.actionmenu.add_command(label="Show message", command=self.show_message)
        # self.menubar.add_cascade(menu=self.actionmenu, label='Action')

        self.root.config(menu=self.menubar)

        # FRAMES =====================
        self.main_frame = tk.Frame(master=self.root)
        self.main_frame.pack(side='top', expand=True, padx=10, pady=20, fill=tk.Y)

        self.slider_frame = tk.Frame(master=self.root, highlightbackground="black", highlightthickness=1)
        self.slider_frame.pack(side='top', expand=False, padx=5, pady=5, fill=tk.X)

        self.footer_frame = tk.Frame(self.root)
        self.footer_frame.pack(side='bottom', expand=False, padx=5, fill=tk.X)

        # CONTROLS IN FOOTER FRAME ==================
        self.btn_exit = tk.Button(self.footer_frame, text="close", width=10, command=self.close)
        # self.btn_exit.pack(anchor=tk.E, padx=20, pady=20)
        self.btn_exit.pack(side=tk.RIGHT, padx=10, pady=10)

        self.btn_save_file = tk.Button(self.footer_frame, text="save file",
                                       width=10, state='disabled', command=self.save_file)
        self.btn_save_file.pack(side=tk.RIGHT, padx=6, pady=10)

        # self.btn_add_watermark = tk.Button(self.footer_frame, text="add watermark",
        #                                    width=10, state='disabled', command=self.add_watermark)
        # self.btn_add_watermark.pack(side=tk.RIGHT, padx=6, pady=10)

        self.btn_open_file = tk.Button(self.footer_frame, text="open file", width=10, command=self.open_file)
        self.btn_open_file.pack(side=tk.RIGHT, padx=6, pady=10)

        # CONTROLS IN SLIDER FRAME ====================
        self.btn_color = tk.Button(self.slider_frame, text="pick color", command=self.choose_color)
        self.btn_color.pack(side=tk.RIGHT, padx=10, pady=10)

        self.lbl_spacer1 = tk.Label(self.slider_frame, text="")
        self.lbl_spacer1.pack(side=tk.RIGHT, padx=10)

        self.font_slider_current_value = tk.DoubleVar()
        self.font_slider = tk.Scale(self.slider_frame, from_=80, to=300, orient='horizontal',
                                     variable=self.font_slider_current_value, command=self.font_slider_changed)
        self.font_slider.set(150)
        self.font_slider.pack(side=tk.RIGHT, expand=False, padx=6, pady=10)

        self.lbl_font = tk.Label(self.slider_frame, text='font size:', font=("Arial", 12))
        self.lbl_font.pack(side=tk.RIGHT, padx=0, pady=10)

        self.lbl_spacer2 = tk.Label(self.slider_frame, text="")
        self.lbl_spacer2.pack(side=tk.RIGHT, padx=10)

        self.trans_slider_current_value = tk.DoubleVar()
        self.trans_slider = tk.Scale(self.slider_frame, from_=0, to=255, orient='horizontal',
                                      variable=self.trans_slider_current_value, command=self.trans_slider_changed)
        # set default value: https://stackoverflow.com/questions/3963329/how-can-i-set-the-default-value-of-my-tkinter-scale-widget-slider-to-100
        self.trans_slider.set(50)
        self.trans_slider.pack(side=tk.RIGHT, expand=False, padx=6, pady=10)

        self.lbl_trans = tk.Label(self.slider_frame, text='transparency:', font=("Arial", 12))
        self.lbl_trans.pack(side=tk.RIGHT, padx=0, pady=10)

        self.lbl_spacer3 = tk.Label(self.slider_frame, text="")
        self.lbl_spacer3.pack(side=tk.RIGHT, padx=10)

        text = tk.StringVar()
        text.set('enter watermark text')
        self.edt_text = tk.Entry(self.slider_frame, textvariable=text, width=25, bg='white')
        self.edt_text.bind('<KeyPress>', self.keypress_in_entry)
        self.edt_text.pack(side=tk.RIGHT, padx=10, pady=10)

        self.imglabel = tk.Label(master=self.main_frame)

        tk.mainloop()

    def close(self):
        # if messagebox.askyesno(title="quit?", message="really want to quit?"):
        self.root.destroy()

    def resize_image(self, source_image):
        # https://medium.com/@nutanbhogendrasharma/watermark-image-with-python-506f76e2aaa0
        img_w, img_h = source_image.size
        ratio = img_w / img_h
        if img_w > img_h:
            width = 700
            height = width / ratio
        else:
            height = 440
            width = ratio * height
        print([img_w, img_h, ratio, width, height])
        return source_image.resize((int(width), int(height)))

    def open_file(self):
        # https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/
        filetypes = (
            ('img files', '.jpg .jpeg .png'),
            ('All files', '*.*')
        )

        filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir='/media/datax/coding/images',
            filetypes=filetypes)

        self.fullname = filename
        self.filename = filename.split('/')[-1]
        self.root.title(f"{self.filename}  -  watermarker")
        # Image.open(image_path).convert('RGBA').save(image_path)
        # https://gist.github.com/xiaody/c20dcf9cdf61bd10ccd1  convert-png-to-rgba.py
        self.image = Image.open(filename).convert('RGBA')
        img_resized = self.resize_image(self.image)
        self.display_image(img_resized)
        self.add_watermark()
        self.btn_save_file.config(state='normal')
        self.filemenu.entryconfig("Save file", state='normal')

    def display_image(self, img):
        self.photo = ImageTk.PhotoImage(img)
        self.imglabel.config(image=self.photo)
        self.imglabel.pack(side='top')
        # self.btn_add_watermark.config(state='normal')

    def keyboard_shortcuts(self, event):
        """ctrl-O for open file, ctrl-S for save file"""
        if event.keysym == 'o' and event.state == 4:
            self.open_file()
        if event.keysym == 's' and event.state == 4:
            self.save_file()

    def add_watermark(self):
        try:
            if self.image is None:
                return
        except AttributeError:
            print(f"{AttributeError}")
            return
        # watermark code from https://holypython.com/how-to-watermark-images-w-python-pil/
        if self.edt_text.get() == "":
            messagebox.showinfo(
                title='No watermark',
                message='Enter the text for the watermark in the editbox'
            )
            return
        img = self.image
        txt = Image.new('RGBA', img.size, (255, 255, 255, 0))

        # Creating Text
        font_size = int(self.font_slider_current_value.get())
        text = self.edt_text.get()
        font = ImageFont.truetype("arial.ttf", font_size)

        # Creating Draw Object
        d = ImageDraw.Draw(txt)

        # Positioning Text
        width, height = img.size
        textwidth = d.textlength(text, font)
        textheight = font.size
        x = (width - textwidth) / 2
        y = (height - textheight) / 2

        # Applying Text
        print(f"color={self.color}, type={type(self.color)}")
        transparency = int(self.trans_slider_current_value.get())
        fillcolor = (self.color[0], self.color[1], self.color[2], transparency)
        d.text((x, y), text, fill=fillcolor, font=font)

        # Combining Original Image with Text
        self.watermarked_image = Image.alpha_composite(img, txt)
        watermarked_thumbnail = self.resize_image(self.watermarked_image)
        self.display_image(watermarked_thumbnail)

    def save_file(self):
        # https://pythonguides.com/python-save-an-image-to-file/
        # https://www.geeksforgeeks.org/python-pil-image-save-method/
        # https://www.tutorialspoint.com/save-file-dialog-box-in-tkinter
        print(f"----------------------------in save_file: {self.fullname}")
        pathobj = Path(self.fullname)
        print(f"savefile,pathobj= {pathobj}")
        stem = pathobj.stem
        print(f"stem={stem}")
        newstem = stem + "-watermarked"
        print(f"newstem={newstem}")
        # stella = '/media/datax/coding/images/stellawells-009biebel.png'
        # p = Path(self)
        # newname = p.with_stem(Path(stella).stem + '-final')
        # pathobj.with_stem(newstem)
        newname = pathobj.with_stem(pathobj.stem + '-watermarked')
        # # newname = pathobj.with_stem(newstem)
        # newname = 'dump/kaka.txt'
        print(newname)
        # newbasename = Path(newname.name)
        # print(newbasename)
        newbasename = newname.name
        try:
            filename_to_save = filedialog.asksaveasfile(initialfile=newbasename).name
            if filename_to_save:
                print(f"filename_to_save={filename_to_save}, type={type(filename_to_save)}")
                path = Path(filename_to_save)
                ext = path.suffix
                print(f"ext={ext}")
                if ext != '.png':
                    self.watermarked_image = self.watermarked_image.convert('RGB')
                self.watermarked_image.save(filename_to_save)

        except AttributeError:
            print("save was canceled")

    def trans_slider_changed(self, event):
        print(f"trans_slider_changed, {int(self.trans_slider_current_value.get())}")
        self.add_watermark()

    def font_slider_changed(self, event):
        print(f"font_slider_changed: {int(self.font_slider_current_value.get())}")
        self.add_watermark()

    def choose_color(self):
        color = askcolor()[0]
        print(color)
        self.color = color
        self.add_watermark()

    def keypress_in_entry(self, event):
        print(f"from entry: key was {event.keysym}")
        if self.image is not None:
            self.add_watermark()


Watermarker()
