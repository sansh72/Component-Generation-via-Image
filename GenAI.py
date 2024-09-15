import requests
import json
import os
import base64
import cv2
from openai import OpenAI

# OpenAI API Key
api_key = "Your open AI key "
API_TOKEN = 'Your figma API key '
os.environ['OPENAI_API_KEY'] = api_key
FILE_KEY = 'Your figma file key '

# OpenAI client initialization
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Reading file contents
with open('python/response.txt', 'r') as file:
    file_contents = file.read()

with open('backend/clicks.csv', 'r') as file:
    csv_contents = file.read()

# Figma API request headers
headers = {'X-Figma-Token': API_TOKEN}
url = f'https://api.figma.com/v1/files/{FILE_KEY}'

# Requesting Figma file data
response = requests.get(url, headers=headers)
if response.status_code == 200:
    figma_file_data = response.json()
    nodes = figma_file_data.get('document', {}).get('children', [])
    components = []

    # Save Figma data to JSON
    with open('figma_file_data.json', 'w') as json_file:
        json.dump(figma_file_data, json_file, indent=2)

# Function to encode the image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Encode the image
image_path = "python/GenAI.png"
base64_image = encode_image(image_path)

# Conversation state and inputs
previous_response = ""
user_input = ""
conversation_continues = True
conversation_state = {
    'previous_responses': [],
    'current_context': None
}

# Chat interaction loop
while conversation_continues:
    user_input = input("Enter your prompt: ") 

    if user_input.lower() == 'exit':
        conversation_continues = False
        print("Exiting...")
        break

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Prepare request payload
    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": f"{user_input}"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ],
        "max_tokens": 300
    }

    # Send POST request to OpenAI API
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        if 'choices' in data and len(data['choices']) > 0:
            text_response = data['choices'][0]['message']['content']
            print(text_response)
            
            # Save response to file
            with open("python/response.txt", 'a') as file:
                file.write("> " + user_input + "\n")
                file.write("> " + text_response + "\n\n")
        else:
            print("No valid response found.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
