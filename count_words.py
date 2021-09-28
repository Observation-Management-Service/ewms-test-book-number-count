#!/bin/python

from collections import Counter
# import subprocess
# from mqclient_pulsar import Queue
import pulsar
import json

def count_words(s: list) -> dict:
    return dict(Counter(s))

def get_token(token_file: str) -> str:
    with open(token_file, "r") as tf:
        token = tf.read()
    return token

token = get_token("auth.token")

client = pulsar.Client(
    'pulsar://pulsar.api.jetstream.rr.icecube.aq:6650',
    authentication=pulsar.AuthenticationToken(token)
    )

consumer = client.subscribe('persistent://test/pre-grid/book-in-test', 
                            'test-sub-1',
                            consumer_type=pulsar.ConsumerType.Shared,
                            initial_position=pulsar.InitialPosition.Earliest)

producer = client.create_producer('persistent://test/pre-grid/book-out-test')

while True:
    try:
        msg = consumer.receive(timeout_millis=10000)
    except pulsar.exceptions.Timeout:
        print("x")
        break
    data = msg.data().decode()
    print(data.strip().split(" ")[0])
    if not data.strip().split(" ")[0]:
        consumer.acknowledge(msg)
        continue
    newl = []
    for w in data.strip().split(" "):
        if "." in w: w = w.strip(".")
        if "," in w: w = w.strip(",")
        if "\"" in w: w = w.strip("\"")
        newl.append(w)
    print(newl)
    word_count = count_words(newl)
    print(msg.data(), msg.message_id(), word_count)
    producer.send(json.dumps(word_count).encode('utf-8'))
    consumer.acknowledge(msg)

client.close()





    


#  with open("book", "r") as file:
#     ...:     for l in file.readlines():
#     ...:         if not l.strip().split(" ")[0]:
#     ...:             continue
#     ...:         newl = []
#     ...:         for w in l.strip().split(" "):
#     ...:             if "." in w: w = w.strip(".")
#     ...:             if "," in w: w = w.strip(",")
#     ...:             if "\"" in w: w = w.strip("\"")
#     ...:             newl.append(w)
#     ...:         print(Counter(newl))
