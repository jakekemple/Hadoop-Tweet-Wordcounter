#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "2842408481-TtwFDJpcnjmoJXSJRpCMF6llHPBnUvr7mNdOgzT"
access_token_secret = "RhP31HRTdmGmhfpOHYjY7UECGQVg34XxNX02ymtvDY1wV"
consumer_key = "OjvwP5iftQjXKTw20iLinoasC"
consumer_secret = "dMFGwZD5eqHsTSLrIx9sc1K4D5wcsXtI9ccsVVuFY3vcQOrnYq"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        #print data
        with open('fetched_tweets.txt','a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['#hungry', '#food', '#delicious'])
