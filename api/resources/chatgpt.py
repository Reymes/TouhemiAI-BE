from flask import request
from flask_restful import Resource

from services.openai_service import get_response
from resources.errors import InternalServerError


class chatGPT(Resource):
    def post(self):
        try:
            message = request.json.get("message")
            response = get_response(message)
            return {"response": response}, 200
        except Exception as exc:
            raise InternalServerError from exc
