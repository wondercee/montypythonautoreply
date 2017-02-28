#!/usr/bin/env python
import tweepy, time, sys
#from our keys module (keys.py), import the keys dictionary
from keys import keys

argfile = 'helloworld.txt'

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

twt = api.search(q="#bored")

#filename=open(argfile,'r')
#f=filename.readlines()
#filename.close()
#print type(f)
#list of specific strings we want to check for in Tweets
t = ['#bored',
    '#Bored',
    '#BORED']

for s in twt:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s Why not enjoy a few #MontyPython quotes on my timeline?" % (sn)
            s = api.update_status(m, s.id)
            #time.sleep(900) #Tweet every 15 minutes
