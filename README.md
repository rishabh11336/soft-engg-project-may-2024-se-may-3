This commit is for the GEN AI functions of the SE project.

The code is designed assuming that the genAI.py file and 'dev.db', 'ta_complete.xlsx' and 'Prog_assign.xlsx' are in the same directory. If the directories are different, change the paths in the functions accordingly.

The file contains 4 functionalities. Their purpose, inputs, outputs, and working are described below:


1. get_client(token):
   
    -This function is used to initialize the GenAI API client necessary for generating text.
   
    -It is used in all the 4 other functions.
   
    -It takes an API token as input and initialized the client.

2. generate_summary(video_id):
   
    -This function is used to generate summary for transcripts of videos.
   
    -It takes the video_id as input. It fetches the transcript of the corresponding video from the database 'dev.db', where the video is uniquely identified by the primary key 'id'.
![image](https://github.com/user-attachments/assets/4f5b5acc-991c-43de-a5c7-0eecf7439cab)


    -The function then processes the fetched transcript, initializes the GenAI client, and returns the summary as a string. 

3. explain_theory_question(week_number, question_number):
    -This function is used to generate a simplified explanation of Theory Graded Assignment questions, that helps the learner to understand and solve the questions in a step-wise approach.
   
    -It fetches the data from the 'ta_complete.xlsx' file, which contains all questions of the course.
   
    -It filters the question by week_number, and question_number. The combined pair of attributes (week_number, question_number) acts as the primary key in this case, as neither of them are individually unique.

    -The function fetches the base question, as well as the associated code snippet(if it is part of the question) from the identified row.

    -Then, the API client is initialized, and the explanation is generated.

    -The function returns the explanation as a string.

4. explain_programming_assignment(week_number):

   -This function is used to generate simplified explanation for the Programming Assignment questions. It provides suggestions on how the programmer can approach the problem at hand.

   -It takes week_number as input, fetches corresponding question from the "Prog_assign.xlsx" file, which contains 1 programming assignment question from each week.

   -It then connects to the API client, and generates explanation for the question.

   -The function returns the generated explanation as a string

5. doubtbot(video_id, question):

   -This function is used to generate explanations for doubts of the user.

   -It takes 2 parameters as input: the video_id, and the question asked by the user.

   -The video id is used to fetch transcript of the video.
    
   -The function also uses a global string variable, 'history', to store chat history. History is updated each time the user asks a question, and each time the system responds with an answer.

   -The function returns the response to current question as output as a string.

6. It is also important to note the refreshing of tokens.

    -The tokens are stored in a list.

    -Each time any function is run, it is executed through a try-catch-else block.

    -If the token has enough balance, there is no issue.

    -If the token has insufficient balance, the error is caught, and it is replaced with a fresh token.
