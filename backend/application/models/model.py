from flask_sqlalchemy import SQLAlchemy
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

db = SQLAlchemy()


def YouTubeTranscript(video_id):
    '''
        Fetches the transcript of the video with the given video_id
        "video_id is the video id of the youtube video example: 'dQw4w9WgXcQ' 
        in a link like https://www.youtube.com/watch?v=dQw4w9WgXcQ
    '''
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    formatter = TextFormatter()
    return formatter.format_transcript(transcript)

class Questions(db.Model):
    __tablename__ = 'questions'
    number = db.Column(db.Integer,autoincrement = True,primary_key = True)
    weeknumber = db.Column(db.Integer,nullable = False)
    #! Need a column named week number so that we do not need to create new tables 
    type = db.Column(db.String(255),nullable = False)
    question = db.Column(db.String(255))
    code_snippet = db.Column(db.String(255))
    option1 = db.Column(db.String(255))
    option2 = db.Column(db.String(255))
    option3 = db.Column(db.String(255))
    option4 = db.Column(db.String(255))
    answer1 = db.Column(db.String(255))
    answer2 = db.Column(db.String(255))
    answer3 = db.Column(db.String(255))
    answer4 = db.Column(db.String(255))

    def serialize(self):
        return {
            "number": self.number,
            "weeknumber": self.weeknumber,
            "type": self.type,
            "question": self.question,
            "code_snippet": self.code_snippet,
            "option1": self.option1,
            "option2": self.option2,
            "option3": self.option3,
            "option4": self.option4,
            "answer1": self.answer1,
            "answer2": self.answer2,
            "answer3": self.answer3,
            "answer4": self.answer4
        }


class CourseContent(db.Model):
    __tablename__ = 'coursecontent'
    id = db.Column(db.Integer,autoincrement = True, primary_key = True)
    week = db.Column(db.Integer,nullable = False)
    index = db.Column(db.Integer,nullable = False)
    type = db.Column(db.String(255),nullable = False)
    title = db.Column(db.String(255),nullable = False)
    link = db.Column(db.String(255),nullable = False)

    def serialize(self):
        return {
            "id": self.id,
            "week": self.week,
            "index": str(self.index),
            "type": self.type,
            "title": self.title,
            "link": self.link,
            "transcript": YouTubeTranscript(self.link)
        }

class Submissions(db.Model):
    _tablename_ = 'submissions'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    weeknumber = db.Column(db.Integer, nullable=False)
    submitted_answer1 = db.Column(db.String(255))
    submitted_answer2 = db.Column(db.String(255))
    submitted_answer3 = db.Column(db.String(255))
    submitted_answer4 = db.Column(db.String(255))
    marks_awarded = db.Column(db.Float, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "number": self.number,
            "weeknumber": self.weeknumber,
            "submitted_answer1": self.submitted_answer1,
            "submitted_answer2": self.submitted_answer2,
            "submitted_answer3": self.submitted_answer3,
            "submitted_answer4": self.submitted_answer4,
            "marks_awarded": self.marks_awarded
        }

class ProgrammingAssignments(db.Model):
    _tablename_ = 'programming_assignments'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    weeknumber = db.Column(db.Integer, nullable=False)
    question = db.Column(db.String(255), nullable=False)
    public_test_case1 = db.Column(db.String(255))
    public_test_case2 = db.Column(db.String(255))
    public_test_case3 = db.Column(db.String(255))
    output_public_test_case1 = db.Column(db.String(255))
    output_public_test_case2 = db.Column(db.String(255))
    output_public_test_case3 = db.Column(db.String(255))
    private_test_case1 = db.Column(db.String(255))
    private_test_case2 = db.Column(db.String(255))
    private_test_case3 = db.Column(db.String(255))
    output_private_test_case1 = db.Column(db.String(255))
    output_private_test_case2 = db.Column(db.String(255))
    output_private_test_case3 = db.Column(db.String(255))

    def serialize(self):
        return {
            "id": self.id,
            "weeknumber": self.weeknumber,
            "question": self.question,
            "public_test_case1": self.public_test_case1,
            "public_test_case2": self.public_test_case2,
            "public_test_case3": self.public_test_case3,
            "output_public_test_case1": self.output_public_test_case1,
            "output_public_test_case2": self.output_public_test_case2,
            "output_public_test_case3": self.output_public_test_case3,
            "private_test_case1": self.private_test_case1,
            "private_test_case2": self.private_test_case2,
            "private_test_case3": self.private_test_case3,
            "output_private_test_case1": self.output_private_test_case1,
            "output_private_test_case2": self.output_private_test_case2,
            "output_private_test_case3": self.output_private_test_case3
        }


class ProgrammingSubmissions(db.Model):
    __tablename__ = 'programming_submissions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    weeknumber = db.Column(db.Integer, nullable=False)
    assignment_id = db.Column(db.Integer, nullable=False)
    user_output_public_test_case1 = db.Column(db.String(255))
    user_output_public_test_case2 = db.Column(db.String(255))
    user_output_public_test_case3 = db.Column(db.String(255))
    user_output_private_test_case1 = db.Column(db.String(255))
    user_output_private_test_case2 = db.Column(db.String(255))
    user_output_private_test_case3 = db.Column(db.String(255))
    marks_awarded = db.Column(db.Float, nullable=False)
    SUBMITCODE = db.Column(db.String(300), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'weeknumber': self.weeknumber,
            'assignment_id': self.assignment_id,
            'user_output_public_test_case1': self.user_output_public_test_case1,
            'user_output_public_test_case2': self.user_output_public_test_case2,
            'user_output_public_test_case3': self.user_output_public_test_case3,
            'user_output_private_test_case1': self.user_output_private_test_case1,
            'user_output_private_test_case2': self.user_output_private_test_case2,
            'user_output_private_test_case3': self.user_output_private_test_case3,
            'marks_awarded': self.marks_awarded,
            'submit_code': self.SUBMITCODE
        }

class Quiz(db.Model):
    __tablename__ = 'quiz_questions'
    id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    number = db.Column(db.Integer,nullable = False)
    type = db.Column(db.String,nullable = False)
    question = db.Column(db.String,nullable = False)
    code_snippet = db.Column(db.String,nullable = False)
    option1 = db.Column(db.String(255))
    option2 = db.Column(db.String(255))
    option3 = db.Column(db.String(255))
    option4 = db.Column(db.String(255))
    answer1 = db.Column(db.String(255))
    answer2 = db.Column(db.String(255))
    answer3 = db.Column(db.String(255))
    answer4 = db.Column(db.String(255))
    youranswer1 = db.Column(db.String(255))
    youranswer2 = db.Column(db.String(255))
    youranswer3 = db.Column(db.String(255))
    youranswer4 = db.Column(db.String(255))
        
    def serialize(self):
        return {
        'id':self.id,
        'question_number':self.number,
        'question_type': self.type,
        'question':self.question,
        'code_snippet':self.code_snippet,
        "option1": self.option1,
        "option2": self.option2,
        "option3": self.option3,
        "option4": self.option4,
        "answer1": self.answer1,
        "answer2": self.answer2,
        "answer3": self.answer3,
        "answer4": self.answer4,
        "youranswer1": self.youranswer1,
        "youranswer2": self.youranswer2,
        "youranswer3": self.youranswer3,
        "youranswer4": self.answer4
 


        }
