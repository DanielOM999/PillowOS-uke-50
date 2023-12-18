from PIL import Image, ImageDraw, ImageFilter
import os

# Load your image
image_path = os.path.join(os.path.dirname(__file__), "images")
new_folder = os.path.join(image_path, "Framed_Images")
frame_path = os.path.join(os.path.dirname(__file__), "usinfiles")
os.makedirs(new_folder, exist_ok=True)
im_path = os.path.join(image_path, "black.jpg")
im = Image.open(im_path)
frame = Image.open(os.path.join(frame_path, "frame.png"))
paper = Image.open(os.path.join(frame_path, "oldpaper.jpg"))
fn, fenx = os.path.splitext("black.jpg")
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
new_image.save("output.jpg")
