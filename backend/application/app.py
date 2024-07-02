import os

from flask import Flask,request,jsonify, send_file
from flask_cors import CORS

from .Config.config import Config
from .models.model import db, CourseContent, Questions
from .resources.Coursecontent.coursecontentAPI import CourseContentAPI
from .resources.Questions.questionAPI import QuestionAPI


current_dir = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

CORS(app)
CORS(
    app,
    resources={
        r"/*": {
            "origins": "http://localhost:5173",
            "supports_credentials": True,
            "Access-Control-Allow-Credentials": True,
        }
    },
)
    

# API Endpoints

# Course Content
app.add_url_rule("/api/coursecontent/<int:week>", view_func=CourseContentAPI.as_view("coursecontent"), methods=["GET"])

# Questions
app.add_url_rule("/api/questions/<int:week>", view_func=QuestionAPI.as_view("questions"), methods=["GET"])


# check for database and create if not exists
with app.app_context():
    db.create_all()