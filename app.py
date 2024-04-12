import streamlit as st
from PIL import Image, ImageDraw, ImageFont

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]  

global ratio

def ascii_art(image, new_width=200):  
    global ratio

    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    image = image.resize((new_width, new_height)) # Resized image

    image = image.convert("L") # Grayscale image

    pixels = image.getdata()
    ascii_img = ""
    i = 0
    for pixel in pixels:
        ascii_img += ASCII_CHARS[pixel//25]
        if ( i == new_width):
            ascii_img += '\n'
            i = 0
        i += 1
    
    # f = open("image.txt", "w")
    # f.write(ascii_img)
    # f.close()

    return ascii_img

def ascii_to_img(ascii_art):
    global ratio
    fontname = "Consolas.ttf"
    fontsize = 5
    text = "example@gmail.com"
    
    colorText = "white"
    colorOutline = "red"
    colorBackground = "black"

    font = ImageFont.truetype(fontname, fontsize)
    img = Image.new('RGB', (1000, int(1000 * ratio)), colorBackground)
    d = ImageDraw.Draw(img)
    d.text((0, 0), ascii_art, fill=colorText, font=font)
    # d.rectangle((0, 0, width+3, height+3), outline=colorOutline)
    
    img.save("image.png")


if __name__ == '__main__':

    st.header("Image to ASCII Art", divider="rainbow")

    img_buffer = st.file_uploader(
        label = "Pick a file",
        type = ['png', 'jpg', 'jpeg'],
        accept_multiple_files = False
        )

    if img_buffer is not None:
        fname = img_buffer.name
        image = Image.open(img_buffer)
        ascii_to_img(ascii_art(image))
        # st.download_button("Download ASCII art", ascii_art(image=image), file_name = f"{fname[0:fname.index('.')]}.txt")

        # st.text(ascii_art(image))