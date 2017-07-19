import os
import praw
import time
from image_handler import download_gif, extractFrames, get_text_from_image

reddit = praw.Reddit('gif_recipes_bot')

# Good test urls
# http://i.imgur.com/f52csda.gif pasta

def main(reddit=reddit):
    gif_recipes_subreddit = reddit.subreddit('gifrecipes')
    for submission in gif_recipes_subreddit.hot(limit=10):
        if submission.url[-4:] == 'gifv':
            download_gif(submission.url[0:-1])  # download the .gif not .gifv
            extractFrames()
            for f in os.listdir('images'):
                print('-' * 20, f, '-' * 20)
                if f != '.placeholder':
                    print(get_text_from_image('images/{}'.format(f)))
            return  # return after one for now

if __name__ == '__main__':
    main()
