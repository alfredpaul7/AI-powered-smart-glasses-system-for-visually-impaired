import pyttsx3


engine = pyttsx3.init()

engine.setProperty(
    "rate",
    160
)


def speak_text(text):

    print(
        "🔊",
        text
    )

    engine.say(
        text
    )

    engine.runAndWait()