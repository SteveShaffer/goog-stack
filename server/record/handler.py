#!/usr/bin/env python
import webapp2

import models

import json


class RecordHandler(webapp2.RequestHandler):
    def get(self, record_type, record_id):
        record = models.Record.get_by_type_and_id(record_type, record_id)  # TODO: Pluralization?
        self.response.headers['content-type'] = 'application/json'
        self.response.write(json.dumps(record.api_message()))  # TODO: Helper functions in the base class

app = webapp2.WSGIApplication([
    ('/api/records/(.*)/(.*)', RecordHandler),
], debug=True)
