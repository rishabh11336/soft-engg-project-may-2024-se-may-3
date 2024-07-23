from application.models.model import db, ProgrammingAssignments
from flask import jsonify, request
from flask_restful import Resource
from .genAI import explain_programming_assignment


class ExplainProgrammingQuestionAPI(Resource):
    def get(self, id):
        question = ProgrammingAssignments.query.filter_by(id=id).first()
        explanation = explain_programming_assignment(question.question)
        return {'explanation': explanation}, 200

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass