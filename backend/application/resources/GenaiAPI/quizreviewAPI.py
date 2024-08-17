from application.models.model import Quiz
from flask_restful import Resource
from flask import jsonify,request
from genAI import quiz_review

class QuizReview(Resource):
    def get(self):
        quiz_questions = Quiz.query.all()

        if not quiz_questions:
            return {'message' : "Some error occured"}, 404
        
        response = {'response': quiz_review(quiz_records=quiz_questions)}, 200

    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass
