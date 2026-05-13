import time
import requests

from camera_capture import Camera

from text_to_speech import (
    speak_text
)

from config import (
    SERVER_URL,
    CAPTURE_INTERVAL
)


camera = Camera()


def send_image(
    image_path
):

    with open(
        image_path,
        "rb"
    ) as img:

        files = {
            "image": img
        }

        response = requests.post(
            SERVER_URL,
            files=files
        )

    return response.json()


try:

    while True:

        image = camera.capture()

        result = send_image(
            image
        )

        caption = result[
            "caption"
        ]

        speak_text(
            caption
        )

        time.sleep(
            CAPTURE_INTERVAL
        )

except KeyboardInterrupt:

    camera.release()