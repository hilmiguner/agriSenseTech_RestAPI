from flask import Flask, request, jsonify
from hidden_constants import serverIP
from database import insertUserMessage

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Merhaba Dünya!'

@app.route("/send_data")
def send_data():
    data = request.args.get("data")
    return f"Your data is {data}"

@app.route("/insert_user_message", methods=["POST"])
def insert_user_message():
    data = request.json

    try:
        respond = insertUserMessage(data["title"], data["message"], data["name"], data["email"], data["datetime"], data["fb_local_id"])
        return jsonify(respond)
    except Exception as err:
        return jsonify({ 'status': 400, 'error': str(err) })

if __name__ == '__main__':
    app.run(host=serverIP, debug=True)
