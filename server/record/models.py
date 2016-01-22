#!/usr/bin/env python
from server.core import models


class RecordType(models.BaseModel):
    # ID = User-generated
    pass


class Record(models.BaseModel):
    # Parent = RecordType
    # ID = User-generated

    @classmethod
    def api_read(cls, record_type, record_id):
        return cls.get_by_type_and_id(record_type, record_id).api_message()

    def api_message(self, *args, **kwargs):
        data = super(Record, self).api_message(*args, **kwargs)
        data['type'] = self.key.parent().id()
        return data

    @classmethod
    def get_by_type_and_id(cls, record_type, record_id):
        record_type = RecordType.get_or_insert(record_type)  # TODO: Why never-used errors here?
        record = cls.get_or_insert(record_id, parent=record_type.key)
        return record
