

import urllib.request
import json
import codecs
locu_api = '4fda38a894269e7abed0b1b5c4af272a4c82decd'
url = 'https://api.locu.com/v1_0/venue/search/?name=hello&locality=Conway&cuisine=Asian&api_key=4fda38a894269e7abed0b1b\
5c4af272a4c82decd'


object_dict = {}

state = input("Please enter your State:")
object_dict['State'] = state

locality = input("Please enter City Name:")
object_dict['City'] = locality

print("Would you like to enter the name of the restaurant?")
choice = input('Y/y for yes or N/n for no: ')
if choice == 'Y' or choice == 'y':
    rest_name = input("Please enter name of restaurant: ")
else:
    rest_name = None
object_dict['Restaurant'] = rest_name

print("Would you like to enter the cuisine of the restaurant?")
choice = input('Y/y for yes or N/n for no: ')
if choice == 'Y' or choice == 'y':
    food_type = input("Please enter desired cuisine: ")
else:
    food_type = None
object_dict['Cuisine'] = food_type

def restaurant_search(**object_dict):
    new_url = 'https://api.locu.com/v1_0/venue/search/?api_key=4fda38a894269e7abed0b1b5c4af272a4c82decd'
    new_url = 'https://api.locu.com/v1_0/venue/search/?api_key=4fda38a894269e7abed0b1b5c4af272a4c82decd' \
        + "&locality=" + object_dict['City'] + '&region=' + object_dict['State']

    if object_dict['Restaurant'] is not None:
        new_url = 'https://api.locu.com/v1_0/venue/search/?api_key=4fda38a894269e7abed0b1b5c4af272a4c82decd' \
            + "&locality=" + object_dict['City'] + '&name=' + object_dict['Restaurant']
    if object_dict['Cuisine'] is not None:
        new_url = 'https://api.locu.com/v1_0/venue/search/?api_key=4fda38a894269e7abed0b1b5c4af272a4c82decd' \
            + "&locality=" + object_dict['City'] + '&name=' + object_dict['Restaurant'] + '&cuisine=' + \
            object_dict['Cuisine']
    request = urllib.request.urlopen(new_url)
    reader = codecs.getreader("utf-8")
    data = json.load(reader(request))

    for each in data['objects']:
        print (each['name'])
        print (each['phone'])
        print (each['street_address'], '\n')
        print ('-------------------')

restaurant_search(**object_dict)


