import os

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS

from application.resources.Code.run_pa_code import RunProgAssign
from application.resources.Marks.programming_marks import GetProgrammingAssignmentMarksAPI

from .Config.config import Config
from .models.model import CourseContent, Questions, Submissions, db
from .resources.Coursecontent.coursecontentAPI import CourseContentAPI
from .resources.GASubmission.submissionapi import SubmitAnswerAPI
from .resources.Marks.marks import MarksAllWeeksAPI, MarksSpecificWeekAPI
from .resources.PASubmission.submissionpa import SubmitProgrammingAssignmentAPI
from .resources.ProgrammingAssignments.PAquestionsAPI import ProgrammingAssignmentAPI
from .resources.Questions.questionAPI import QuestionAPI
from .resources.GenaiAPI.lectureSummaryAPI import LectureSummaryAPI
from .resources.GenaiAPI.explainTheoryQuestionAPI import ExplainTheoryQuestionAPI
from .resources.GenaiAPI.explainProgrammingQuestionAPI import ExplainProgrammingQuestionAPI
from .resources.GenaiAPI.doubtbot import doubtbotAPI
from .resources.Coursecontent.videocontentAPI import VideoContentAPI
from .resources.QuizQuestions.quizquestionAPI import QuizQuestionAPI
from .resources.Code.run_code import RunPython
from .resources.GenaiAPI.quizreviewAPI import QuizReview
from .resources.GenaiAPI.programmingFeedBack import ProgrammingFeeback

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

# Video & Transcript Content
app.add_url_rule("/api/videocontent/<int:id>", view_func=VideoContentAPI.as_view("videocontent"), methods=["GET"])

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

# Programming marks
app.add_url_rule("/api/programmingassignments/<int:weeknumber>/marks/<int:assignment_id>",
                 view_func=GetProgrammingAssignmentMarksAPI.as_view("get_programming_assignment_marks"),
                 methods=["GET"])

# Quiz Questions
# app.add_url_rule('/api/quizquestion/<int:week>',view_func=QuizQuestionAPI.as_view('quizquestion'),methods = ["GET"])
app.add_url_rule('/api/quizquestion', view_func=QuizQuestionAPI.as_view('quizquestion'), methods=["GET"])

# GenAI API
# transcript summary
app.add_url_rule("/api/genai/summary/<int:weeknumber>/<string:id>", view_func=LectureSummaryAPI.as_view("genai_summary"), methods=["GET"])

# explain theory question
app.add_url_rule("/api/genai/explaintheory/<int:number>", view_func=ExplainTheoryQuestionAPI.as_view("genai_explaintheory"), methods=["GET"])

# explain programming question
app.add_url_rule("/api/genai/explainprogramming/<int:id>", view_func=ExplainProgrammingQuestionAPI.as_view("genai_explainprogramming"), methods=["GET"])

# doubtbot api
app.add_url_rule('/api/genai/doubtbot/<int:video_id>/<string:user_query>',view_func=doubtbotAPI.as_view('genai_doubtbot'), methods = ['GET'])

# Quiz Review API
app.add_url_rule('/api/genai/quizreview',view_func=QuizReview.as_view('quiz_question'),methods = ['GET'])

# Programming Assignement Feedback
app.add_url_rule('/api/programmingfeedback/<int:week>',view_func=ProgrammingFeeback.as_view('prograamming_feedback'),methods = ['GET'])

# check for database and create if not exists
with app.app_context():
    db.create_all()
