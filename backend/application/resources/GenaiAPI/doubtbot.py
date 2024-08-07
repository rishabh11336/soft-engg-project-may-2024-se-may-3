from flask import jsonify,request
from flask_restful import Resource
from .genAI import doubtbot
from application.models.model import db,CourseContent 

class doubtbotAPI(Resource):
    def get(self,video_id):
        coursecontent = CourseContent.query.filter_by(id = video_id).first()
        transcript = coursecontent.transcript
        if not coursecontent:
            return {'message': 'Some error occured'}
        return {'response':doubtbot(coursecontent.id,transcript)},200
        
    
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass