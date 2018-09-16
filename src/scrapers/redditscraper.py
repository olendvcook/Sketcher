import praw
import shelve


def connect():
    """
    Read reddit connect info from shelve db, (or create if doesn't exist)
    and then return a reddit connection
    """
    client_id = client_secret = username = password = None

    with shelve.open('./resources/redditdata') as rdata:
        try:
            client_id = rdata['client_id']
        except KeyError as ke:
            client_id = input("Reddit client_id missing, please input:")
            rdata['client_id'] = client_id
        try:
            client_secret = rdata['client_secret']
        except KeyError as ke:
            client_secret = input("Reddit client_secret missing, please input:")
            rdata['client_secret'] = client_secret
        try:
            username = rdata['username']
        except KeyError as ke:
            username = input("Reddit username missing, please input:")
            rdata['username'] = username
        try:
            password = rdata['password']
        except KeyError as ke:
            password = input("Reddit password missing, please input:")
            rdata['password'] = password
        print('id: ' + rdata['client_id'])
        print('secret: ' + rdata['client_secret'])
        print('username: ' + rdata['username'])
        #print('password: ' + rdata['password'])

        return praw.Reddit(client_id=client_id, \
                            client_secret=client_secret, \
                            user_agent='Sketcher', \
                            username=username, \
                            password=password)

def get_images(subreddit, limit):
    """
    generates a list of image urls from 'hot' posts from passed in subreddit
    """
    image_urls = []
    for submission in subreddit.top(limit=limit):
        if '.gifv' in submission.url:
            #no gifs
            continue
        elif '.jpg' in submission.url:
            image_urls.append(submission.url)
        elif '.png' in submission.url:
            image_urls.append(submission.url)
        elif 'i.imgur.com/' in submission.url:
            image_urls.append(submission.url)
        elif 'imgur.com/' in submission.url:
            imageHash = submission.url.split('/')[-1].split('?')[0] + '.jpg'
            image_urls.append('i.imgur.com/' + imageHash)
    #print(image_urls)
    return image_urls


        

