#!/bin/python
import pulsar
from common import get_token
# client = pulsar.Client(
#     'pulsar://pulsar.api.jetstream.icecube.aq:6651',
#     authentication=pulsar.AuthenticationToken('eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZXN0LXVzZXItd29yZHMiLCJleHAiOjE2NjI1ODMyNzN9.ts3xrJ1rB5G5HBS67CZSsOJ-Am5p35duSVK7l6AR5SDCiwuI9_aX-rhv9G6VaUxbqESInM83tx0yI8G53JMYOw')
#     )

token = get_token("auth.token")

client = pulsar.Client(
    'pulsar://pulsar.api.jetstream.rr.icecube.aq:6650',
    # authentication=pulsar.AuthenticationToken('eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZXN0LXVzZXItd29yZHMiLCJleHAiOjE2NjI1ODMyNzN9.ts3xrJ1rB5G5HBS67CZSsOJ-Am5p35duSVK7l6AR5SDCiwuI9_aX-rhv9G6VaUxbqESInM83tx0yI8G53JMYOw')
    authentication=pulsar.AuthenticationToken(token)
    )

# client.get_topic_partitions("persistent://test/dummy/laptop")

producer = client.create_producer('persistent://test/pre-grid/book-in-test')

# for i in range(10):
#     producer.send(('Hello-%d-v2' % i).encode('utf-8'))


# def count_words(s):
#     return dict(Counter(s.strip().split(" ")))

with open("book", "r") as b:
    for l in b.readlines():
        l = l.strip()
        print(l)
        producer.send(l.encode('utf-8'))
client.close()
