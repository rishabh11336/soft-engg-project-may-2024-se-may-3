from application.models.model import (ProgrammingAssignments,
                                      ProgrammingSubmissions, db)
from flask import jsonify, request
from flask_restful import Resource


class SubmitProgrammingAssignmentAPI(Resource):
    def post(self):
        data = request.get_json()
        weeknumber = data.get('weeknumber')
        assignment_id = data.get('assignment_id')
        user_outputs = [
            data.get('user_output_public_test_case1', ""),
            data.get('user_output_public_test_case2', ""),
            data.get('user_output_public_test_case3', ""),
            data.get('user_output_private_test_case1', ""),
            data.get('user_output_private_test_case2', ""),
            data.get('user_output_private_test_case3', "")
        ]

        assignment = ProgrammingAssignments.query.filter_by(id=assignment_id, weeknumber=weeknumber).first()
        if not assignment:
            return {"message": "Assignment not found"}, 404

        expected_outputs = [
            assignment.output_public_test_case1,
            assignment.output_public_test_case2,
            assignment.output_public_test_case3,
            assignment.output_private_test_case1,
            assignment.output_private_test_case2,
            assignment.output_private_test_case3
        ]

        total_test_cases = sum(1 for output in expected_outputs if output)
        correct_count = 0
        marks_awarded = 0

        for user_output, expected_output in zip(user_outputs, expected_outputs):
            if user_output == expected_output:
                correct_count += 1

        if correct_count > 0 and total_test_cases > 0:
            marks_awarded = correct_count / total_test_cases

        submission = ProgrammingSubmissions(
            weeknumber=weeknumber,
            assignment_id=assignment_id,
            user_output_public_test_case1=user_outputs[0],
            user_output_public_test_case2=user_outputs[1],
            user_output_public_test_case3=user_outputs[2],
            user_output_private_test_case1=user_outputs[3],
            user_output_private_test_case2=user_outputs[4],
            user_output_private_test_case3=user_outputs[5],
            marks_awarded=marks_awarded
        )

        # Check for existing submission and delete if exists
        existing_submission = ProgrammingSubmissions.query.filter_by(weeknumber=weeknumber, assignment_id=assignment_id).first()
        if existing_submission:
            db.session.delete(existing_submission)
            db.session.commit()

        db.session.add(submission)
        db.session.commit()

        return submission.serialize(), 201
