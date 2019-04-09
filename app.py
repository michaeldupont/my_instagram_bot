from flask import Flask, render_template
from InstagramAPI import InstagramAPI
import json

MyApp = Flask(__name__)

@MyApp.route("/")
def hello():
	print("login success ! ")
	data = "bonjour mike"
	api = InstagramAPI("instamike59.officiel", "091h1scd")
	if (api.login()):
        	api.getSelfUserFeed()  # get self user feed
        	data = api.LastJson
        	print (type(data))
        	json.dumps(data, indent=4)
        	with open('data.json', 'w') as f:
                	f.write(json.dumps(data, indent=4))
	else:
        	print("Can't login!")

	return render_template('index.html')

@MyApp.route('/data')
def data():
	return render_template('index.html')

@MyApp.route('/bytel')
def bytel():
	return render_template('index.html')

if __name__ == "__main__":
	MyApp.run()
