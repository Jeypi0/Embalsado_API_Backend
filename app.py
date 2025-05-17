from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '').lower()

    if user_message == 'hi':
        response = 'hello'
    else:
        response = "I don't understand."

    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(debug=True)
