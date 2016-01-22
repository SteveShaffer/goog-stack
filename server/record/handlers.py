#!/usr/bin/env python
from server.core import handlers

import models


class RecordCollectionHandler(handlers.CollectionHandler):
    model = models.Record


class RecordResourceHandler(handlers.ResourceHandler):
    model = models.Record


app = handlers.WSGIApplication([
    ('/api/records/(.*)/(.*)', RecordResourceHandler),
    ('/api/records/(.*)', RecordCollectionHandler),
], debug=True)
