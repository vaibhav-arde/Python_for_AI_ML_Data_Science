# Import necessary libraries from Flask and OpenAI
from flask import Flask, request, jsonify, render_template
import openai

# Initialize the Flask application
app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = 'your_openai_api_key'  # Replace 'your_openai_api_key'

@app.route("/")
def home():
    # Render the 'index.html' template when the home page is accessed
    return render_template('text_to_image.html')

# Define the route for the generate_image endpoint, which accepts POST requests
@app.route('/generate_image', methods=['POST'])
def generate_image():

    # Get the 'prompt' from the JSON payload of the POST request
    prompt = request.json.get('prompt')

    # Use the OpenAI API to generate an image based on the prompt
    response = openai.Image.create(
        prompt=prompt,  # The text prompt for generating the image
        n=1,            # Number of images to generate
        size="512x512"  # Size of the generated image
    )
    image_url = response['data'][0]['url']

    # Return the image URL as a JSON response
    return jsonify({'image_url': image_url})

# Run the Flask application
if __name__ == "__main__":
    # Start the Flask app in debug mode, which provides detailed error messages and auto-reloads
    app.run(debug=True)
