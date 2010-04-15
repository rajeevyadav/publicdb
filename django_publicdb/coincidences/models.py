from django.db import models

import zlib
import cPickle as pickle
import base64

from django_publicdb.inforecords import models as inforecords


class SerializedDataField(models.Field):
    # This makes sure that to_python() will be called when objects are
    # initialized
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        super(SerializedDataField, self).__init__(*args, **kwargs)

    def db_type(self):
        return 'LONGBLOB'

    def to_python(self, value):
        try:
            unpickled = pickle.loads(zlib.decompress(base64.b64decode(value)))
        except:
            return value
        else:
            return unpickled

    def get_db_prep_value(self, value):
        return base64.b64encode(zlib.compress(pickle.dumps(value)))

class Event(models.Model):
    date = models.DateField()
    time = models.TimeField()
    nanoseconds = models.IntegerField()
    station = models.ForeignKey(inforecords.Station)
    pulseheights = SerializedDataField()
    integrals = SerializedDataField()
    traces = SerializedDataField()
    
    class Meta:
        ordering = ('date', 'time', 'nanoseconds', 'station')

class Coincidence(models.Model):
    date = models.DateField()
    time = models.TimeField()
    nanoseconds = models.IntegerField()
    events = models.ManyToManyField(Event)

    def num_events(self):
        return self.events.count()
    
    class Meta:
        ordering = ('date', 'time', 'nanoseconds')
