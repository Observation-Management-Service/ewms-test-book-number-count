#!/bin/python

from collections import Counter
# import subprocess
# from mqclient_pulsar import Queue
import pulsar

client = pulsar.Client(
    'pulsar://pulsar.api.jetstream.icecube.aq:6651',
    authentication=pulsar.AuthenticationToken('eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZXN0LXVzZXItd29yZHMiLCJleHAiOjE2NjI1ODMyNzN9.ts3xrJ1rB5G5HBS67CZSsOJ-Am5p35duSVK7l6AR5SDCiwuI9_aX-rhv9G6VaUxbqESInM83tx0yI8G53JMYOw')
    )

consumer = client.subscribe('persistent://test/dummy/laptop', "test-mctest")

while True:
    msg = consumer.receive()
    print(msg.data())
    consumer.acknowledge(msg)
client.close()