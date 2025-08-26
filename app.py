
from flask import Flask, render_template, send_from_directory, jsonify
import os
import json

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game-data')
def game_data():
    data_path = os.path.join(app.static_folder, 'game_data.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    # Use 0.0.0.0 if you want to access from another device on your LAN
    app.run(host='127.0.0.1', port=5000, debug=True)
