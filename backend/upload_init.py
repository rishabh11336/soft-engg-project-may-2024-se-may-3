# from application.models.models import Questions,db,CourseContent
from main import app
import csv
import pandas as pd
from application.models.model import db,CourseContent,Questions,ProgrammingAssignments

def updateCourseContent():
    dfCourseContent = pd.read_csv('data/Course Content - Sheet1.csv')
    print('INFO: Writing data for course content')
    for idx in range(dfCourseContent.shape[0]):
        coursecontent = CourseContent(week = int(dfCourseContent['Week'][idx]),index = dfCourseContent['Index'][idx],type=dfCourseContent['Type'][idx],title = dfCourseContent['Title'][idx],link = dfCourseContent['YouTube Link'][idx],transcript = dfCourseContent['Transcript'][idx])
        db.session.add(coursecontent)
    db.session.commit()
    print('INFO: Writing data for course content complete')

def updateProgrammingCourseContent():
    dfProgrammingAssignement = pd.read_excel('data/Copy of PA.xlsx')
    print("INFO: Writing data for  programming assignements")
    for idx in range(dfProgrammingAssignement.shape[0]):
        programmingAssignement = ProgrammingAssignments(
            weeknumber = dfProgrammingAssignement['WeekNumber'][idx],
            question = dfProgrammingAssignement['Question'][idx],
            public_test_case1 = dfProgrammingAssignement['PublicTestCase1'][idx],
            public_test_case2 = dfProgrammingAssignement['PublicTestCase2'][idx],
            public_test_case3 = dfProgrammingAssignement['PublicTestCase3'][idx],
            output_public_test_case1 = dfProgrammingAssignement['OutputPublicTestCase1'][idx],
            output_public_test_case2 = dfProgrammingAssignement['OutputPublicTestCase2'][idx],
            output_public_test_case3 = dfProgrammingAssignement['OutputPublicTestCase3'][idx],
            private_test_case1 = dfProgrammingAssignement['PrivateTestCase1'][idx],
            private_test_case2 = dfProgrammingAssignement['PrivateTestCase2'][idx],
            private_test_case3 = dfProgrammingAssignement['PrivateTestCase3'][idx],
            output_private_test_case1 = dfProgrammingAssignement['OutputPrivateTestCase1'][idx],
            output_private_test_case2 = dfProgrammingAssignement['OutputPrivateTestCase2'][idx],
            output_private_test_case3 = dfProgrammingAssignement['OutputPrivateTestCase3'][idx]
        )
        db.session.add(programmingAssignement)
    db.session.commit()
    print("INFO: Writing data form programming assignements COMPLETE")

def updateWeeklyQuestions():
    dataframe = pd.read_excel('data/ta_complete.xlsx')
    print('INFO: Writing the data for all weeks')
    for idx in range(dataframe.shape[0]):
        question = Questions(type = dataframe['QuestionType'][idx], 
                             weeknumber = dataframe['WeekNumber'][idx],
                             question = dataframe['Question'][idx],
                             code_snippet = dataframe['CodeSnippet'][idx],
                             option1 = dataframe['Option1'][idx],
                             option2 = dataframe['Option2'][idx],
                             option3 = dataframe['Option3'][idx],
                             option4 = dataframe['Option4'][idx],
                             answer1 = dataframe['Answer1'][idx],
                             answer2 = dataframe['Answer2'][idx],
                             answer3 = dataframe['Answer3'][idx],
                             answer4 = dataframe['Answer4'][idx])

        db.session.add(question)
    print('INFO: Writing the data for all weeks complete')
    db.session.commit()
with app.app_context():
    db.create_all()
    updateCourseContent()
    updateProgrammingCourseContent()
    updateWeeklyQuestions()





