from application.models.model import Quiz
from flask_restful import Resource
from flask import jsonify,request
from .genAI import quiz_review

class QuizReview(Resource):
    def get(self):
        quiz_questions = Quiz.query.all()

        if not quiz_questions:
            return {'message': "No quiz questions found"}, 404
        
        feedback = quiz_review(quiz_records=quiz_questions)
        return jsonify({'response': feedback})

    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass
