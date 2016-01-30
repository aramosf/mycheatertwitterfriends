#!/usr/bin/python

from twitter import *
from bs4 import BeautifulSoup
from urllib2 import urlopen
import requests

# Edit with your details
consumer_key = "xxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxx"
access_key = "xxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
username = "aramosf"
#

twitter = Twitter(
		auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))
query = twitter.friends.ids(screen_name = username)
for n in range(0, len(query["ids"]), 100):
	ids = query["ids"][n:n+100]
	subquery = twitter.users.lookup(user_id = ids)
	for user in subquery:
		url = "https://www.twitteraudit.com/" + user["screen_name"]
		req = requests.get(url)
		html = BeautifulSoup(req.text,"lxml")
		find = html.find('div',{'class':'percentage good'})
		try: 
		   per=find.contents
		except:
		   per[0]="null"
		print "user:", user["screen_name"].rstrip(), ":", per[0].rstrip().strip()

