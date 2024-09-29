# server.py
from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    """
    Endpoint to detect emotions from the provided text.

    Returns:
        JSON response containing the emotion analysis results or an error message.
    """
    text = request.json.get('text', '')
    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. The dominant emotion is "
        f"{result['dominant_emotion']}."
    )

    return jsonify(response_message)

if __name__ == '__main__':
    """
    Main entry point for the Flask application.
    Runs the application in debug mode.
    """
    app.run(debug=True)
