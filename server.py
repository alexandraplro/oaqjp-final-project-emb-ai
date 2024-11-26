""" Emotion Detector Flask Application 
This module creates a Flask application to detect emotions in text. 
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    """ 
    Endpoint to analyze text and return emotion scores. 
    Parameters: None (inputs obtained via request.args) 
    Returns: str: A formatted string with emotion scores as well as the dominant emotion. 
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger = response.get('anger', 0)
    disgust = response.get('disgust', 0)
    fear = response.get('fear', 0)
    joy = response.get('joy', 0)
    sadness = response.get('sadness', 0)
    dominant_emotion = response.get('dominant_emotion', 'Unknown')

    if dominant_emotion is None:
        return "Invalid text! Please try again."

    return f"For the given statement, the system response is 'anger': {anger}, "\
           f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, "\
           f"and 'sadness': {sadness}. The dominant emotion is <b>{dominant_emotion}</b>."

@app.route("/")
def render_index_page():
    """ 
    Renders the index page from Templates folder. 
    Returns: str: Rendered HTML template for the index page. 
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
