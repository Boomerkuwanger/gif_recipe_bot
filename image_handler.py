import os
import requests
import pytesseract
from PIL import Image


def get_text_from_image(image_file):
    image = Image.open(image_file)
    return pytesseract.image_to_string(image)

def extract_frames(in_gif='current_recipe.gif', out_folder='images'):
    frame = Image.open(in_gif)
    nframes = 0
    while frame:
        save_file = os.path.join(
            out_folder,
            "{}-{:06d}.png".format(os.path.basename(in_gif), int(nframes))
        )
        frame.save(save_file)
        nframes += 1
        try:
            frame.seek( nframes )
        except EOFError:
            break;
    return True

def download_gif(uri, out_file='current_recipe.gif'):
    response = requests.get(uri)
    if response.status_code == 200:
        with open(out_file, 'wb') as f:
            for chunk in response.iter_content(4096):
                f.write(chunk)
