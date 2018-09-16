from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

"""
Scrapes Images from a Subreddit
"""

def scrape_url(url):
    """
    Attempts to get the content at url
    """
    print("Attempting to get " + url)
    try:
        resp = get(url)
        if is_good_response(resp):
            return resp.content
        else:
            print('Bad Response from ' + url)
            return None

    except RequestException as e:
        print('Error during requests to {0} : {1}', format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    return (resp.status_code == 200 )
