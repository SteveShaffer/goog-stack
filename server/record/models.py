#!/usr/bin/env python
from google.appengine.ext import ndb


class RecordType(ndb.Model):
    # ID = User-generated
    pass


class Record(ndb.Model):
    # Parent = RecordType
    # ID = User-generated

    def api_message(self):  # TODO: Default override-able in base class?
        return {
            'type': self.key.parent().id(),
            'id': self.key.id()
        }

    @classmethod
    def get_by_type_and_id(cls, record_type, record_id):
        record_type = RecordType.get_or_insert(record_type)  # TODO: Why never-used errors here?
        record = Record.get_or_insert(record_id, parent=record_type.key)
        return record
