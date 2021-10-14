#!/bin/python

from collections import Counter
# import subprocess
# from mqclient_pulsar import Queue
import pulsar
from common import get_token

token = get_token("auth.token")

client = pulsar.Client(
    'pulsar://pulsar.api.jetstream.rr.icecube.aq:6650',
    authentication=pulsar.AuthenticationToken(token)
    )

consumer = client.subscribe('persistent://test/pre-grid/book-out-test', "test-mctest")

while True:
    msg = consumer.receive()
    print(msg.data())
    consumer.acknowledge(msg)
client.close()