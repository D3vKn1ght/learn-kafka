Chinh sua topic, set tu dong xoa message sau 1 phut: kafka-topics.sh --alter --topic streaming --config retention.ms=60000 --zookeeper zookeeper:2181


To set a time-to-live (TTL) for messages in Kafka or delete messages after a certain number of messages have been produced to a partition, you can use the retention.ms and retention.bytes configurations for your Kafka topic.

The retention.ms configuration sets the maximum amount of time that a message is retained in the topic before it is deleted. For example, if you set retention.ms to 86400000 (1 day), then any message that is older than 1 day will be deleted.

The retention.bytes configuration sets the maximum amount of data that is retained in the topic before messages are deleted. For example, if you set retention.bytes to 1073741824 (1 GB), then any messages that exceed 1 GB in total size will be deleted.

You can set these configurations when you create a new topic or modify an existing topic using the kafka-topics command-line tool. For example, to create a new topic with a retention period of 1 day and a maximum size of 1 GB, you can use the following command:
kafka-topics.sh --create --topic my-topic --replication-factor 1 --partitions 1 --config retention.ms=86400000 --config retention.bytes=1073741824

link: https://viblo.asia/p/kafka-docker-python-LzD5dodzljY
