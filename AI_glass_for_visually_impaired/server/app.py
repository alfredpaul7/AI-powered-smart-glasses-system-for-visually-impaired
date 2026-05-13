from flask import (
    Flask,
    request,
    jsonify
)

import os

from moondream_inference import (
    generate_caption
)


app = Flask(__name__)


os.makedirs(
    "uploads",
    exist_ok=True
)


@app.route(
    "/analyze",
    methods=["POST"]
)
def analyze():

    file = request.files[
        "image"
    ]

    path = os.path.join(
        "uploads",
        file.filename
    )

    file.save(
        path
    )

    caption = generate_caption(
        path
    )

    return jsonify({

        "caption":
        caption

    })


if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000
    )