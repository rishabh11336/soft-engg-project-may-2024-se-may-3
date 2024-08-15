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
    "LL-7u9HFmV7Zyu9sCyDE7NpY7hjFfHt6p7h6Po9pLAi9d4VgkjwTTL9bnN51cKsDwJ7",
    "LL-Qm2wzWhTyYYAJV2kWgGhcbCLIVZBCOzSDuib1smXSsouoANM1YtgSfp3v9IlyQPW",
    "LA-dbfcbb80618f4c7ea1c27f4e20af79fd4af3c30849f94657aef232d0197082b5",
    "LA-51215ccf1b454a63a7d70253a0ac65b4c55758b2e56042e2a590def77849fe83"
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
def generate_summary(transcript):
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
            response = client.chat.completions.create(
                model="llama3-70b",
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
            response = client.chat.completions.create(
                model="llama3-70b",
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

