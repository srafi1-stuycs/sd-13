# Shakil Rafi
# SoftDev1 pd7
# HW13 -- A RESTful journey skyward
# 2017-11-09

from flask import Flask, render_template
import urllib2, json

key = 'B0GjYlBz3NFCm3urthnt8Ae2ulnBO2V1mfURha2H'
app = Flask(__name__)

@app.route('/')
def index():
    url ='https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=%s' 
    resp = urllib2.urlopen(url % key)
    data = resp.read()
    data_list = json.loads(data)
    data_list = data_list['photos'][:50]
    print data_list[0]
    return render_template('index.html', photos=data_list)

if __name__ == '__main__':
    app.run(debug=True)
