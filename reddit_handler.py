import os
import praw
import time
from image_handler import download_gif, extract_frames, get_text_from_image


reddit = praw.Reddit('gif_recipes_bot')

# Good test urls
# http://i.imgur.com/f52csda.gif pasta

def main(reddit=reddit):
    gif_recipes_subreddit = reddit.subreddit('gifrecipes')
    try:
        for submission in gif_recipes_subreddit.top(limit=10):
            if submission.url[-4:] == 'gifv':
                download_gif(submission.url[0:-1])  # download the .gif not .gifv
                extract_frames()
                for f in os.listdir('images'):
                    if f != '.placeholder':
                        print('-' * 20, f, '-' * 20)
                        print(get_text_from_image(os.path.join('images', f)))
                break  # return after one for now
    finally:
        try:
            os.remove('current_recipe.gif')
        except FileNotFoundError:
            pass
        [os.remove(os.path.join('images', f)) for f in os.listdir('images') if f.endswith('.png')]

if __name__ == '__main__':
    main()
