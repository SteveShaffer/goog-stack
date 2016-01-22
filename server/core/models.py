#!/usr/bin/env python
from google.appengine.ext import ndb


class BaseModel(ndb.Model):

    @classmethod
    def api_list(cls):
        return [obj.api_message() for obj in cls.query()]  # TODO: Expensive.  Optimize, paginate, etc.

    @classmethod
    def api_read(cls, *args):
        return cls.get_by_id(args[0]).api_message()

    def api_message(self):  # TODO: Allow thing to be added, not just overridden?
        return {
            'id': self.key.id()
        }
