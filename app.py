from flask import Flask, request, jsonify, render_template
import requests
import time

from dotenv import load_dotenv
import os

load_dotenv()

# Access environment variables
# OpenAI API key (Note: It's best to keep API keys secure and not hardcode them)
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')  # Render the 'index.html' template

# Define the route for the chat endpoint, which accepts POST requests
@app.route('/chat', methods=["POST"])
def chat():
    # Get the user's message from the JSON payload of the request
    user_input = request.json.get('message')
    print(f"Received message: {user_input}")  # Debugging statement to print the received message

    # Get the response from GPT-3
    response = get_gpt_response(user_input)
    print(f"GPT-3 response: {response}")  # Debugging statement to print the GPT-3 response

    # Return the GPT-3 response as a JSON object
    return jsonify({'response': response})

def get_gpt_response(user_input, retry_count=3):
    # Set up the headers for the API request
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    # Set up the data for the API request
    data = {
        'model': 'gpt-3.5-turbo-16k',  # Use a current model
        'messages': [{'role': 'user', 'content': user_input}],  # User's input message
        'max_tokens': 300  # Limit the response length
    }
    for attempt in range(retry_count):
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json={})

        if response.status_code == 200:
            try:
                # Return the content of the first choice in the response
                return response.json()['choices'][0]['message']['content']
            except (KeyError, IndexError) as e:
                print(f"Error parsing response JSON: {e}")  # Print the error
                print(f"Response JSON: {response.json()}")  # Print the full response JSON
                return "An error occurred while processing the response from OpenAI."
        elif response.status_code == 429:
            # Handle rate limiting errors
            print(f"Request to OpenAI failed with status code: {response.status_code}")
            print(f"Response: {response.text}")
            if attempt < retry_count - 1:
                print("Retrying...")
                time.sleep(2 ** attempt)  # Exponential backoff before retrying
            else:
                return "You have exceeded your current quota. Please check your plan and billing details."
        else:
            # Handle other errors
            print(f"Request to OpenAI failed with status code: {response.status_code}")
            print(f"Response: {response.text}")
            return "An error occurred while communicating with OpenAI."

# Run the Flask application
if __name__ == '__main__':
    app.run(port=5000, debug=True) # Run the app in debug mode
    