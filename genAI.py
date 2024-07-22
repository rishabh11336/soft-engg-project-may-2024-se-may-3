from llamaapi import LlamaAPI
import json
from openai import OpenAI
import openai
import sqlite3
import pandas as pd

# this a string that will get updated to store history of the chat in doubt-bot
history = ''

# this is a list that stores tokens
tokens = [
    'LL-7laZB8w678F4A0OgeCEIc7dKUMtIYPiPGysdgWaWsGjLo5eoA1SY0QTuzSkcdg6r',
    'LL-esImLousIiNJvte7MOE1tonq4ZNHYSmcj5jBqRzc9aUkpMBk7AvSFORsKpZ2cxZ3',
    'LL-O9tdUpjWi0Vbsa9gESembDfAAg3lV8yLMRsbro3WZojE9zEWJSbGHOCRNJguE1lF',
    'LL-OjDJrgP1pldQBUd0n6ClilHK5xTfwRsXBN88fd1Bs0bhQIxJ2JjPma6cc0oIqwvO',
    'LL-wvB7p79fDcSMj4w0v2j7wmEPEwlUrs7YKAK1UXBeaIrEh0NfPLe29ZkRNr4uOWB8',
    'LL-daymeve1sjGZAfI0fv3g3QZ7bxhVeAUHVjDZ39hFodeeYD7UI6225tcdSJPK4JFV',
    # Add more tokens if required
]


# this is a function that will be used inside the other functions below to call tokens and initiate API client.
def get_client(token):
    return OpenAI(
        api_key=token,
        base_url="https://api.llama-api.com"
    )


# below this are the genai_functions that need to be called using routers and api

#Summary generation function. Takes 'id' attribute from database as input, and returns the summary string as output
def generate_summary(video_id):
    # the codes below to fetch the data are written assuming that both this .py file
    # and the database/xlsx files are in the same root directory. Kindly rewrite
    # this section as required

    #connect to database
    db_path = 'dev.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    #fetch transcript by video id
    cursor.execute("SELECT transcript FROM coursecontent WHERE id = ?", (video_id,))
    row = cursor.fetchone()

    conn.close()

    if row:
        transcript = row[0]
    else:
        transcript = "Failed"
        raise ValueError(f"No transcript found for video ID {video_id}")

    # everything above this should be rewritten as required
    #Generating summary
    for token in tokens:
        try:
            client = get_client(token)
            response = client.chat.completions.create(
                model="llama3-70b",
                messages=[
                    {"role": "system",
                     "content": "You are given a transcript of a programming lecture video. Give summary of the key concepts taught"},
                    {"role": "user", "content": transcript}
                ],
                max_tokens=10000
            )
            return response.choices[0].message.content
        except openai.AuthenticationError as e:
            if 'Insufficient balance' in str(e):
                continue
            else:
                raise e
    raise ValueError("All tokens have been exhausted.")

#Function to explain theory questions. Takes week and question number as input, returns explanation string as output
def explain_theory_question(week_number, question_number):
    # the codes below to fetch the data are written assuming that both this .py file
    # and the database/xlsx files are in the same root directory. Kindly rewrite
    # this section as required

    #fetching the questions
    file_path = 'ta_complete.xlsx'
    df = pd.read_excel(file_path)
    filtered_df = df[(df['WeekNumber'] == week_number) & (df['QuestionNumber'] == question_number)]

    #Filter required question and code snipped
    if not filtered_df.empty:
        question = filtered_df['Question'].values[0]
        code_snippet = filtered_df['CodeSnippet'].values[0]
    else:
        question = ""
        code_snippet = " "
    prompt = question + "\nCode Snippet:\n" + code_snippet

    
    # everything above this should be rewritten as required
    #generate explanation for question
    for token in tokens:
        try:
            client = get_client(token)
            response = client.chat.completions.create(
                model="llama3-70b",
                messages=[
                    {"role": "system",
                     "content": "You are given a programming question. Explain the question, and what concept it is based on, without making the answer too obvious"},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=10000
            )
            return response.choices[0].message.content
        except openai.AuthenticationError as e:
            if 'Insufficient balance' in str(e):
                continue
            else:
                raise e
    raise ValueError("All tokens have been exhausted.")

#function to explain programming questions. Takes week number as input and returns explanation as output
def explain_programming_assignment(week_number):
    # the codes below to fetch the data are written assuming that both this .py file
    # and the database/xlsx files are in the same root directory. Kindly rewrite
    # this section as required

    #Fetch questions
    file_path = 'Prog_assign.xlsx'
    df = pd.read_excel(file_path)
    #Filter required question
    filtered_df = df[(df['WeekNumber'] == week_number)]

    if not filtered_df.empty:
        question = filtered_df['Question'].values[0]
    else:
        question = "No question"

    # everything above this should be rewritten as required
    #generate question explanation
    for token in tokens:
        try:
            client = get_client(token)
            response = client.chat.completions.create(
                model="llama3-70b",
                messages=[
                    {"role": "system",
                     "content": "You are given a programming question, which requires the student to run a code. Explain how to approach the problem, what are the concepts, without giving away the answer."},
                    {"role": "user", "content": question}
                ],
                max_tokens=10000
            )
            return response.choices[0].message.content
        except openai.AuthenticationError as e:
            if 'Insufficient balance' in str(e):
                continue
            else:
                raise e
    raise ValueError("All tokens have been exhausted.")


#Chatbot to solve doubts. Takes video id and question as inputs, returns answer as output
def doubtbot(video_id, question="How does list append works"):
    global history
    history += "User:" + question

    # the codes below to fetch the data are written assuming that both this .py file
    # and the database/xlsx files are in the same root directory. Kindly rewrite
    # this section as required

    db_path = 'dev.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT transcript FROM coursecontent WHERE id = ?", (video_id,))
    row = cursor.fetchone()

    conn.close()

    if row:
        transcript = row[0]
    else:
        transcript = ""

    # everything above this should be rewritten as required

    for token in tokens:
        try:
            client = get_client(token)
            response = client.chat.completions.create(
                model="llama3-70b",
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
