from flask_restful import Resource
from flask import request, jsonify

from application.models.model import db, CourseContent

class VideoContentAPI(Resource):
    def get(self, id=None):
        coursecontent = CourseContent.query.filter_by(id=id).first()
        return jsonify(coursecontent.serialize())
    
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass