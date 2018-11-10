from scrapers.redditscraper import connect, get_images
from scrapers.imagescraper import grab_rdm_img
from imggui import ImgGui
from ctrlgui import CtrlGui
import praw
import PIL
import time
import csv

if __name__ == '__main__':
    print("World Hello")

    # Initialize reddit connection
    reddit = connect()

    subs = []
    multisub = ''
    with open ('./resources/subs.txt', 'r') as input:
        csv_reader = csv.reader(input, delimiter=',')
        for row in csv_reader:
            for sub in row:
                multisub = multisub + sub + '+'
        print(subs)
    print(multisub)


    
    # pull a subreddit
    # Note: possible to do a multireddit
    
    #sub = reddit.subreddit('supermodelcats')
    sub = reddit.subreddit(multisub)
    # pull "limit" number of posts and then get the image urls
    img_urls = get_images(sub, 900)

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

