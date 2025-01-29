from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_info():
    return jsonify({
        "email": "nmurigi@kabarak.ac.ke",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https"
        })

if __name__ == '__main__':
    app.run(debug=True)
