from flask import Flask, jsonify
from domain.model.model import Ping

app = Flask(__name__)

@app.route('/')
def hello():
    ping_responde = Ping(seconds=300, byte=1500, server="ebay.com")
    return jsonify(ping_responde.__dict__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    