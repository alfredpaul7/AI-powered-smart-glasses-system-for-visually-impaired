import cv2
import os
from datetime import datetime

from config import (
    STREAM_URL
)

from moondream_inference import (
    generate_caption
)

from raspberry_pi.text_to_speech import (
    speak_text
)


SAVE_DIR = "frames"

os.makedirs(
    SAVE_DIR,
    exist_ok=True
)


cap = cv2.VideoCapture(
    STREAM_URL
)


print(
    "Press s to capture."
)


while True:

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow(
        "Live Stream",
        frame
    )

    key = cv2.waitKey(
        1
    ) & 0xFF

    if key == ord("s"):

        name = datetime.now().strftime(
            "%Y%m%d_%H%M%S.jpg"
        )

        path = os.path.join(
            SAVE_DIR,
            name
        )

        cv2.imwrite(
            path,
            frame
        )

        caption = generate_caption(
            path
        )

        print(
            caption
        )

        speak_text(
            caption
        )

    elif key == ord("q"):

        break


cap.release()

cv2.destroyAllWindows()