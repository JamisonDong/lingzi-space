#!/usr/bin/env python3
from flask import Flask, jsonify, Response
from datetime import datetime
import json
import os
from flask_cors import CORS

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(ROOT_DIR, "frontend")
STATE_FILE = os.path.join(ROOT_DIR, "state.json")
app = Flask(__name__)
CORS(app)

DEFAULT_STATE = {
    "state": "idle",
    "detail": "铃子正在待命...",
    "progress": 0,
    "updated_at": datetime.now().isoformat()
}

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return dict(DEFAULT_STATE)

def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

if not os.path.exists(STATE_FILE):
    save_state(DEFAULT_STATE)

@app.route("/")
def index():
    index_path = os.path.join(FRONTEND_DIR, "index.html")
    with open(index_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    return Response(html_content, mimetype='text/html')

@app.route("/status")
def get_status():
    return jsonify(load_state())

@app.route("/health")
def health():
    return jsonify({"status": "ok", "timestamp": datetime.now().isoformat()})

if __name__ == "__main__":
    print("Lingzi Star Office Backend v2 listening on http://0.0.0.0:18791")
    app.run(host="0.0.0.0", port=18791, debug=False)
