from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Merhaba Dünya!'

@app.route("/send_data")
def send_data():
    data = request.args.get("data")
    return f"Your data is {data}"

if __name__ == '__main__':
    app.run(host="145.239.134.25", debug=True)
