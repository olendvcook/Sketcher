from scrapers.redditscraper import connect, get_images
from scrapers.imagescraper import grab_rdm_img
from imggui import ImgGui
from ctrlgui import CtrlGui
import praw
import PIL
import time

if __name__ == '__main__':
    print("World Hello")

    # Initialize reddit connection
    reddit = connect()

    # pull a subreddit
    # Note: possible to do a multireddit
    sub = reddit.subreddit('supermodelcats')

    # pull "limit" number of posts and then get the image urls
    img_urls = get_images(sub, 100)

    #initialize gui
    img_gui = ImgGui()

    ctrl = CtrlGui(img_urls, img_gui)

    while (img_gui.running and ctrl.running):
        # We can get exception if we close window before calling the next few lines

        """
        img = grab_rdm_img(img_urls)

        img_gui.display_img(img)

        time.sleep(5)
        """
