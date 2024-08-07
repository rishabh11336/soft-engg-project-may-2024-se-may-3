from flask_restful import Resource
from flask import request, jsonify

from application.models.model import db, CourseContent

class CourseContentAPI(Resource):
    def get(self, week=None):
        coursecontent = CourseContent.query.filter_by(week=week).all()
        return jsonify([{
            "id": content.id,
            "week": content.week,
            "index": str(content.index),
            "type": content.type,
            "title": content.title,
            "link": content.link } for content in coursecontent])
    
    def post(self):
        pass 

    def put(self):
        pass

    def delete(self):
        pass