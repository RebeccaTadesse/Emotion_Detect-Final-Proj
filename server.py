''' This is the server file for the deployment of the Emotion Detection 
Web App using FLask. It encaplsulates the necessary CRUD functions 
for this web app.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_analyzer():
    # Extract the text to be analyzed
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text into the emotion_detector function and save to response
    response = emotion_detector(text_to_analyze)
    # Store each emotion score for the given text as well as the dominant emotion
    a_score = response['anger']
    d_score = response['disgust']
    f_score = response['fear']
    j_score = response['joy']
    s_score = response['sadness']
    dom_emotion = response['dominant_emotion']
    if dom_emotion is None:
        # This occurs if field is blank. If so, return error message
        return "Invalid text! Please try again!"
    # Return an f-string with the final statement
    return f"For the given statement, the system response is \
    'anger': {a_score}, 'disgust': {d_score}, 'fear': {f_score}, \
    'joy': {j_score} and 'sadness': {s_score}. The dominant emotion is \
    {dom_emotion}."

@app.route("/")
def render_index_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



