from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS
from collections import OrderedDict
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_info():
    response_data = OrderedDict([
        ("email", "nmurigi@kabarak.ac.ke"),
        ("current_datetime", datetime.utcnow().isoformat() + "Z"),
        ("github_url", "https://github.com/StanleyMurigi/HNG-12")
        ])

    return app.response_class(
        response=json.dumps(response_data),  # Use json.dumps() to control order
        status=200,
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(debug=True)
