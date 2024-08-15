from application.models.model import db, CourseContent
from flask import jsonify, request
from flask_restful import Resource
from .genAI import generate_summary
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def YouTubeTranscript(video_id):
    '''
        Fetches the transcript of the video with the given video_id
        "video_id is the video id of the youtube video example: 'dQw4w9WgXcQ' 
        in a link like https://www.youtube.com/watch?v=dQw4w9WgXcQ
    '''
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    formatter = TextFormatter()
    return formatter.format_transcript(transcript)

class LectureSummaryAPI(Resource):
    def get(self, weeknumber, id):
        content = CourseContent.query.filter_by(week=weeknumber, id=id).first()
        if not content:
            return {"message": "No transcript found for this week"}, 404
        video_id=content.link
        transcript=YouTubeTranscript(video_id)
        return {'summary' : generate_summary(transcript)}, 200
    
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
