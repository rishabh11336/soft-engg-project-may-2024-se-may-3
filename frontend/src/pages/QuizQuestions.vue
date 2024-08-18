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
          <pre>{{ question.code_snippet }}</pre>
        </div>
        <div v-if="question.question_type === 'Multi-choice'"> 
          <div v-for="optionNum in 4" :key="optionNum">
            <div v-if="question[`option${optionNum}`]">
              <input
                type="radio"
                :name="`answer_${question.id}`"
                :id="`option${optionNum}_${question.id}`"
                :value="question[`option${optionNum}`]"
                v-model="selectedAnswers[question.id]"
                :disabled="true"
              />
              <label :for="`option${optionNum}_${question.id}`">{{ question[`option${optionNum}`] }}</label>
            </div>
          </div>
        </div>
        <div v-else>
          <div class="answer">
            <input
              type="text"
              :value="selectedAnswers[question.id]"
              disabled
            />
          </div>
        </div>
        <div class="feedback" :class="getFeedbackClass(question)">
          <p v-if="isCorrect(question)">Correct!</p>
          <p v-else>
            Incorrect. The correct answer is: {{ question.answer1 }}
          </p>
        </div>
      </div>
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
          this.initializeSelectedAnswers();
        })
        .catch((error) => {
          console.error('Error fetching quiz questions:', error);
        });
    },
    initializeSelectedAnswers() {
      this.quizQuestions.forEach(question => {
        this.selectedAnswers[question.id] = question.youranswer1;
      });
    },
    isCorrect(question) {
      return question.youranswer1 === question.answer1;
    },
    getFeedbackClass(question) {
      return this.isCorrect(question) ? 'correct' : 'incorrect';
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

.feedback {
  margin-top: 10px;
  padding: 5px;
  border-radius: 4px;
}
.correct {
  background-color: #d4edda;
  color: #155724;
}
.incorrect {
  background-color: #f8d7da;
  color: #721c24;
}
pre {
  background-color: #f4f4f4;
  padding: 10px;
  border-radius: 4px;
  overflow-x: auto;
}

</style>