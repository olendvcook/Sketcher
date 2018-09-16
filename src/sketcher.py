from scrapers.redditscraper import connect
import praw

if __name__ == '__main__':
    print("World Hello")

    reddit = connect()

    sub_aww = reddit.subreddit('aww')

    for submission in sub_aww.hot(limit=20):
        print(submission.title, submission.id)



"""
def download_image(imageUrl, localFileName):
    make_sure_path_exists(directory)
    print(imageUrl)
    response = requests.get(imageUrl)

    if response.status_code == 200:
        print('Downloading %s...' % localFileName)
        localFilePath = directory + localFileName
        with open(localFileName, 'wb') as fh:
            for chunk in response.iter_content(4096):
                fh.write(chunk)
        print('Download complete!')
    else:
        print('Problem downloading - status code %s' % response.status_code)

    print(localFileName)
    return localFileName
"""

'''
    subreddit = reddit.subreddit('SketchDaily')
    print(subreddit.description)
    for submissions in subreddit.new(limit=1):
        print(submissions.selftext)
    print("Hello World!")
    rPics = reddit.subreddit('aww')
    for submission in rPics.new(limit=1):
        print(submission.url)
        if '.jpg' in submission.url:
            imagePath = downloadImage(submission.url, submission.url.split('/')[-1])
            createGUI(imagePath)
        elif 'i.imgur.com/' in submission.url:
            imagePath = downloadImage(submission.url, submission.url.split('/')[-1].split('?')[0])
            createGUI(imagePath)
        elif 'imgur.com/' in submission.url:
            imageHash = submission.url.split('/')[-1].split('?')[0] + '.jpg'
            imagePath = downloadImage('i.imgur.com/' + imageHash, imageHash)
            createGUI(imagePath)
        else:
            createGUI(imagePath)
            '''