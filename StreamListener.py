# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:35:35 2019

@author: Lakshay
"""
"""
86zcMt0XZHoExyXnCR43HP5ND (API key)

f2yTpmZFt29lBcHzHzECjjO8tvepcjmNI3t9b0PqOx6qsnoeJy (API secret key)
761144980215853056-03ugz5acerhAV3JUnSV8CByXiWqYtMX (Access token)

obsSJsQhYzFjewPx4bonoeeBHqxXK73VD1rRS4LUsmXV7 (Access token secret)
"""
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "761144980215853056-03ugz5acerhAV3JUnSV8CByXiWqYtMX"
access_token_secret = "obsSJsQhYzFjewPx4bonoeeBHqxXK73VD1rRS4LUsmXV7"
consumer_key = "86zcMt0XZHoExyXnCR43HP5ND"
consumer_secret = "f2yTpmZFt29lBcHzHzECjjO8tvepcjmNI3t9b0PqOx6qsnoeJy"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['@laksharma1997'])