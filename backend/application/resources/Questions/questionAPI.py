from flask_restful import Resource
from flask import request, jsonify

from application.models.model import db, Questions

class QuestionAPI(Resource):
    def get(self, week=None):
        questions = Questions.query.filter_by(weeknumber=week)
        return jsonify([question.serialize() for question in questions])

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
