# DEPENDENCIES
import tweepy # python library, documentation here: http://docs.tweepy.org/en/latest/index.html
import pandas as pd
from keyring import twitter_public_key, twitter_secret_key, twitter_public_access_token, twitter_secret_access_token

# build the engine that will allow for interaction with the API
auth = tweepy.OAuthHandler(twitter_public_key, twitter_secret_key)
auth.set_access_token(twitter_public_access_token, twitter_secret_access_token)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) 

# FUNCTIONS
# this function will cause the authenticated user to follow the Users that are following the specified account
def followBack(user=api.me()): # defaults to self, change here to follow a different User's followers
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
    print("I ain't no follow-back girl")

# RUN ME
followBack()
