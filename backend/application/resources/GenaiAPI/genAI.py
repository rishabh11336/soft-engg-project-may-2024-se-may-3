from llamaapi import LlamaAPI
import json
from openai import OpenAI
import openai
import sqlite3
import pandas as pd
from mistralai import Mistral
import markdown

# this a string that will get updated to store history of the chat in doubt-bot
history = ''

# this is a list that stores tokens
tokens = [    
          "hjpyLPMMAnbUgCOjxOVbhdTyajCihDDv"
    # Add more tokens if required
]

# this is a function that will be used inside the other functions below to call tokens and initiate API client.
def get_client(token):
    return Mistral(
        api_key=token
    )

# below this are the genai_functions that need to be called using routers and api

#Summary generation function. Takes 'id' attribute from database as input, and returns the summary string as output
def generate_summary(transcript):
    #Generating summary
    for token in tokens:
        try:
            client = get_client(token)
            response = client.chat.complete(
                model="open-mistral-nemo",
                messages=[
                    {"role": "system",
                     "content": "You are given a transcript of a programming lecture video. Give summary of the key concepts taught"},
                    {"role": "user", "content": transcript}
                ],
                max_tokens=5000
            )
            return response.choices[0].message.content
        except openai.AuthenticationError as e:
            if 'Insufficient balance' in str(e):
                continue
            else:
                raise e
    raise ValueError("All tokens have been exhausted.")

