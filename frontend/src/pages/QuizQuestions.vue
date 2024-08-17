<template>
    <div v-if="quizQuestions.length">
      <h2>Quiz</h2>
      <div class="quiz-wrapper">
        <div
          class="question-answer"
          v-for="(question, index) in quizQuestions"
          :key="question.id"
        >
          <div class="question-wrapper">
            <p>{{ index + 1 }}. {{ question.question }}</p> 
            <strong>1 point</strong>
          </div>
          <div v-if="question.code_snippet" class="question">
            {{ question.code_snippet }}
          </div>
          <div v-if="question.question_type === 'Multi-choice'"> 
            <div v-if="question.option1">
              <input
                type="radio"
                :name="`answer_${question.id}`"
                :id="`option1_${question.id}`"
                :value="question.option1"
                v-model="selectedAnswers[question.id]"
              />
              <label :for="`option1_${question.id}`">{{ question.option1 }}</label>
            </div>
            <div v-if="question.option2">
              <input
                type="radio"
                :name="`answer_${question.id}`"
                :id="`option2_${question.id}`"
                :value="question.option2"
                v-model="selectedAnswers[question.id]"
              />
              <label :for="`option2_${question.id}`">{{ question.option2 }}</label>
            </div>
            <div v-if="question.option3">
              <input
                type="radio"
                :name="`answer_${question.id}`"
                :id="`option3_${question.id}`"
                :value="question.option3"
                v-model="selectedAnswers[question.id]"
              />
              <label :for="`option3_${question.id}`">{{ question.option3 }}</label>
            </div>
            <div v-if="question.option4">
              <input
                type="radio"
                :name="`answer_${question.id}`"
                :id="`option4_${question.id}`"
                :value="question.option4"
                v-model="selectedAnswers[question.id]"
              />
              <label :for="`option4_${question.id}`">{{ question.option4 }}</label>
            </div>
          </div>
          <div v-else>
            <div class="answer">
              <input
                type="text"
                placeholder="Answer..."
                v-model="selectedAnswers[question.id]"
              />
            </div>
          </div>
        </div>
        <button @click="submitAnswers" class="submit">Submit Answers</button>
      </div>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </template>
  
  
  <script>
  import { getQuizQuestions } from '@/services/apiServices';
  
  export default {
    name: 'QuizQuestions',
    data() {
      return {
        quizQuestions: [],
        selectedAnswers: {},
      };
    },
    created() {
      this.fetchQuizQuestions();
    },
    methods: {
      fetchQuizQuestions() {
        getQuizQuestions()
          .then((response) => {
            console.log('Quiz Questions:', response.data);
            this.quizQuestions = response.data;
          })
          .catch((error) => {
            console.error('Error fetching quiz questions:', error);
          });
      },
      submitAnswers() {
        // Implementation for submitting answers
      },
    },
  };
  </script>

<style scoped>
.quiz-wrapper {
    background-color: rgb(247, 246, 246);
    padding: 15px;
    height: auto;
}

.question-answer {
    background-color: white;
    padding: 10px;
    margin-top: 20px;
}

.question-wrapper {
    display: flex;
    justify-content: space-between;
}

.question-answer label {
    color: #212925;
    font-size: 14px;
    margin-left: 10px;
    line-height: 2;
    margin-top: 5px;
}

.question {
    background-color: transparent;
    height: max-content;
    padding: 10px;
    color: rgb(8, 25, 250);
    font-size: 14px;
    font-weight: bold;
    border: 1px solid gray;
    border-radius: 5px;
    margin-bottom: 5px;
}

.answer input {
    width: 90px;
    padding: 5px 15px;
    border-radius: 5px;
    border: 1px solid lightgray;
}

button {
    padding: 10px;
    background-color: black;
    color: white;
    font-size: 14px;
    font-weight: bold;
    border: none;
    border-radius: 2px;
    margin-top: 20px;
    cursor: pointer;
    margin-bottom: 50px;
}

.help-btn {
    margin: 10px 5px 5px 0px;
}

.explanation {
    background-color: rgb(248, 243, 243);
    padding: 10px;
    margin-top: 10px;
    max-height: 200px;
    overflow-y: auto;
}

.loading p {
    color: coral;
    font-size: 18px;
}

.correct-answer {
    color: green;
    font-size: 16px;
}
</style>