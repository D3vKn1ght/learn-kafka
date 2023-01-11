Su dung: docker compose up <br>
pip install kafka-python<br>
cd kafka_python <br>
Tao topic voi config messsage : python3 management.py <br>
Publish message : python3 producers.py <br>
Subcribe message: python3 consumers.py <br>
consumers.py se luu frame image nhan duoc trong folder image <br>



Note:
Chinh sua topic, set tu dong xoa message sau 1 phut: kafka-topics.sh --alter --topic streaming --config retention.ms=60000 --zookeeper zookeeper:2181 <br>


To set a time-to-live (TTL) for messages in Kafka or delete messages after a certain number of messages have been produced to a partition, you can use the retention.ms and retention.bytes configurations for your Kafka topic. <br>

The retention.ms configuration sets the maximum amount of time that a message is retained in the topic before it is deleted. For example, if you set retention.ms to 86400000 (1 day), then any message that is older than 1 day will be deleted. <br>

The retention.bytes configuration sets the maximum amount of data that is retained in the topic before messages are deleted. For example, if you set retention.bytes to 1073741824 (1 GB), then any messages that exceed 1 GB in total size will be deleted. <br>

You can set these configurations when you create a new topic or modify an existing topic using the kafka-topics command-line tool. For example, to create a new topic with a retention period of 1 day and a maximum size of 1 GB, you can use the following command: <br>
kafka-topics.sh --create --topic my-topic --replication-factor 1 --partitions 1 --config retention.ms=86400000 --config retention.bytes=1073741824 <br>

link tham khao:  <br>
https://github.com/better-data-science/Apache-Kafka-in-Python <br>
https://betterdatascience.com/how-to-install-apache-kafka-using-docker-the-easy-way/ <br>
https://betterdatascience.com/master-the-kafka-shell-in-5-minutes-topics-producers-and-consumers-explained/ <br>
