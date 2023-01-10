import random 
import string 
import imutils
from imutils.video import VideoStream
import cv2
import time 
import base64

user_ids = list(range(1, 101))
recipient_ids = list(range(1, 101))


def generate_message() -> dict:
    random_user_id = random.choice(user_ids)

    # Copy the recipients array
    recipient_ids_copy = recipient_ids.copy()

    # User can't send message to himself
    recipient_ids_copy.remove(random_user_id)
    random_recipient_id = random.choice(recipient_ids_copy)

    # Generate a random message
    message = ''.join(random.choice(string.ascii_letters) for i in range(32))

    return {
        'user_id': random_user_id,
        'recipient_id': random_recipient_id,
        'message': message
    }


class Stream:
    def __init__(self,camera_id, stream_path):
        self.stream_path = stream_path
        self.camera_id=camera_id
        self.stream = VideoStream(self.stream_path).start()


    def get_message(self):
        frame = self.stream.read()
        frame=cv2.resize(frame, (1280, 720))
        # check for frame if Nonetype
        if frame is None:
            print("Het frame")
            return False,{}
        ret, jpeg = cv2.imencode(".jpg", frame)
        return True, {
        'camera_id': self.camera_id,
        'frame': base64.b64encode(jpeg).decode("utf-8")
        }

    def stop_stream(self):
        self.stream.stop()



if __name__ == '__main__':
    stream =Stream("camera01","http://camapp.click:15301/livestream/camera01/stream_0.m3u8")
    dem=0
    while True:
        hasFrame,data=stream.get_message()
        if  not hasFrame:
            print("do not frame")
            continue
        cv2.imwrite(f"image/{dem}.jpeg", data["frame"])
        dem+=1
        time.sleep(2)

        
        