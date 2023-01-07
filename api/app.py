import os

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources.errors import errors
from resources.routes import initialize_routes


app = Flask(__name__)
app.config.from_object(os.getenv("APP_SETTINGS"))

cors = CORS(app, supports_credentials=True)
api = Api(app, errors=errors)


initialize_routes(api)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6010)
