import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "status": "online",
        "service": "Diskwala Resolver"
    })


@app.get("/health")
def health():
    return "OK", 200


@app.route("/resolve", methods=["GET", "POST"])
def resolve():
    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        url = data.get("url")
    else:
        url = request.args.get("url")

    if not url:
        return jsonify({
            "status": "error",
            "message": "Missing url"
        }), 400

    if "diskwala.com" not in url:
        return jsonify({
            "status": "error",
            "message": "Only Diskwala URLs are supported"
        }), 400

    return jsonify({
        "status": "received",
        "url": url,
        "message": "Diskwala link received successfully"
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
