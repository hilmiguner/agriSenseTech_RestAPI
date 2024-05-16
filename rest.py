from flask import Flask, request, jsonify 
from hidden_constants import serverIP
from database import insertUserMessage, getWeeds
import base64

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
    
@app.route("/get_weeds", methods=["POST"])
def get_weeds():
    data = request.json

    try:
        respond = getWeeds(data["fb_local_id"],)
        for id in respond["data"]:
            filename = respond["data"][id]["image_path"]
            with open(f"img_weeds/{data['fb_local_id']}/{filename}", "rb") as file:
                imageData = file.read()
                imageBase64 = base64.b64encode(imageData).decode("utf-8")
            respond["data"][id]["image"] = imageBase64
        return jsonify(respond)
    except Exception as err:
        return jsonify({ 'status': 400, 'error': str(err) })

if __name__ == '__main__':
    app.run(host=serverIP, debug=True)
