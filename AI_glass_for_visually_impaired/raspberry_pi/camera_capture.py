import cv2

from config import (
    IMAGE_WIDTH,
    IMAGE_HEIGHT
)


class Camera:

    def __init__(self):

        self.cap = cv2.VideoCapture(
            0
        )

        self.cap.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            IMAGE_WIDTH
        )

        self.cap.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            IMAGE_HEIGHT
        )

    def capture(
        self,
        filename="capture.jpg"
    ):

        ret, frame = self.cap.read()

        if not ret:
            raise Exception(
                "Camera Error"
            )

        cv2.imwrite(
            filename,
            frame
        )

        return filename

    def release(self):

        self.cap.release()