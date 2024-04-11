import streamlit as st
from PIL import Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]  

def ascii_art(image, new_width=100):  
    
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
    
    return ascii_img

if __name__ == '__main__':
    img_buffer = st.file_uploader(
        label = "Pick a file",
        type = ['png', 'jpg', 'jpeg'],
        accept_multiple_files = False
        )

    if img_buffer is not None:
        fname = img_buffer.name
        print(fname)
        image = Image.open(img_buffer)
        ascii_art(image)
        st.download_button("Download ASCII art", ascii_art(image=image), file_name = f"{fname[0:fname.index('.')]}.txt")