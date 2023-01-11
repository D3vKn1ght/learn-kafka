import json 
from kafka import KafkaConsumer
import cv2
import base64
import numpy as np

if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        'streaming',
        bootstrap_servers='localhost:9094',
        auto_offset_reset='earliest'
    )
    dem =0
    for message in consumer:
        my_bytes_value = message.value
        my_json = my_bytes_value.decode('utf8')
        dict = eval(my_json)
        camera_id=str(dict["camera_id"])
        jpeg = base64.b64decode(dict["frame"])
        # Decode the JPEG image
        image = cv2.imdecode(np.frombuffer(jpeg, dtype=np.uint8), cv2.IMREAD_COLOR)
        cv2.imwrite(f"image/{camera_id}_{dem}.jpeg", image)
        print("Receive image save in",f"image/{camera_id}_{dem}.jpeg")
        dem+=1
