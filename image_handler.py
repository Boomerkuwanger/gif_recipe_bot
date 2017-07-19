import os
import requests
import pytesseract
from PIL import Image


def get_text_from_image(image_file):
    return pytesseract.image_to_string(Image.open(image_file))

def extract_frames(in_gif='current_recipe.gif', out_folder='images'):
    frame = Image.open(in_gif)
    nframes = 0
    while frame:
        frame.save( '%s/%s-%06d.png' % (out_folder, os.path.basename(in_gif), int(nframes)))
        nframes += 1
        try:
            frame.seek( nframes )
        except EOFError:
            break;
    return True

def download_gif(uri):
    response = requests.get(uri)
    if response.status_code == 200:
        with open('current_recipe.gif', 'wb') as f:
            for chunk in response.iter_content(4096):
                f.write(chunk)
