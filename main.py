from flask import Flask, jsonify
from domain.model.model import Ping
from domain.data.PingReader import fetch_ping_data

app = Flask(__name__)

@app.route('/')
def hello():
    
    single_value = fetch_ping_data()
    ping_responde = Ping(seconds=300, byte=1500, server=single_value)
    return jsonify(ping_responde.__dict__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)