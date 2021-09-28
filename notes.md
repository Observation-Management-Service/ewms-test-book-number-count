auth errors can show up in weird ways:
2021-09-23 10:56:09.319 ERROR [140128357570304] ClientImpl:181 | Error Checking/Getting Partition Metadata while creating producer on persistent://test/pre-grid/laptop -- ConnectError
when using a malformed token


Consumers will always be FIFO.
To read a queue from the start (before a subscription is created) you need the "earliest". Default is "latest", which will give you all messages since the subscription was created in FIFO order. 

If the subscription was created with latest, you cannot change to earliest. the start point for the subscription will be the point when the subscription was created