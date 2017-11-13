# Shakil Rafi
# SoftDev1 pd7
# HW13 -- A RESTful journey skyward
# 2017-11-09

from flask import Flask, render_template, request
import urllib2, json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    base_url = 'http://pokeapi.co/api/v2/pokemon/%d' 
    dexnum = request.args.get('dexnum')
    if not dexnum:
        dexnum = 1
    else:
        dexnum = int(dexnum)
    url = base_url % dexnum
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
    req = urllib2.Request(url, headers=header)
    resp = urllib2.urlopen(req)
    data = resp.read()
    data_dict = json.loads(data)
    return render_template('index.html', pokemon=data_dict)

if __name__ == '__main__':
    app.run(debug=True)
