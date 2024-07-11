from application.models.model import Questions, Submissions, db
from flask import jsonify, request
from flask_restful import Resource


class SubmitAnswerAPI(Resource):
    def post(self):
        data = request.get_json()
        number = data.get('number')
        weeknumber = data.get('weeknumber')
        submitted_answers = data.get('submitted_answers', ["", "", "", ""])

        # Fetch the question from the database
        question = Questions.query.filter_by(number=number, weeknumber=weeknumber).first()
        if not question:
            return {"message": "Question not found"}, 404

        correct_answers = [
            question.answer1,
            question.answer2,
            question.answer3,
            question.answer4
        ]

        total_correct_answers = sum(1 for answer in correct_answers if answer)
        correct_count = 0
        marks_awarded = 0

        for submitted, correct in zip(submitted_answers, correct_answers):
            if submitted and submitted == correct:
                correct_count += 1
            elif submitted and submitted != correct:
                marks_awarded = 0
                break
        
        if correct_count > 0 and total_correct_answers > 0:
            marks_awarded = correct_count / total_correct_answers

        # Check for existing submissions and delete them if present
        existing_submissions = Submissions.query.filter_by(number=number, weeknumber=weeknumber).all()
        if existing_submissions:
            for submission in existing_submissions:
                db.session.delete(submission)
            db.session.commit()

        # Add the new submission
        submission = Submissions(
            number=number,
            weeknumber=weeknumber,
            submitted_answer1=submitted_answers[0],
            submitted_answer2=submitted_answers[1],
            submitted_answer3=submitted_answers[2],
            submitted_answer4=submitted_answers[3],
            marks_awarded=marks_awarded
        )

        db.session.add(submission)
        db.session.commit()

        return submission.serialize(), 201
