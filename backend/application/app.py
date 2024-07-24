import os

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS

from .Config.config import Config
from .models.model import CourseContent, Questions, Submissions, db
from .resources.Coursecontent.coursecontentAPI import CourseContentAPI
from .resources.GASubmission.submissionapi import SubmitAnswerAPI
from .resources.Marks.marks import MarksAllWeeksAPI, MarksSpecificWeekAPI
from .resources.PASubmission.submissionpa import SubmitProgrammingAssignmentAPI
from .resources.ProgrammingAssignments.PAquestionsAPI import \
    ProgrammingAssignmentAPI
from .resources.Questions.questionAPI import QuestionAPI

from .resources.Code.run_code import RunPython
from .resources.Code.run_pa_code import RunProgAssign

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

# Submit GA Answer
app.add_url_rule("/api/gasubmit", view_func=SubmitAnswerAPI.as_view("submit"), methods=["POST"])

# Marks
app.add_url_rule("/api/marks/all", view_func=MarksAllWeeksAPI.as_view("marks_all_weeks"), methods=["GET"])
app.add_url_rule("/api/marks/<int:week>", view_func=MarksSpecificWeekAPI.as_view("marks_specific_week"), methods=["GET"])

# Programming Assignments
app.add_url_rule("/api/programmingassignments/<int:week>", view_func=ProgrammingAssignmentAPI.as_view("programmingassignments"), methods=["GET"])

# Submit PA Answer
app.add_url_rule("/api/pasubmit", view_func=SubmitProgrammingAssignmentAPI.as_view("submit_pa"), methods=["POST"])

app.add_url_rule("/api/run-python", view_func=RunPython.as_view("run_python"), methods=["POST"])
app.add_url_rule("/api/run-pa-code", view_func=RunProgAssign.as_view("run_pa_code"), methods=["POST"])


# check for database and create if not exists
with app.app_context():
    db.create_all()