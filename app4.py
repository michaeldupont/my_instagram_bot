from flask import Flask, render_template
from InstagramAPI import InstagramAPI
import json
import pandas as pd

MyApp = Flask(__name__)

@MyApp.route("/")
def hello():
    with open("config.json","r") as fichier:
        conf = json.load(fichier)
    username = conf["INSTAGRAM"]["USER"]

    return render_template("index.html", user=username)

@MyApp.route("/data")
def data():
    with open("config.json","r") as fichier:
        conf = json.load(fichier)
    user = conf["INSTAGRAM"]["USER"]
    pwd = conf["INSTAGRAM"]["PASSWORD"]
    api = InstagramAPI(user,pwd)

    if api.login():
        api.getSelfUserFeed()
        data1 = api.LastJson
        with open("data1.json", "w") as f:
            f.write(json.dumps(data1, indent=4))
            #test sur git branche de test
        
    return render_template("index.html")

@MyApp.route("/bytel")
def bytel():
    return render_template("index.html")

if __name__ == "__main__":
	MyApp.run()