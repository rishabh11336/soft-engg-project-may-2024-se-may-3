from application.models.model import ProgrammingAssignments, db
from flask import jsonify, request
from flask_restful import Resource


class ProgrammingAssignmentAPI(Resource):
    def get(self, week=None):
        assignments = ProgrammingAssignments.query.filter_by(weeknumber=week).all()
        return jsonify([assignment.serialize() for assignment in assignments])
    
    def post(self):
        data = request.get_json()
        new_assignment = ProgrammingAssignments(
            weeknumber=data.get('weeknumber'),
            question=data.get('question'),
            public_test_case1=data.get('public_test_case1'),
            public_test_case2=data.get('public_test_case2'),
            public_test_case3=data.get('public_test_case3'),
            output_public_test_case1=data.get('output_public_test_case1'),
            output_public_test_case2=data.get('output_public_test_case2'),
            output_public_test_case3=data.get('output_public_test_case3'),
            private_test_case1=data.get('private_test_case1'),
            private_test_case2=data.get('private_test_case2'),
            private_test_case3=data.get('private_test_case3'),
            output_private_test_case1=data.get('output_private_test_case1'),
            output_private_test_case2=data.get('output_private_test_case2'),
            output_private_test_case3=data.get('output_private_test_case3')
        )

        db.session.add(new_assignment)
        db.session.commit()
        return new_assignment.serialize(), 201

    def put(self, id):
        data = request.get_json()
        assignment = ProgrammingAssignments.query.get(id)
        if not assignment:
            return {"message": "Assignment not found"}, 404
        
        assignment.weeknumber = data.get('weeknumber', assignment.weeknumber)
        assignment.question = data.get('question', assignment.question)
        assignment.public_test_case1 = data.get('public_test_case1', assignment.public_test_case1)
        assignment.public_test_case2 = data.get('public_test_case2', assignment.public_test_case2)
        assignment.public_test_case3 = data.get('public_test_case3', assignment.public_test_case3)
        assignment.output_public_test_case1 = data.get('output_public_test_case1', assignment.output_public_test_case1)
        assignment.output_public_test_case2 = data.get('output_public_test_case2', assignment.output_public_test_case2)
        assignment.output_public_test_case3 = data.get('output_public_test_case3', assignment.output_public_test_case3)
        assignment.private_test_case1 = data.get('private_test_case1', assignment.private_test_case1)
        assignment.private_test_case2 = data.get('private_test_case2', assignment.private_test_case2)
        assignment.private_test_case3 = data.get('private_test_case3', assignment.private_test_case3)
        assignment.output_private_test_case1 = data.get('output_private_test_case1', assignment.output_private_test_case1)
        assignment.output_private_test_case2 = data.get('output_private_test_case2', assignment.output_private_test_case2)
        assignment.output_private_test_case3 = data.get('output_private_test_case3', assignment.output_private_test_case3)

        db.session.commit()
        return assignment.serialize(), 200

    def delete(self, id):
        assignment = ProgrammingAssignments.query.get(id)
        if not assignment:
            return {"message": "Assignment not found"}, 404
        
        db.session.delete(assignment)
        db.session.commit()
        return {"message": "Assignment deleted successfully"}, 200
