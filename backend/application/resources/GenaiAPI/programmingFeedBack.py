from flask_restful import Resource
from application.models.model import ProgrammingAssignments, ProgrammingSubmissions
from .genAI import PAfeedback
class ProgrammingFeeback(Resource):
    def get(self,week = None):
        programming_submission = ProgrammingSubmissions.query.filter_by(weeknumber = week)
        programming_question = ProgrammingAssignments.query.filter_by(weeknumber = week)

        if (not programming_question) or (not programming_submission):
            return {'message': "Some error occured"}, 404
        
        return {'response': PAfeedback(programming_question.question,programming_submission.SUBMITCODE)}
    
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass