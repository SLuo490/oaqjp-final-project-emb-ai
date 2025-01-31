import requests
import json

session = requests.Session()

def emotion_detector(text_to_analyse):
    response = session.post(
        'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
        headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        json={ "raw_document": { "text": text_to_analyse } }
    )

    format_response = json.loads(response.text)

    if response.status_code == 200:
        anger_score = format_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = format_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = format_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = format_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = format_response['emotionPredictions'][0]['emotion']['sadness']

        data = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
        }
        data['dominant_emotion'] = max(data, key=data.get)
    else:
        data =  {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    return data