from application.models.models import Questions,db,CourseContent
from main import app
import csv
import pandas as pd

with app.app_context():
    db.create_all()

    dfCourseContent = pd.read_csv('Course Content - Sheet1.csv')
    print('INFO: Writing data for course content')
    for idx in range(dfCourseContent.shape[0]):
        coursecontent = CourseContent(week = int(dfCourseContent['Week'][idx]),index = dfCourseContent['Index'][idx],type=dfCourseContent['Type'][idx],title = dfCourseContent['Title'][idx],link = dfCourseContent['YouTube Link'][idx],transcript = dfCourseContent['Transcript'][idx])
        db.session.add(coursecontent)
    db.session.commit()
    print('INFO: Writing data for course content complete')



    dataframe = pd.read_csv('TA_Week1 - Sheet1.csv')
    print('INFO: Writing the data for Week-1')
    for idx in range(dataframe.shape[0]):
        question = Questions(type = dataframe['QuestionType'][idx], weeknumber = int(1),
                             question = dataframe['Question'][idx],code_snippet = dataframe['CodeSnippet'][idx],
                             option1 = dataframe['Option1'][idx],option2 = dataframe['Option2'][idx],
                             option3 = dataframe['Option3'][idx],option4 = dataframe['Option4'][idx],
                             answer1 = dataframe['Answer1'][idx],answer2 = dataframe['Answer2'][idx],
                             answer3 = dataframe['Answer3'][idx],answer4 = dataframe['Answer4'][idx])

        db.session.add(question)
    print('INFO: Writing the data for Week-1 complete')
    db.session.commit()

    dataframe = pd.read_csv('TA_Week2 - Sheet1.csv')
    print('INFO: Writing the data for Week-2')
    for idx in range(dataframe.shape[0]):
        question = Questions(type = dataframe['QuestionType'][idx], weeknumber = int(2),
                             question = dataframe['Question'][idx],code_snippet = dataframe['CodeSnippet'][idx],
                             option1 = dataframe['Option1'][idx],option2 = dataframe['Option2'][idx],
                             option3 = dataframe['Option3'][idx],option4 = dataframe['Option4'][idx],
                             answer1 = dataframe['Answer1'][idx],answer2 = dataframe['Answer2'][idx],
                             answer3 = dataframe['Answer3'][idx],answer4 = dataframe['Answer4'][idx])

        db.session.add(question)
    print('INFO: Writing the data for Week-2 complete')
    db.session.commit()




