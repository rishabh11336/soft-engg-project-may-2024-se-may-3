from application.models.model import Submissions, db
from flask import jsonify
from flask_restful import Resource


class MarksAllWeeksAPI(Resource):
    def get(self):
        weeks = db.session.query(Submissions.weeknumber).distinct().all()
        week_marks = []

        for week in weeks:
            total_marks = db.session.query(db.func.sum(Submissions.marks_awarded)).filter_by(weeknumber=week[0]).scalar()
            total_questions = db.session.query(Submissions).filter_by(weeknumber=week[0]).count()
            normalized_marks = (total_marks / total_questions) * 100 if total_questions > 0 else 0
            week_marks.append({
                "weeknumber": week[0],
                "marks": normalized_marks
            })

        return jsonify(week_marks)

class MarksSpecificWeekAPI(Resource):
    def get(self, week):
        total_marks = db.session.query(db.func.sum(Submissions.marks_awarded)).filter_by(weeknumber=week).scalar()
        total_questions = db.session.query(Submissions).filter_by(weeknumber=week).count()
        normalized_marks = (total_marks / total_questions) * 100 if total_questions > 0 else 0

        return jsonify({
            "weeknumber": week,
            "marks": normalized_marks
        })
