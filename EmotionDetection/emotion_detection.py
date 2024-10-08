import requests
import json
def emotion_detection(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock", 
        "Content-Type": "application/json"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, headers=headers, json = input_json)
        response.raise_for_status()
        emotion_data = response.json()
        print("Emotion Data: ", emotion_data)

        # Ensure the expected structure
        if "emotionPredictions" not in emotion_data or not emotion_data["emotionPredictions"]:
            print("No emotion predictions found in response.")
            return None

        # Extracting emotions from the response
        emotions = emotion_data["emotionPredictions"][0]["emotion"]

        # Add dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion

        return emotions

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None