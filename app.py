from flask import Flask, request, jsonify, send_from_directory
from chatBot import Conversation  

app = Flask(__name__)

# Initialize the Conversation class
conversation_obj = Conversation()

@app.route('/conversation', methods=['POST'])
def conversation_controller():
    if request.is_json:
        # Call the post method from Conversation class
        return conversation_obj.post()
    else:
        return jsonify({"error": "Unsupported Media Type"}), 415

@app.route('/')
def serve_html():
    return send_from_directory('', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)


