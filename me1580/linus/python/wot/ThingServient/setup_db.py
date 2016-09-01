# -*- coding: utf-8 -*-
from pymongo import MongoClient

# Set up initial test database (MongoDB)
dbclient = MongoClient()
db = dbclient.wot
# Set up an initial things collection
initial_things = [
    {
    'id': 1,
    'name': u'Light manager',
    'uri': u'http://194.47.142.175:5000/light',
    'description': u'Manages sensors and actuators to control lights',
    'sensors':[{
        'id': 1,
        'name': u'Luminosity sensor',
        'description': u'Current luminosity (measured in 5 minute intervals)',
        'type': u'Float',
        'value': 0.675
        }],
    'actors':[{
          'id': 1,
          'name': u'Light',
          'description': u'Lightswitch to control the light',
          'type': u'Boolean',
          'value': u'False'
    }]
  }
]

result = db.thing.insert_many(initial_things)
print result.inserted_ids
