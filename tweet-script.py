"""
Script to retrieve tweets via tweepy & the twitter api
Usage: Run ./get-tweets.py <hashtag word>
"""

#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

#Variables that contains the user credentials to access Twitter API
access_token = "XXXX"
access_token_secret = "XXXX"
consumer_key = "XXXX"
consumer_secret = "XXXX"

hashtag_word = sys.argv[1]
if ('#' not in hashtag_word):
    hashtag_word = "#" + sys.argv[1]

#This is a basic listener that just prints received tweets to stdout.
class tweet_grab:

    def on_data(self, hashtag):
        count = 0
        # Copy from twitter to file
        with open('fetched_tweets.txt','a') as tf:
            for page in tweepy.Cursor(api.search, q=hashtag, rpp=100, result_type="recent").pages():
                for tweet in page:
                    # Exclude Retweets from tweets written to file
                    if (not tweet.retweeted) and ('RT @' not in tweet.text):
                        tf.write('\n\n\n')
                        tf.write(tweet.text)
                count+=1
                print("pages gathered so far: ", count)
            return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)
    tweet_grab().on_data(hashtag_word)

    sys.exit
