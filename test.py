women = {
    "name": "sanne",
    "attributes": [
        "tetten", "foef", "clit", "schaamlippen", "neukhol", "stronthol"
    ]
}

if __name__ == '__main__':

values = ahmed
ali = "ali"
print(ali)

kut = 'kut'
print(kut)


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
    # d.text((x, y), text, fill=(255, 255, 255, transparency), font=font)
    d.text((x, y), text, fill=fillcolor, font=font)
    # Combining Original Image with Text
    self.watermarked_image = image.alpha_composite(img, txt)
    watermarked_thumbnail = self.resize_image(self.watermarked_image)
    self.display_image(watermarked_thumbnail)


