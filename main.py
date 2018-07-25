import jinja2
import webapp2
import os
import json
import urllib
import urllib2
import logging
from google.appengine.ext import ndb
from google.appengine.api import urlfetch

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(
        os.path.dirname(__file__) + '/templates'))

class UserSearch(ndb.Model):
    term = ndb.StringProperty(required=True)
    count = ndb.IntegerProperty(required=True)

class Location(object):
    name = ""
    Lng = 0
    Lat = 0

    def __init__(self, name, Lng, Lat):
        self.name = name
        self.Lng = Lng
        self.Lat = Lat


def make_location(name, Lng, Lat):
    location = Location(name, Lng, Lat)
    location.name = name
    location.Lng = Lng
    location.Lat = Lat
    print(location.name)
    print(location.Lng)
    print(location.Lat)
    return location



class MainPage(webapp2.RequestHandler):
    def get(self):
        make_location("Brussels", 100, 20)
        search_term = self.request.get('search') #what is being searched
        if search_term: #if search_term does exist
            lterm = search_term.lower()
            # CREATE A KEY
            key = ndb.Key('UserSearch', lterm) #the key functions is activated looking for
            # READ DATABASE
            search = key.get()
            if not search:
                #CREATE IF NOT THERE
                search = UserSearch(
                    key =key, count =0,
                    term = search_term)
            # UPDATE ACCOUNT
                # if there's nothing in the array, it creates a new user and sets the page count to 1
        else: #if search_term doesnt exist
            search_term = "Seattle"

        searchInfo = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=%s&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyAQw6VVsR22oM5DCilaaXDEk5VOQKnLq9w" %search_term

        # getGiphy()
        # This stores the variables
        # content = json.loads(response.read())
        # This parses the data, turns it into a dictionary
        # json.loads turns the string into a dictionary
        locations = []
        # locations.append(search_term)

# This finds all the info about the location you put in, the next step is to isolate the lat and lng

        variables = {
        # 'content': content,
        'locations' : locations,
        'search_term': search_term,
        }

        template = jinja_environment.get_template('maps.html')
        self.response.write(template.render(variables))

app = webapp2.WSGIApplication([
    ('/', MainPage),])
