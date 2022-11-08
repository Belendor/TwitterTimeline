import os
from urllib import response
import tweepy
from dotenv import load_dotenv

load_dotenv()

# client = tweepy.Client(consumer_key=os.getenv('CONSUMER_KEY'),
#                        consumer_secret=os.getenv('CONSUMER_SECRET'),
#                        access_token=os.getenv('ACCESS_TOKEN'),
#                        access_token_secret=os.getenv('TOKEN_SECRET'))

# response = client.create_tweet(text='hello worl!111')
# mediaID = client.media_upload()


# print(mediaID)

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'),
                           os.getenv('CONSUMER_SECRET'))

# set access to user's access key and access secret
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('TOKEN_SECRET'))

# calling the api
api = tweepy.API(auth)

# the text to be tweeted
status = "This is a media upload."

# the path of the media to be uploaded
filename = "gfg.png"

# posting the tweet
media = api.media_upload(os.getcwd() + '\\uploads\\3.png')

print("The media ID is : " + media.media_id_string)
mediaID1 = media.media_id_string

client = tweepy.Client(consumer_key=os.getenv('CONSUMER_KEY'),
                       consumer_secret=os.getenv('CONSUMER_SECRET'),
                       access_token=os.getenv('ACCESS_TOKEN'),
                       access_token_secret=os.getenv('TOKEN_SECRET'))

response = client.create_tweet(text='I want to Post 3 Photos and description', media_ids=[mediaID1])

print(response)
