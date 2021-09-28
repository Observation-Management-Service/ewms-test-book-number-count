#!/bin/python
import pulsar

# client = pulsar.Client(
#     'pulsar://pulsar.api.jetstream.icecube.aq:6651',
#     authentication=pulsar.AuthenticationToken('eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZXN0LXVzZXItd29yZHMiLCJleHAiOjE2NjI1ODMyNzN9.ts3xrJ1rB5G5HBS67CZSsOJ-Am5p35duSVK7l6AR5SDCiwuI9_aX-rhv9G6VaUxbqESInM83tx0yI8G53JMYOw')
#     )

client = pulsar.Client(
    'pulsar://pulsar.api.jetstream.rr.icecube.aq:6650',
    # authentication=pulsar.AuthenticationToken('eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZXN0LXVzZXItd29yZHMiLCJleHAiOjE2NjI1ODMyNzN9.ts3xrJ1rB5G5HBS67CZSsOJ-Am5p35duSVK7l6AR5SDCiwuI9_aX-rhv9G6VaUxbqESInM83tx0yI8G53JMYOw')
    authentication=pulsar.AuthenticationToken('eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJ0ZXN0LXVzZXItd29yZHMiLCJleHAiOjE2NjM5NDkxMzR9.MqTCZnmzR-3n4eketM5O2ZS5wsfOdcbsQVPseQCchilswHo4XQwixl9wmM-8xCcC_5BLUVg8AYYsmnq7fb_GERaH2_azD7fxHDa8qdw6aiErTYXfH1rMjcbMzXNJGL-akhUswPR0P8wAUPyfmNmJdNJVox9kvQgskZf6qJEDiiIVjRcWlSDlH9tluQ2dwyM_gEWpcvcm2JOgGBLX4Ydj74EmRtk4UEZH7d2sI-wI6JXdjfoHAhnbSwP9UFLay21X4gV688_M3vOBSR4V2i7ME8EyQuQA8KcWFRUe_R-EAOMH-IBrfZKkj_7jPlv6qvdikZPE79zkSCgiViLHxusn1Q')
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
