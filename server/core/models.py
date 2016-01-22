#!/usr/bin/env python
from google.appengine.ext import ndb


class BaseModel(ndb.Model):

    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def api_list(cls):
        return [obj.api_message() for obj in cls.query()]  # TODO: Expensive.  Optimize, paginate, etc.

    @classmethod
    def api_read(cls, *args):
        return cls.get_by_id(args[0]).api_message()

    def api_message(self, stub=False):  # TODO: Allow thing to be added, not just overridden?
        """Define the message sent back for a READ request from the API

        Override this to redefine what gets sent or call this with super and subclass it
        # TODO: Use _api_message() instead of requiring super?

        Args:
            stub: Should we just send a quick stub of the data? (useful for collections)

        Returns: Data to be passed back through the API
        """
        data = {'id': self.key.id()}
        if not stub:
            data.update({
                'created_at': self.created_at,
                'updated_at': self.updated_at
            })
        return data
