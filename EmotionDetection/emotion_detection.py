''' This file contains the emotion_detector function to be used by the server
    later. It uses Watson Embedded  NLP libraries, notably the Emotion Predict
    function
'''
import json
import requests
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    formatted_response = json.loads(response.text)  # Format text as a dictionary
    # Extract emotion scores and storing them
    if response.status_code == 200:     # If text field is not blank, proceed with detection
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        # To get the dominant emotion, use the max() method and store it in a variable
        dominant_emotion_score = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)
        # Loop through the dictionary to find the key value with the highest
        for em in formatted_response['emotionPredictions'][0]['emotion']:
            if formatted_response['emotionPredictions'][0]['emotion'][em] == dominant_emotion_score:
                dominant_emotion_name = em
    
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion_name
        }
    elif response.status_code == 400:       # If text field is blank return dictionary with None values
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }