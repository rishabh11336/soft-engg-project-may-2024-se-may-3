from application.models.model import db, CourseContent
from flask import jsonify, request
from flask_restful import Resource
from .genAI import generate_summary


class LectureSummaryAPI(Resource):
    def get(self, weeknumber, id):
        content = CourseContent.query.filter_by(week=weeknumber, id=id).first()
        if not content:
            return {"message": "No transcript found for this week"}, 404
        return {'summary' : generate_summary(content.transcript)}, 200
    
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass