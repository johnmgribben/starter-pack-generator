import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

@app.route("/search")
def search():
    query    = request.args.get("query", "")
    per_page = request.args.get("per_page", 20)
    locale   = request.args.get("locale", "en-US")
    if not query:
        return jsonify({"error": "No query provided"}), 400
    try:
        r = requests.get(
            "https://api.pexels.com/v1/search",
            headers={"Authorization": PEXELS_API_KEY},
            params={"query": query, "per_page": per_page, "orientation": "landscape", "locale": locale},
            timeout=10
        )
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/claude", methods=["POST"])
def claude():
    try:
        data = request.get_json()
        r = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json=data,
            timeout=60
        )
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY")

@app.route("/search")
def search():
    query   = request.args.get("query", "")
    per_page = request.args.get("per_page", 20)
    locale  = request.args.get("locale", "en-US")

    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        r = requests.get(
            "https://api.pexels.com/v1/search",
            headers={"Authorization": PEXELS_API_KEY},
            params={"query": query, "per_page": per_page, "orientation": "landscape", "locale": locale},
            timeout=10
        )
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
