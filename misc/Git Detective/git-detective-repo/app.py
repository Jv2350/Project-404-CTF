from flask import Flask, jsonify
import config

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok", "version": config.APP_VERSION})

@app.route('/metrics')
def metrics():
    return jsonify({"cpu": 45.2, "memory": 67.8, "disk": 23.1})

if __name__ == '__main__':
    app.run(debug=config.DEBUG)
