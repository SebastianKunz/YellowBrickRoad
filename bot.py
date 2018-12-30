#!/usr/bin/env python

import tweepy
from time import sleep
import datetime

consumer_key = "XXXX"
consumer_secret = "XXXX"
access_token = "XXXX"
access_token_secret = "XXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweet = api.user_timeline("42SiliconValley", count = 1)[0]

timestamp = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

file = open("Log.txt", "a")
try:
    tweet.favorite()
    tweet.retweet()
    api.update_status(status = "Hey, my Python-Bot just retweeted and favorited the latest Tweet of @42SiliconValley !")
    file.write(timestamp + ": " + "Succsess!" + "\n")
except tweepy.TweepError as e:
    file.write(timestamp + ": " + str(e.message[0]['message']) + "\n")
file.close()
