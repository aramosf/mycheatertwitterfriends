#!/usr/bin/python
# 
# + support to add audits to twitteraudit (need valid cookies)

from twitter import *
from bs4 import BeautifulSoup
from urllib2 import urlopen
import requests
import logging
import httplib
import requests

# Edit with your details
consumer_key = "xxxxx"
consumer_secret = "xxxx"
access_key = "xxxx"
access_secret = "xxxxx"
username = "aramosf"
# twitteraudit cookies
sessionid="xxxxx"
csrftoken="xxxxxx"
####


#httplib.HTTPConnection.debuglevel = 1

#logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
#requests_log = logging.getLogger("requests.packages.urllib3")
#requests_log.setLevel(logging.DEBUG)
#requests_log.propagate = True

twitter = Twitter(
		auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))
query = twitter.friends.ids(screen_name = username)
for n in range(0, len(query["ids"]), 100):
	ids = query["ids"][n:n+100]
	subquery = twitter.users.lookup(user_id = ids)
	for user in subquery:
	    	u = 'https://www.twitteraudit.com/'
		url = u + user["screen_name"]
		req = requests.get(url)
		html = BeautifulSoup(req.text,"lxml")
		find = html.find('div',{'class':'percentage good'})
		try: 
		   per=find.contents
		except:
	           pl = { 'csrfmiddlewaretoken' : csrftoken, 'screen_name' : user["screen_name"] }
	           h = { 'Referer': 'https://www.twitteraudit.com/' + user["screen_name"] }
	           req = requests.post(u, data=pl,  cookies={"sessionid": sessionid, "csrftoken": csrftoken}, headers=h )
	           per[0]="null"
		print "user:", user["screen_name"].rstrip(), ":", per[0].rstrip().strip()

