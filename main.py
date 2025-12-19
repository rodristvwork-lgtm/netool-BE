from flask import Flask, jsonify
from domain.model.Ping import Ping
from read.read.PingDataRead import read_ping_data

app = Flask(__name__)

@app.route('/')
def hello():
    
    data = read_ping_data()
    print(data)
    ping_responde = Ping(seconds=300, byte=1500, server="Ebay")
    return jsonify(ping_responde.__dict__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  