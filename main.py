import jinja2
import webapp2
import os
import json
import urllib
import urllib2
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainPage(webapp2.RequestHandler):
    def get(self):
        loginTemplate = jinja_environment.get_template('templates/Login.html')
        self.response.write(loginTemplate.render())

    # function onSignIn(googleUser) {
    #     var profile = googleUser.getBasicProfile();
    #     console.log('ID: ' + profile.getId());
    #     console.log('Name: ' + profile.getName());
    #     console.log('Image URL: ' + profile.getImageUrl());
    #     console.log('Email: ' + profile.getEmail());

app = webapp2.WSGIApplication([
    ('/', MainPage),
])
