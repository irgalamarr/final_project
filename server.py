from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "No text provided for analysis."


    response = emotion_detector(text_to_analyze)
    dominant_emotion = response.get('dominant_emotion')
    if not dominant_emotion:
        return "Invalid input or unable to determine emotion. Try again."

    # Formatted response
    return f"For the given statement, the system response is " \
           f"'anger': {response['anger']}, 'disgust': {response['disgust']}, " \
           f"'fear': {response['fear']}, 'joy': {response['joy']} and " \
           f"'sadness': {response['sadness']}. The dominant emotion is {dominant_emotion}."


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

