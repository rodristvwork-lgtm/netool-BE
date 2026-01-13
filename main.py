from flask import Flask, jsonify
from domain.model.Ping import Ping
from read.service.PingServiceRead import findAllPingResults

app = Flask(__name__)

@app.route('/')
def hello():
    
    data = findAllPingResults()
    return jsonify("to update ping class") # -> return jsonify(ping_responde.__dict__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  