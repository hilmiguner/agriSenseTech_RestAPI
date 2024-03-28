from flask import Flask, request
from hidden_constants import serverIP

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Merhaba Dünya!'

@app.route("/send_data")
def send_data():
    data = request.args.get("data")
    return f"Your data is {data}"

if __name__ == '__main__':
    app.run(host=serverIP, debug=True)
