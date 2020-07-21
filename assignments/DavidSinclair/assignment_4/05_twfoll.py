import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import time

#get keys from: https://apps.twitter.com/
#consumer key, consumer secret, access token, access secret.
ckey = 'TulEhMcwsvnMGgDnYXJS2O0Mr'
csecret = '9ZfQvJy6CDF20fAVoFDL0YZhBMBwoN6Kb9NXtwxIJWvVaH31DX'
atoken = '955941770369609733-gcO2pTEx5gNikLQb05l6gEuTfAlw6li'
asecret = 'wSwUnXYJodfT78rhXkzQpjfaFVYfwpwfwfmtOTZrqPkwS'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

for user in tweepy.Cursor(api.followers, screen_name="acnwala").items():
    print(user.screen_name,',',user.followers_count,file=open('acnwalatwt.csv','a'))
