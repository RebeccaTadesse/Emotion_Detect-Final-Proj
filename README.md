# Repository for final project
## Overview
Welcome! This was the final project for the IBM Course, "Developing AI Applications with Python and Flask.
### Provided Scenario
You have been hired as a software engineer by an e-commerce company to create an AI-based web app that performs analytics on customer feedback for their signature products. To accomplish this requirement, you will create an Emotion Detection system that processes feedback provided by the customer in text format and deciphers the associated emotion expressed.

This project uses Embeddable Watson AI Libraries, specifically the Watson NLP Library. As this project was completed using the Skills Network Labs Cloud IDE, these libraries were pre-installed. You can find the library at the following link: https://www.ibm.com/products/natural-language-processing?utm_source=ibm_developer&utm_content=in_content_link&utm_id=articles_watson-libraries-embeddable-ai-that-works-for-you&cm_sp=ibmdev-_-developer-articles-_-product


### NLP Library
The NLP library includes functions for sentiment analysis, emotion detection, text classification, language detection, etc. among others. The speech-to-text library contains functions that perform the transcription service and generates written text from spoken audio. The text-to-speech library generates natural sounding audio from written text. 
For this project, we use the  Emotion Predict function of the Watson NLP Library.

### Emotion Predict
Emotion detection extends the concept of sentiment analysis by extracting the finer emotions, like joy, sadness, anger, and so on, from statements rather than the simple polarity that sentiment analysis provides. This makes emotion detection a very important branch of study and businesses use such systems widely for their AI based recommendation systems, automated chat bots, and so on.

## Project
### Application
The application is packaged as EmotionDetection. It contains the __init__ file and the main file for our emotion detect function (emotion_detector). emotion_detector takes the input from the interface (the user) and returns a dictionary of each emotion and its score, as well as the dominant emotion, i.e:
`{
'anger': anger_score,
'disgust': disgust_score,
'fear': fear_score,
'joy': joy_score,
'sadness': sadness_score,
'dominant_emotion': '<name of the dominant emotion>'
}`

If the user doesn't input anything, the user will be prompted to not leave the field blank.

### Unit Tests
Unit testing was conducted on the sentiment_analyzer in the file test_emotion_detection.py. Here, we test if emotion_detector returns the correct dominant emotion.

### Deployment
To deploy the app, index.html in the templates folder and mywebscript.js in the static folder were provided for the interface of this project.
When interacting with the html interface, clicking the "Run Sentiment Analysis" button calls the javascript file, which in turn executes a GET request and takes the text provided by the user as input.This text, saved in a variable named textToAnalyze, is then passed on to the server file to be sent to the application. The main task in this project, however, was the completion of server.py.
server.py initiates the application of sentiment analysis to be executed over the Flask channel and deployed on localhost:5000

### Run
Make sure you have Python and Flask installed.
Fork and clone this repository, and navigate to the project directory using the cd command.
Open the Python terminal in the shell and call server.py
If using Cloud Skills IDE, navigate to Skills Network Toolbox and launch application
Make sure your port is 5000 and launch either in brower or in a new window in the IDE.

### Notes
Static code analysis was performed to ensure that the code for sentiment_analysis.py and server.py follow PEP8 guidelines

### Topics covered
- Emotion Detection
- Watson NLP Library
- Packages
- Unit Tesing
- Flask
- Error Handling
- Pylint
