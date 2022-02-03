import requests
import configparser
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')
@app.route("/results", methods=['POST'])
def results():
    zip_code=request.form['ZipCode']
    country_code=request.form['CountryCode']
    if(zip_code.isnumeric()):
        data = get_weather(zip_code, country_code, get_api())
        place = data["name"]
        temp = "{0:.2f}".format(data["main"]["temp"])
        weather = data["weather"][0]["description"]
        return render_template('results.html', place=place, temp=temp, weather=weather)
    else:
        return "Error 404"


def get_api():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']
def get_weather(zip_code,country_code, api_key):
    #.format allows us to take the variable that we are passing in functions to take in string
    api_url="http://api.openweathermap.org/data/2.5/weather?zip={},{}&units=metric&appid={}".format(zip_code,country_code,api_key)
    r = requests.get(api_url)
    return r.json()

if(__name__ == '__main__'):
    app.run()


