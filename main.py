    from flask import Flask 
app= Flask(__name__)
# apiKey = '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'

import base64
import requests

# OpenAI API Key
# api_key = "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"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "./tn_1.png"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What’s in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())

@app.route('/')
def home():
    return response.json()
    


# @app.route('/post/video', methods=['POST'])
# def process_video():
#     try:
#         video_file = request.files['video']
        
#         # Process the video file as needed
#         # For example, you can save it to the server
#         video_file.save('./video.mp4')

#         # Your additional processing logic here
        
#         return {"message": "Video received and processed successfully"}, 200

#     except Exception as e:
#         print('Hello error')
#         return {"error": "Internal server error"}, 500

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)


# from flask import Flask 
# app= Flask(__name__)
# import base64
# import requests

# # OpenAI API Key
# from openai import OpenAI
# # api_key = "your-api-key"
# openai = OpenAI(api_key=api_key)


# response = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#     {"role": "user", "content": "Where was it played?"}
 
#   ]
# )

