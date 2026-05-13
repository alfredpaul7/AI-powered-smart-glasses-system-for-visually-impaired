import requests
import base64

from config import (
    OLLAMA_URL,
    MODEL_NAME,
    PROMPT
)


def generate_caption(
    image_path
):

    with open(
        image_path,
        "rb"
    ) as img:

        encoded = (
            base64.b64encode(
                img.read()
            ).decode("utf-8")
        )

    payload = {

        "model":
        MODEL_NAME,

        "prompt":
        PROMPT,

        "images":
        [encoded],

        "stream":
        False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    if response.status_code == 200:

        return response.json()[
            "response"
        ]

    return (
        "Unable to describe."
    )