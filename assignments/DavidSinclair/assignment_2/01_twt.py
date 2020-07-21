'''
	prerequisites:
	0. create a twitter account
	1. obtain your access tokens: https://apps.twitter.com/
		1.0 create new app
	2. install tweepy (pip install tweepy)

	credit: 
	http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html
	http://adilmoujahid.com/posts/2014/07/twitter-analytics/
	https://pythonprogramming.net/twitter-api-streaming-tweets-python-tutorial/

	Tweet JSON:, use http://jsonviewer.stack.hu/ to view object
	https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json

	rate limiting:
	https://developer.twitter.com/en/docs/basics/rate-limiting

	streaming rate limiting:
	https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/connecting.html
'''

#Import the necessary methods from tweepy library
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

class listener(StreamListener):

	def on_data(self, data):
		#learn about tweet json structure: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json
		tweetJson = json.loads(data)
		
		#tweet = tweetJson['text']
		username = tweetJson['user']['screen_name']
		links = tweetJson['entities']['urls']

		if( len(links) != 0 and tweetJson['truncated'] == False ):
			links = self.getLinksFromTweet(links)
			
			print( username , '\t' , )
			for l in links :
				print(l ,file=open("twitterlinks.raw", "a"),)
				print(l,)
			print ()
			filename = "twitterlinks.raw"
			numLines = sum(1 for line in open("twitterlinks.raw"))
			print (numLines)
			if numLines==2000: #Number of links you want to collect and have the file stop.
				exit()

		#print('...sleep for 5 seconds')
		#time.sleep(5)

		return True

	def getLinksFromTweet(self, linksDict):

		links = []
		for uri in linksDict:
			links.append( uri['expanded_url'] )

		return links

	def on_error(self, status):
		print( status )
		
		if status_code == 420:
			#returning False in on_data disconnects the stream
			return False
		return True

		
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['government'])


