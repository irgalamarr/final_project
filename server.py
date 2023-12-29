"""
This module is a Flask application for detecting emotions in text.
It uses the EmotionDetection package to analyze text and determine the dominant emotion.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    This route receives text via query parameters and returns the dominant emotion
    and the emotion scores for anger, disgust, fear, joy, and sadness.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response.get('dominant_emotion')
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Formatted response
    return f"For the given statement, the system response is " \
           f"'anger': {response['anger']}, 'disgust': {response['disgust']}, " \
           f"'fear': {response['fear']}, 'joy': {response['joy']} and " \
           f"'sadness': {response['sadness']}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """
    This route renders the main index page of the web application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
