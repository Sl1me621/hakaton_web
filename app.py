from flask import Flask, render_template

import requests

app = Flask(__name__)
import json
name='Имя'
def readData():...

def readApi():
    r = requests.get('https://reqres.in/api/users?per_page=12').json()
    return (r['data'])
def readApi2():
    rn = requests.get('https://reqres.in/api/users?per_page=12').json()
    return (rn['data'])
@app.route("/")
def home():
    return render_template('index.html')
@app.route("/team")
def team():
    allteam= readApi()
    return render_template('team.html',allteam=allteam)
@app.route("/weather")
def weather():
    weatherr= readApi2()
    return render_template('/weather',weatherr=weatherr)


@app.route("/allinfo")
def allinfo():
    return render_template('allinfo.html')
if __name__=="__main__":
    app.run(debug=True)