from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    feedback = request.form["feedback"]

    result = emotion_detector(feedback)

    if result is None:
        return render_template(
            "index.html",
            error="Unable to analyze text."
        )

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)