from application.models.model import db, Questions
from flask import jsonify, request
from flask_restful import Resource
from .genAI import explain_theory_question


class ExplainTheoryQuestionAPI(Resource):
    def get(self, number):
        question = Questions.query.filter_by(number=number).first()
        explanation = explain_theory_question(question.question, question.code_snippet)
        return {'explanation': explanation}, 200

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass