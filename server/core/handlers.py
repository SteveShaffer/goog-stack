#!/usr/bin/env python
# TODO: Better module name than "handlers"
import webapp2

import json


class BaseHandler(webapp2.RequestHandler):

    model = None  # Override with model class  # TODO: Should this default to a generic BaseModel class?

    def send_json(self, content):
        self.response.headers['content-type'] = 'application/json'
        self.response.write(json.dumps(content))  # TODO: Need to be able to parse dates (and other types I'm sure)


class CollectionHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.send_json(self.model.api_list(*args, **kwargs))


class ResourceHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.send_json(self.model.api_read(*args, **kwargs))


class WSGIApplication(webapp2.WSGIApplication):  # TODO: Name something cooler
    pass  # TODO: Do more than just an alias
