"""This code checks if the name is in Redis using the id key. If not, then the name is set with an expiration time,
which you use because the cache is short-lived."""

### Redis as cache database

import redis
from datetime import timedelta

# In a real web application, configuration is obtained from settings or utils
r = redis.Redis()

# Assume this is a getter handling a request
def get_name(request, *args, **kwargs):
    id = request.get('id')
    if id in r:
        return r.get(id)  # Assume that we have an {id: name} store
    else:
        # Get data from the main DB here, assume we already did it
        name = 'Bob'
        # Set the value in the cache database, with an expiration time
        r.setex(id, timedelta(minutes=60), value=name)
        return name