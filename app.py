from flask import Flask, jsonify, request
from localragAPI import chatBotFun
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chatbot', methods=['POST'])
def hello_world():
    data = request.get_json()
    userMessage = data.get('message')
    print("request message input: \n"+userMessage)
    response = chatBotFun(userMessage)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)