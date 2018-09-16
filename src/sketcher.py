from scrapers.redditscraper import connect, get_images
from scrapers.imagescraper import grab_rdm_img
from gui import Gui
import praw
import PIL
import time

if __name__ == '__main__':
    print("World Hello")

    # Initialize reddit connection
    reddit = connect()

    # pull a subreddit
    # Note: possible to od a multireddit
    sub = reddit.subreddit('supermodelcats')

    # pull "limit" number of posts and then get the image urls
    img_urls = get_images(sub, 100)

    #initialize gui
    gui = Gui()

    while (gui.running):
        # We can get exception if we close window before calling the next few lines


        img = grab_rdm_img(img_urls)

        gui.display_img(img)

        time.sleep(5)
