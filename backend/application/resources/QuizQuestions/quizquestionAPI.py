from flask_restful import Resource
from flask import request, jsonify

from application.models.model import db, Quiz

class QuizQuestionAPI(Resource):
    def get(self, week=None):
        questions = Quiz.query.filter_by(number=week)
        return jsonify([question.serialize() for question in questions])

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
