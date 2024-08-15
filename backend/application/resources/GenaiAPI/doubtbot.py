from flask import jsonify,request
from flask_restful import Resource
from .genAI import doubtbot
from application.models.model import db,CourseContent 
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

class doubtbotAPI(Resource):
    def get(self,video_id, user_query):
        coursecontent = CourseContent.query.filter_by(id = video_id).first()
        transcript_raw = YouTubeTranscriptApi.get_transcript(coursecontent.link)
        formatter = TextFormatter()
        transcript = formatter.format_transcript(transcript_raw)

        if not coursecontent:
            return {'message': 'Some error occured'}
 
        return {'response':doubtbot(coursecontent.id,transcript, user_query)},200
        
        
    
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
    
