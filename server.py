"""
server.py: A Flask application that detects emotions from text.
The application provides an endpoint '/emotionDetector' that takes 
text input and returns the detected emotions and dominant emotion.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detection

app = Flask(__name__)

@app.route("/emotionDetector")
def em_detector():
    """
    Analyse client request text for emotions and return a string 
    including emotion scores and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detection(text_to_analyze)

    # Check for a valid response
    if response is None or response['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again."})

    # Use the response to format the output string
    output = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return jsonify({"response": output})

@app.route("/")
def render_index_page():
    """
    Render the homepage template and return a string which is its HTML.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
