#!/usr/bin/env python
import webapp2


class MainHandler(webapp2.RequestHandler):  # TODO: Doing nothing?
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    webapp2.Route('/client', webapp2.RedirectHandler, defaults={'_uri': '/client/'}),
], debug=True)
