from kafka.admin import KafkaAdminClient, NewTopic,ConfigResource,ConfigResourceType
topic_name="streaming"
admin_client = KafkaAdminClient(bootstrap_servers=['localhost:9092'])
# Hien thi danh sach topic
list_topic=admin_client.list_topics()
print("List topic :",list_topic)
# Tao topic neu chua ton tai
if topic_name not in list_topic:
    new_topic = NewTopic(topic_name, num_partitions=1, replication_factor=1, topic_configs={'retention.ms': '60000', 'retention.bytes': '10485760'})
    admin_client.create_topics([new_topic])
    print("Da tao topic",topic_name)
# Xem thong tin topic
print("Thong tin topic",topic_name)
configs = admin_client.describe_configs(config_resources=[ConfigResource(ConfigResourceType.TOPIC, topic_name)])
config_list = configs[0].resources[0][4]
for config in config_list:
    print(config)


admin_client.close()