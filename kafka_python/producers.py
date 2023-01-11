import time 
import json 
import random 
from datetime import datetime
from data_generator import generate_message,Stream
from kafka import KafkaProducer
import numpy as np

# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message).encode('utf-8')


# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)



if __name__ == '__main__':
    stream =Stream("camera01","http://camapp.click:15301/livestream/camera01/stream_0.m3u8")
    # Infinite loop - runs until you kill the program
    while True:
        hasFrame,data=stream.get_message()
        if  not hasFrame:
            print("do not frame")
            continue
        
        # Send it to our 'messages' topic
        print(f'Producing message @ {datetime.now()} | cameraid = {str(data["camera_id"])}')
        producer.send('streaming', data)
        # Sleep for a random number of seconds
        time_to_sleep = random.randint(1, 11)
        time.sleep(time_to_sleep)
    