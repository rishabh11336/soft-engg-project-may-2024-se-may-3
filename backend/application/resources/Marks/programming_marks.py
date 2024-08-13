from application.models.model import ProgrammingSubmissions, db
from flask import jsonify
from flask_restful import Resource

class GetProgrammingAssignmentMarksAPI(Resource):
    def get(self, weeknumber, assignment_id):
        submissions = ProgrammingSubmissions.query.filter_by(weeknumber=weeknumber, assignment_id=assignment_id).all()

        if not submissions:
            return {"message": "No submissions found for the given week and assignment"}, 404
        
        total_marks = sum(s.marks_awarded for s in submissions)
        total_assignments = len(submissions)

        normalized_marks = (total_marks / total_assignments) * 100 if total_assignments > 0 else 0

        return jsonify({
            "weeknumber": weeknumber,
            "assignment_id": assignment_id,
            "marks_awarded": normalized_marks
        })
