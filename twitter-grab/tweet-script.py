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

hashtag_word = "#" + sys.argv[1]

#This is a basic listener that just prints received tweets to stdout.
class tweet_crawler:

    def on_data(self, hashtag):

        #print data
        with open('fetched_tweets.txt','a') as tf:
            for tweet in tweepy.Cursor(api.search, q=hashtag, count=5, result_type="recent").items():
                tf.write('\nNew Tweet:\n')
                tf.write(tweet.text)
            return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    #l = tweet_crawler().on_data('#food')

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweet_crawler().on_data(hashtag_word)
    #stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['#hungry', '#food', '#delicious'])
