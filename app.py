from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
# Replace with your actual site URL
CORS(app, resources={r"/*": {"origins": "https://cerulean-cucurucho-7d3c7a.netlify.app"}})


@app.route('/receive_message', methods=['POST'])
def receive_message():
    data = request.get_json()
    
    # Extract additional fields from the incoming data
    number = data.get('number', 'No Number')
    email = data.get('email', 'No Email')
    prefix = data.get('prefix', 'No Prefix')
    
    # Generate a timestamp for when the message is received
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Prepare the data to be stored, including the additional fields and timestamp
    message_data = {
        "title": data.get('title', 'No Title'),
        "subject": data.get('subject', 'No Subject'),
        "message": data.get('message', 'No Message'),
        "number": number,
        "email": email,
        "prefix": prefix,
        "timestamp": timestamp
    }
    
    # Check if the file exists and read its content
    if os.path.exists('messages.json'):
        with open('messages.json', 'r') as f:
            messages = json.load(f)
    else:
        messages = []
    
    # Append the new message to the list of messages
    messages.append(message_data)
    
    # Write the updated list back to the file
    with open('messages.json', 'w') as f:
        json.dump(messages, f)
    
    print(f"Data received and stored: {message_data}")
    
    return jsonify({"status": "success", "message": "Data received and stored"}), 200

if __name__ == '__main__':
    app.run(debug=True)
