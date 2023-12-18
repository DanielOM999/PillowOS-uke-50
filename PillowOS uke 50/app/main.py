from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageTk, ImageDraw, ImageFilter
import pilgram, os
from customtkinter import *
import tkinter as tk

imFolder = os.path.join(os.path.dirname(__file__), "images")
imList = [file for file in os.listdir(imFolder) if file.endswith(".jpg")]
mode = "Instagram"
curIm = imList[0]

def action():
    global curIm
    if mode == "Instagram":
        new_folder = os.path.join(imFolder, "Instagram_Pictures")
        os.makedirs(new_folder, exist_ok=True)
        im_path = os.path.join(imFolder, curIm)
        im = Image.open(im_path)
        fn, fenx = os.path.splitext(curIm)
        pilgram._1977(im).save(os.path.join(new_folder, f"{fn}_Instagram{fenx}"))
        print("Yay!")
    elif mode == "Black and White":
        new_folder = os.path.join(imFolder, "Black_and_White")
        os.makedirs(new_folder, exist_ok=True)
        im_path = os.path.join(imFolder, curIm)
        im = Image.open(im_path)
        fn, fenx = os.path.splitext(curIm)
        pilgram.moon(im).save(os.path.join(new_folder, f"{fn}_black_and_white{fenx}"))
        print("Woah!")
    elif mode == "Rotate":
        value = e1.get()
        if value and value.isnumeric():
            value = float(value)
            print(value)
            new_folder = os.path.join(imFolder, "Rotated_Images")
            os.makedirs(new_folder, exist_ok=True)
            im_path = os.path.join(imFolder, curIm)
            im = Image.open(im_path)
            fn, fenx = os.path.splitext(curIm)
            im.rotate(value).save(os.path.join(new_folder, f"{fn}_rotated{fenx}"))
            print("Woah!")
        else:
            print("No value entered..")
    elif mode == "Resize with to 1080px":
        new_folder = os.path.join(imFolder, "Resized_images")
        os.makedirs(new_folder, exist_ok=True)
        im_path = os.path.join(imFolder, curIm)
        im = Image.open(im_path)
        fn, fenx = os.path.splitext(curIm)
        if im.width < 1080:
            add = 1080 - im.width
            im.resize((im.width + add, im.height + add)).save(os.path.join(new_folder, f"{fn}_1080{fenx}"))
        else:
            print("The image width is larger than 1080px")
    elif mode == "Add Frame":
        new_folder = os.path.join(imFolder, "Framed_Images")
        frame_path = os.path.join(os.path.dirname(__file__), "usinfiles")
        os.makedirs(new_folder, exist_ok=True)
        im_path = os.path.join(imFolder, curIm)
        im = Image.open(im_path)
        frame = Image.open(os.path.join(frame_path, "frame.png"))
        paper = Image.open(os.path.join(frame_path, "oldpaper.jpg"))
        fn, fenx = os.path.splitext(curIm)
        if im.width > im.height:
            crop = im.width - im.height
            crop = crop / 2
            im = im.crop((crop, 0, im.width - crop, im.height))
        im = im.resize((764, 764))
        new_image = Image.new('RGB', (frame.width, frame.height))
        center_x = (new_image.width - im.width) // 2 + 3
        center_y = (new_image.height - im.height) // 5 + 2
        new_image.paste(im, (center_x, center_y))
        new_image.paste(frame, (0, 0), mask=frame)
        new_image.convert("RGB")
        new_image = pilgram.brannan(new_image)
        pilgram.css.blending.color(new_image, paper).save(os.path.join(new_folder, f"{fn}_framed{fenx}"))
        

        # draw = ImageDraw.Draw(im)
        # draw.rectangle((0, 0, im.width, im.height), outline=(220, 220, 220), width=20)
        # x = 0
        # height_fraction = 0.25
        # height = int(height_fraction * im.height)
        # y = im.height - height
        # draw.rectangle([x, y, x + im.width, y + height], fill=(220, 220, 220))
    elif mode == "Overlook":
        new_folder = os.path.join(imFolder, "Overlooked_Images")
        os.makedirs(new_folder, exist_ok=True)
        im_path = os.path.join(imFolder, curIm)
        im = Image.open(im_path)
        fn, fenx = os.path.splitext(curIm)
        output = Image.new("RGB", im.size)
        coefficients = [1, 0.2, 0, 0, 2, 0, 0, 0.002]
        output = im.transform(im.size, Image.PERSPECTIVE, coefficients, Image.BICUBIC)
        output = output.filter(ImageFilter.DETAIL).filter(ImageFilter.SMOOTH).filter(ImageFilter.SHARPEN)
        output.save(os.path.join(new_folder, f"{fn}_overlook{fenx}"))

def combobox_callback(choice):
    global curIm
    curIm = choice
    print("combobox dropdown clicked:", choice)

def set_mode(choice):
    global mode
    mode = choice
    if mode == "Black and White":
        e1.place_forget()
    elif mode == "Instagram":
        e1.place_forget()
    elif mode == "Rotate":
        e1.place(relx=0.7, rely=0.45, anchor="center")
    elif mode == "Resize with to 1080px":
        e1.place_forget()
    elif mode == "Add Frame":
        e1.place_forget()
    elif mode == "Overlook":
        e1.place_forget()
    print(f"Mode set to: {mode}")

def open_directory():
    global imFolder, imList
    directory_path = filedialog.askdirectory()

    if directory_path:
        print(f"Selected Directory: {directory_path}")
        imFolder = directory_path
        imList = [file for file in os.listdir(imFolder) if file.endswith(".jpg")]
        comB1.configure(values=imList)

wn = CTk()
wnwith = 800
wnheight = 600
wn.geometry(f"{wnwith}x{wnheight}")
wn.title("ImageCO")
set_appearance_mode("dark")
set_default_color_theme("blue")
wn.resizable(False, False)

bt1 = CTkButton(wn, text="Open File Dialog", command=open_directory)
bt1.place(relx=0.5, rely=0.35, anchor="center")

bt2 = CTkButton(wn, text="Start!", command=action)
bt2.place(relx=0.5, rely=0.5, anchor="center")

comB1 = CTkComboBox(master=wn, values=imList, command=combobox_callback)
comB1.place(relx=0.5, rely=0.4, anchor="center")
comB1.set(imList[0])

comB2 = CTkComboBox(master=wn, values=["Instagram", "Black and White", "Rotate", "Resize with to 1080px", "Add Frame", "Overlook"], command=set_mode)
comB2.place(relx=0.5, rely=0.45, anchor="center")
comB2.set(mode)

e1 = CTkEntry(master=wn, placeholder_text="CTkEntry", width=120, height=25, border_width=2, corner_radius=10)
e1.place_forget()

wn.mainloop()