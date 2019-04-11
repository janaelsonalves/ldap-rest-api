from flask import Flask
from flask_cors import CORS

from app.views import api

app = Flask(__name__)
CORS("/api/*", app)

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)