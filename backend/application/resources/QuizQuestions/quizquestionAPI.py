from flask_restful import Resource
from flask import jsonify
from application.models.model import Quiz

class QuizQuestionAPI(Resource):
    def get(self):
        questions = Quiz.query.all()
        return jsonify([question.serialize() for question in questions])

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
