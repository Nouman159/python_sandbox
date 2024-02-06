import base64
from flask import Flask 
import requests
from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes by passing the app to CORS

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "./tn_1.png"
# api_key = "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"
api_key = "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"

# Getting the base64 string
from openai import OpenAI
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful hockey commentator"},
    {"role": "user", "content": "What is Pakistan national game?"},
    {"role": "assistant", "content": "Hockey"},
    {"role": "user", "content": "Where was last hockey WC played?"}
  ]
)

print(response.json())

@app.route('/')
def home():
    return response.json()
    
