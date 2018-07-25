import jinja2
import webapp2
import os
import json
import urllib
import urllib2
from google.appengine.ext import ndb
from google.appengine.api import urlfetch


jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))


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
        userTemplate = jinja_environment.get_template('html5up-big-picture/user.html')
        self.response.write(userTemplate.render())


# class UserSearch(ndb.Model):
#     term = ndb.StringProperty(required=True)
#     count = ndb.IntegerProperty(required=True)
#
# def getGiphy():
#     search_term = "Paris, France"
#     params = {'api_key': 'AIzaSyAQw6VVsR22oM5DCilaaXDEk5VOQKnLq9w',
#               'q': search_term,}
#     url ="AIzaSyAQw6VVsR22oM5DCilaaXDEk5VOQKnLq9w&q=Eiffel+Tower,Paris+France"
#     api_url = '//www.google.com/maps/embed/v1/place?' + form_data
#     return api_url
#     # response = urllib2.urlopen(api_url)
#
# class MainPage(webapp2.RequestHandler):
#     def get(self):
#
#
#         search_term = self.request.get('search') #what is being searched
#         if search_term: #if search_term does exist
#             lterm = search_term.lower()
#             # CREATE A KEY
#             key = ndb.Key('UserSearch', lterm) #the key functions is activated looking for
#             # READ DATABASE
#             search = key.get()
#             if not search:
#                 #CREATE IF NOT THERE
#                 search = UserSearch(
#                     key =key, count =0,
#                     term = search_term)
#             # UPDATE ACCOUNT
#             #  SAVE
#             #  ADD TO DATABASE
#                 # if there's nothing in the array, it creates a new user and sets the page count to 1
#         else: #if search_term doesnt exist
#             search_term = "Seattle"
#
#
#
#         # This stores the variables
#         # content = json.loads(response.read())
#         # This parses the data, turns it into a dictionary
#         # json.loads turns the string into a dictionary
#         locations = []
#
#         locations.append(search_term)
#
#         variables = {
#         # 'content': content,
#         'locations' : locations,
#         'search_term': search_term,
#         }

app = webapp2.WSGIApplication([
      ('/', MainPage),
      ('/login', LoginPage),
      ('/user', UserPage),
])
