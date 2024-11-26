import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'error': 'No text provided for analysis.'
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=input_json, headers=headers)
    
    # Check if the response is successful
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'error': 'Bad request. Please provide valid input.'
        }

    formatted_response = response.json()
    emotion_predictions = formatted_response.get('emotionPredictions', [])

    if not emotion_predictions:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'error': 'No emotion predictions found in the response.'
        }

    emotion = emotion_predictions[0].get('emotion', {})
    if not emotion:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'error': 'No emotion scores found in the response.'
        }

    dominant_emotion = max(emotion, key=emotion.get)

    result = {
        'anger': emotion.get('anger', 0),
        'disgust': emotion.get('disgust', 0),
        'fear': emotion.get('fear', 0),
        'joy': emotion.get('joy', 0),
        'sadness': emotion.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }
    return result
