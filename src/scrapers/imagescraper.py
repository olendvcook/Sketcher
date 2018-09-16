import requests
import random
from PIL import Image

def grab_rdm_img(image_urls):
    """
    returns PIL Image randomly from list of image urls through requests
    """
    image_url = random.choice(image_urls)
    return Image.open(requests.get(image_url, stream=True).raw)

