#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import json

api = InstagramAPI("instamike59.officiel", "091h1scd")

if (api.login()):
	api.getSelfUserFeed()  # get self user feed
	data = api.LastJson
	print (type(data))
	json.dumps(data, indent=4)
	with open('data.json', 'w') as f:
    		f.write(json.dumps(data, indent=4))

#	print(data)
	print("Login succes!")
else:
	print("Can't login!")
