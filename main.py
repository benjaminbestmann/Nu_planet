import jinja2
import webapp2
import os
import json
import urllib
import urllib2
from google.appengine.ext import ndb
from google.appengine.api import users

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

app = webapp2.WSGIApplication([
      ('/', MainPage),
      ('/login', LoginPage),
      ('/user', UserPage),
])
