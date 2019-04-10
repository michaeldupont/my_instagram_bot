from flask import Flask, render_template
from InstagramAPI import InstagramAPI
import json

MyApp = Flask(__name__)

@MyApp.route("/")
def hello():
	return render_template('index.html')

@MyApp.route('/data')
def data():
	with open('config.json', 'r') as f:
		config = json.load(f)
	
	user = config['INSTAGRAM']['USER']
	pwd = config['INSTAGRAM']['PASSWORD']

	api = InstagramAPI(user, pwd)
	
	if (api.login()):
		api.getSelfUserFeed()  # get self user feed
		data = api.LastJson
        print (type(data))
    	json.dumps(data, indent=4)
       	with open('data1.json', 'w') as f:
			f.write(json.dumps(data, indent=4))
	
	else:
		print("can't login")
	
	return render_template('index.html')

@MyApp.route('/bytel')
def bytel():
	return render_template('index.html')

if __name__ == "__main__":
	MyApp.run()
