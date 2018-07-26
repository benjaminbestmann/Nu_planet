import jinja2
import webapp2
import os
import json
import urllib
import urllib2
import logging
from google.appengine.ext import ndb
from google.appengine.api import urlfetch
from google.appengine.api import users


jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(
        os.path.dirname(__file__)))


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




class UserData(ndb.Model):
    id = ndb.StringProperty(required=False)
    fullname = ndb.StringProperty(required=False)
    givenname = ndb.StringProperty(required=False)
    imageurl = ndb.StringProperty(required=False)
    email = ndb.StringProperty(required=False)

class UserFood(ndb.Model):
    email = ndb.StringProperty(required=False)
    food = ndb.StringProperty(required=False)
    place = ndb.StringProperty(required=False)
    calories = ndb.IntegerProperty(required=False)
    created_at = ndb.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        loginTemplate = jinja_environment.get_template('index.html')
        self.response.write(loginTemplate.render())

class LoginPage(webapp2.RequestHandler):
    def get(self):
        signinTemplate = jinja_environment.get_template('old templates/Login.html')
        self.response.write(signinTemplate.render())

class UserPage(webapp2.RequestHandler):
    def get(self):
        query1 = UserFood.query()
        food = query1.order(-UserFood.created_at).fetch(limit=10)
        total=0
        for i in food:
            if i.calories == None:
                i.calories=0
            total= i.calories + total
        dict = {
            "string" : food,
            "total": total
            }
        userTemplate = jinja_environment.get_template('html5up-big-picture/user.html')
        self.response.write(userTemplate.render(dict))

    def post(self):
        user_email = self.request.get('email')
        user_food = self.request.get('food')
        user_place = self.request.get('place')
        user_calories = self.request.get('calories')
        user_input = UserFood(food = user_food, place = user_place, calories= int(user_calories), email = user_email)
        user_input.put()
        self.redirect('/user')



class  DataEndpoint(webapp2.RequestHandler):
    def post(self):
        print("post")
        requestObject = json.loads(self.request.body)
        userdata = requestObject.get('data')
        # myuser = user_key
        myuser= UserData()
        print(list(userdata.keys()))
        myuser.id = userdata.get('id')
        myuser.fullname = userdata.get('fullname')
        myuser.givenname = userdata.get('givenname')
        myuser.imageurl = userdata.get('imageurl')
        myuser.email = userdata.get('email')
        myuser.put()



class QueryHandler(webapp2.RequestHandler):
    def get(self):
        query1 = UserFood.query()
        food = query1.fetch()
        print food
        dict = {
            "string" : food
            }
        template = jinja_environment.get_template('Templates/maps2.html')
        self.response.write(template.render(dict))

        # template = jinja_environment.get_template('Templates/maps2.html')
        # self.response.write(template.render(variables))



app = webapp2.WSGIApplication([
      ('/', MainPage),
      ('/login', LoginPage),
      ('/user', UserPage),
      ('/data', DataEndpoint),
      ('/query',QueryHandler),
])
