locu_api = '4fda38a894269e7abed0b1b5c4af272a4c82decd'

import urllib.request
import json
import codecs
url = 'https://api.locu.com/v1_0/venue/search/?locality=Conway&api_key=4fda38a894269e7abed0b1b5c4af\
272a4c82decd'
request = urllib.request.urlopen(url)
reader = codecs.getreader("utf-8")
data = json.load(reader(request))

for each in data['objects']:
    print (each)
