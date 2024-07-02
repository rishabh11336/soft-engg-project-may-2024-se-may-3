from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
    transcript = db.Column(db.String,nullable = False)

    def serialize(self):
        return {
            "id": self.id,
            "week": self.week,
            "index": str(self.index),
            "type": self.type,
            "title": self.title,
            "link": self.link,
            "transcript": self.transcript
        }
