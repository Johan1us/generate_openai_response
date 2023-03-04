# Test local: functions-framework --target generate_openai_response --debug

import os
import json
from firebase_admin import credentials, firestore, initialize_app
import openai
from functions_framework import http

# Initialize Firestore client
cred = credentials.Certificate(os.environ.get("FIRESTORE_CREDS_JSON"))
initialize_app(cred)
db = firestore.client()

# Initialize OpenAI client
openai.api_key = os.environ.get("OPENAI_API_KEY")


@http
def generate_openai_response(request):
    request_json = request.get_json()
    tag = request_json['fulfillmentInfo']['tag']
    user_message = request_json['text']

    collection, document = tag.split(" - ")

    firestore_doc = db.collection(collection).document(document).get().to_dict()

    prompt = firestore_doc['prompt'].replace("<<QUERY>>", user_message)

    settings = firestore_doc['settings']

    response = openai.Completion.create(
        engine=settings['model'],
        prompt=prompt,
        temperature=settings['temperature'],
        max_tokens=settings['max_tokens'],
        top_p=settings['top_p'],
        frequency_penalty=settings['frequency_penalty'],
        presence_penalty=settings['presence_penalty']
    )

    response_text = response.choices[0].text.strip()

    response_json = {
        "fulfillmentResponse": {
            "messages": [{"text": {"text": [response_text]}}]
        }
    }

    return json.dumps(response_json)