#Function to explain theory questions. Takes week and question number as input, returns explanation string as output
def explain_theory_question(question, code_snippet):
    # the codes below to fetch the data are written assuming that both this .py file
    # and the databases files are in the same root directory. Kindly rewrite
    # this section as required

    #fetching the questions
    # db_path = 'dev.db'
    # conn = sqlite3.connect(db_path)
    # cursor = conn.cursor()

    # cursor.execute("SELECT question FROM questions WHERE number = ?", (number,))
    # row = cursor.fetchone()

    
    # if row:
    #     question = row[0]
    # else:
    #     question = ""

    # cursor.execute("SELECT code_snippet FROM questions WHERE number = ?", (number,))
    # row = cursor.fetchone()
    # if row:
    #     code_snippet = row[0]
    # else:
    #     code_snippet = ""
    # conn.close()
    if code_snippet is None:
        code_snippet=" "
    prompt = question + "\nCode Snippet:\n" + code_snippet

    
    # everything above this should be rewritten as required
    #generate explanation for question
    for token in tokens:
        try:
            client = get_client(token)
            response = client.chat.complete(
                model="open-mistral-nemo",
                messages=[
                    {"role": "system",
                     "content": "You are given a programming question. Explain the question, and what concept it is based on, without making the answer too obvious"},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=7000
            )
            return response.choices[0].message.content
        except openai.AuthenticationError as e:
            if 'Insufficient balance' in str(e):
                continue
            else:
                raise e
    raise ValueError("All tokens have been exhausted.")


#function to explain programming questions. Takes week number as input and returns explanation as output
def explain_programming_assignment(question):
    # the codes below to fetch the data are written assuming that both this .py file
    # and the database files are in the same root directory. Kindly rewrite
    # this section as required

    #Fetch questions
   
    # db_path = 'dev.db'
    # conn = sqlite3.connect(db_path)
    # cursor = conn.cursor()

    # cursor.execute("SELECT question FROM programming_assignments WHERE id = ?", (number,))
    # row = cursor.fetchone()

    
    # if row:
    #     question = row[0]
    # else:
    #     question = ""
    # # everything above this should be rewritten as required
    # #generate question explanation
    for token in tokens:
        try:
            client = get_client(token)
            response = client.chat.complete(
                model="open-mistral-nemo",
                messages=[
                    {"role": "system",
                     "content": "You are given a programming question, which requires the student to run a code. Explain how to approach the problem, what are the concepts, without giving away the answer."},
                    {"role": "user", "content": question}
                ],
                max_tokens=7000
            )
            return response.choices[0].message.content
        except openai.AuthenticationError as e:
            if 'Insufficient balance' in str(e):
                continue
            else:
                raise e
    raise ValueError("All tokens have been exhausted.")



#Chatbot to solve doubts. Takes video id and question as inputs, returns answer as output
def doubtbot(video_id,transcript, question="How does list append works"):
    global history
    history += "User:" + question

    # the codes below to fetch the data are written assuming that both this .py file
    # and the database files are in the same root directory. Kindly rewrite
    # this section as required

    # db_path = 'dev.db'
    # conn = sqlite3.connect(db_path)
    # cursor = conn.cursor()

    # cursor.execute("SELECT transcript FROM coursecontent WHERE id = ?", (video_id,))
    # row = cursor.fetchone()

    # conn.close()

    # if row:
    #     transcript = row[0]
    # else:
    #     transcript = ""

    # everything above this should be rewritten as required
    #! pass the history as the function and when the next time the function is called past the updated history. Only for the same week
    for token in tokens:
        try:
            client = get_client(token)
            response = client.chat.complete(
                model="open-mistral-nemo",
                messages=[
                    {"role": "system",
                     "content": "You are given a transcript of a programming lecture video below. Based on this, act as a doubt-bot and answer doubts asked by learners. Do not answer non-programming related questions" + transcript + "\n This is the history so far" + history},
                    {"role": "user", "content": question}
                ],
                max_tokens=2000
            )
            history += "System: " + response.choices[0].message.content
            return response.choices[0].message.content
        except openai.AuthenticationError as e:
            if 'Insufficient balance' in str(e):
                continue
            else:
                raise e
    raise ValueError("All tokens have been exhausted.")



#PROGRAMMING ASSIGNMENT REVIEW
#! This needs to fetch questions for a questions from the programming_assignement table and code from the programming_submisson 
def PAfeedback(question, code):
    for token in tokens:
        try:
            client = get_client(token)
            response = client.chat.completions.create(
                model="open-mistral-nemo",
                messages=[
                    {"role": "system",
                     "content": "You are given a coding question, and the code written by a student. Provide feedback for the code, and suggest possible improvements"},
                    {"role": "user", "content": "Question:" + question + "\n Student's code:" + code}
                ],
                max_tokens=7000
            )
            return response.choices[0].message.content
        except openai.AuthenticationError as e:
            if 'Insufficient balance' in str(e):
                continue
            else:
                raise e
    raise ValueError("All tokens have been exhausted.")

#QUIZ REVIEW FROM HERE
# def quiz_review(quiz_records):
#     #! Entire rows should be put as the input
#     feedback = ""
#     incorrect_questions = []
#     topic_areas = {}

#     # Iterate through the quiz data from the database query
#     for row in quiz_records:
#         question_id = row.QuestionNumber
#         question_type = row.QuestionType
#         question = row.Question
#         code_snippet = getattr(row, 'CodeSnippet', '')  # Use getattr() to handle missing 'CodeSnippet'
#         correct_answer1 = row.Answer1
#         correct_answer2 = row.Answer2
#         correct_answer3 = row.Answer3
#         correct_answer4 = row.Answer4

#         user_answer1 = row.YourAnswer1
#         user_answer2 = row.YourAnswer2
#         user_answer3 = row.YourAnswer3
#         user_answer4 = row.YourAnswer4

#         correct_answers = [correct_answer1, correct_answer2, correct_answer3, correct_answer4]
#         user_answers_list = [user_answer1, user_answer2, user_answer3, user_answer4]

#         # Clean empty strings from the correct answers and user answers
#         correct_answers = [ans for ans in correct_answers if ans]
#         user_answers_list = [ans for ans in user_answers_list if ans]

#         # Check if the user's answers are correct
#         if question_type == "Multi-choice":
#             correct_answer = correct_answers[0]
#             user_answer = user_answers_list[0] if user_answers_list else ""

#             if user_answer != correct_answer:
#                 incorrect_questions.append((question_id, question, correct_answer, user_answer))
#                 update_topic_areas(topic_areas, question)

#         elif question_type == "Multi-select":
#             if set(user_answers_list) != set(correct_answers):
#                 incorrect_questions.append((question_id, question, ', '.join(correct_answers), ', '.join(user_answers_list)))
#                 update_topic_areas(topic_areas, question)

#     # Generate detailed feedback and recommendations
#     if incorrect_questions:
#         feedback += "Here is a summary of the questions you answered incorrectly and the areas you need to focus on:\n\n"
#         for question_id, question, correct_answer, user_answer in incorrect_questions:
#             feedback += f"Question {question_id}: {question}\n"
#             feedback += f"Your answer: {user_answer}\n"
#             feedback += f"Correct answer: {correct_answer}\n\n"
#             feedback += generate_explanation(question, code_snippet, correct_answer, user_answer)

#         feedback += "Based on your performance, here are some areas you should review:\n"
#         for topic, count in topic_areas.items():
#             feedback += f"- {topic}: You missed {count} question(s) related to this concept.\n"
#     else:
#         feedback = "Great job! You answered all questions correctly."

#     return feedback

def quiz_review(quiz_records):
    feedback = ""
    incorrect_questions = []
    topic_areas = {}

    for row in quiz_records:
        question_id = row.id
        question_type = row.type
        question = row.question
        code_snippet = row.code_snippet
        correct_answer1 = row.answer1
        correct_answer2 = row.answer2
        correct_answer3 = row.answer3
        correct_answer4 = row.answer4

        user_answer1 = row.youranswer1
        user_answer2 = row.youranswer2
        user_answer3 = row.youranswer3
        user_answer4 = row.youranswer4

        correct_answers = [correct_answer1, correct_answer2, correct_answer3, correct_answer4]
        user_answers_list = [user_answer1, user_answer2, user_answer3, user_answer4]

        correct_answers = [ans for ans in correct_answers if ans]
        user_answers_list = [ans for ans in user_answers_list if ans]

        if question_type == "Multi-choice":
            correct_answer = correct_answers[0]
            user_answer = user_answers_list[0] if user_answers_list else ""

            if user_answer != correct_answer:
                incorrect_questions.append((question_id, question, correct_answer, user_answer))
                update_topic_areas(topic_areas, question)

        elif question_type == "Multi-select":
            if set(user_answers_list) != set(correct_answers):
                incorrect_questions.append((question_id, question, ', '.join(correct_answers), ', '.join(user_answers_list)))
                update_topic_areas(topic_areas, question)

    if incorrect_questions:
        feedback += "Here is a summary of the questions you answered incorrectly and the areas you need to focus on:\n\n"
        for question_id, question, correct_answer, user_answer in incorrect_questions:
            feedback += f"Question {question_id}: {question}\n"
            feedback += f"Your answer: {user_answer}\n"
            feedback += f"Correct answer: {correct_answer}\n\n"
            feedback += generate_explanation(question, code_snippet, correct_answer, user_answer)

        feedback += "Based on your performance, here are some areas you should review:\n"
        for topic, count in topic_areas.items():
            feedback += f"- {topic}: You missed {count} question(s) related to this concept.\n"
    else:
        feedback = "Great job! You answered all questions correctly."

    return feedback


# Update topic areas based on question content
#! This is a helper functions
def update_topic_areas(topic_areas, question):
    potential_topics = ['loops', 'functions', 'recursion', 'conditionals', 'data structures', 'object-oriented programming']
    for topic in potential_topics:
        if topic in question.lower():
            if topic in topic_areas:
                topic_areas[topic] += 1
            else:
                topic_areas[topic] = 1

# Function to generate explanations using LLaMA API
#! This is a helper function
def generate_explanation(question, code_snippet, correct_answer, user_answer):
    # Construct the prompt for LLaMA
    prompt = f"""
    You are a highly knowledgeable Python tutor. Explain the correct answer and the mistake in the following scenario:

    Question: {question}
    Code Snippet:
    {code_snippet if code_snippet else 'N/A'}

    Correct Answer: {correct_answer}
    User's Incorrect Answer: {user_answer}

    Provide a detailed explanation for the correct answer and what the user should review.
    """

    # Make the API call to LLaMA
    for token in tokens:
        try:
            client = get_client(token)
            response = client.chat.complete(
                model="open-mistral-nemo",
                messages=[
                    {"role": "system", "content": "You are a Python expert. Individuals will ask you for feedback on incorrect answers to python questions. Provide a detailed explanation for the correct answer and what the user should review."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=5000
            )

            return response.choices[0].message.content

        except openai.AuthenticationError as e:
            print(str(e))
            if 'Insufficient balance' in str(e):
                continue
            else:
                raise e

    raise ValueError("All tokens have been exhausted.")
