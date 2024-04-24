from flask import Blueprint, request, jsonify
import requests
from urllib.parse import quote_plus

GPT_bp = Blueprint('GPT', __name__)

@GPT_bp.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['input']
    #response = call_gpt_api(user_input)
    return jsonify("It works!")

def call_gpt_api(text):
    api_key = 'YOUR_OPENAI_API_KEY'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = {
        "model": "text-davinci-003",  # or any other model
        "prompt": text,
        "max_tokens": 150
    }
    response = requests.post('https://api.openai.com/v1/engines/text-davinci-003/completions', headers=headers, json=data)
    return response.json()