from scrapers.redditscraper import connect, get_images
from scrapers.imagescraper import grab_rdm_img
from gui import display_img
import praw
import PIL

if __name__ == '__main__':
    print("World Hello")

    reddit = connect()

    sub_aww = reddit.subreddit('earthporn')

    img_urls = get_images(sub_aww, 500)

    img = grab_rdm_img(img_urls)

    display_img(img)
    #img.show()
