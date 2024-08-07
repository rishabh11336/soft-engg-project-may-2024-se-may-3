<template>
  <div v-if="assignments">
    <h2>Graded Assignment 1</h2>
    <div class="assignment-wrapper">
      <strong>
        You may submit any number of times before the due date. The final
        submission will be considered for grading.
      </strong>
      <div
        class="question-answer"
        v-for="question in assignments"
        :key="question.number"
      >
        <div class="question-wrapper">
          <p>{{ question.question }}</p>
          <strong>1 point</strong>
        </div>
        <div class="question">{{ question.code_snippet }}</div>
        <div v-if="question.type === 'Multi-choice'">
          <div v-if="question.option4">
            <input
              type="radio"
              :name="`answer_${question.number}`"
              :id="`option1_${question.number}`"
              :value="question.option1"
              v-model="selectedAnswers[question.number]"
            />
            <label :for="`option1_${question.number}`">{{
              question.option1
            }}</label>
          </div>
          <div v-if="question.option4">
            <input
              type="radio"
              :name="`answer_${question.number}`"
              :id="`option2_${question.number}`"
              :value="question.option2"
              v-model="selectedAnswers[question.number]"
            />
            <label :for="`option2_${question.number}`">{{
              question.option2
            }}</label>
          </div>
          <div v-if="question.option4">
            <input
              type="radio"
              :name="`answer_${question.number}`"
              :id="`option3_${question.number}`"
              :value="question.option3"
              v-model="selectedAnswers[question.number]"
            />
            <label :for="`option3_${question.number}`">{{
              question.option3
            }}</label>
          </div>
          <div v-if="question.option4">
            <input
              type="radio"
              :name="`answer_${question.number}`"
              :id="`option4_${question.number}`"
              :value="question.option4"
              v-model="selectedAnswers[question.number]"
            />
            <label :for="`option4_${question.number}`">{{
              question.option4
            }}</label>
          </div>
        </div>
        <div v-else>
          <div class="answer">
            <input
              type="number"
              placeholder="Answer..."
              v-model="selectedAnswers[question.number]"
            />
          </div>
        </div>
        <button class="help-btn" @click="fetchQuestionTheory(question.number)">
          Get help
        </button>
        <div :key="question.number" v-if="showExplanation[question.number]">
          <div v-if="loading[question.number]">
            <p>Loading explaination...</p>
          </div>
          <div v-else-if="explanations[question.number]">
            <p>{{ explanations[question.number] }}</p>
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
import {
  getAssignments,
  submitAnswers,
  getTheoryQuestionExplaination,
} from '@/services/apiServices';

export default {
  name: 'GradedAssign',
  data() {
    return {
      assignments: [],
      selectedAnswers: {},
      explanations: {},
      loading: {},
      showExplanation: {},
    };
  },
  methods: {
    fetchAssignments(week_number) {
      getAssignments(week_number).then((response) => {
        this.assignments = response.data;
      });
    },

    submitAnswers() {
      const submissionData = this.assignments.map((question) => ({
        number: question.number,
        weeknumber: question.weeknumber,
        submitted_answers: [
          this.selectedAnswers[question.number] || '',
          '',
          '',
          '',
        ],
      }));

      submissionData.forEach((submission) => {
        submitAnswers(submission)
          .then((response) => {
            console.log('Submission successful:', response.data);
          })
          .catch((error) => {
            console.error('Error submitting answers:', error);
          });
      });
    },

    fetchQuestionTheory(question_number) {
      this.showExplanation[question_number] =
        !this.showExplanation[question_number];
      this.loading[question_number] = true;
      getTheoryQuestionExplaination(question_number)
        .then((response) => {
          this.explanations[question_number] = response.data.explanation;
        })
        .catch((error) => {
          console.error(error);
        })
        .finally(() => {
          this.loading[question_number] = false;
        });
    },
  },
  watch: {
    '$route.params': {
      immediate: true, // Trigger on component mount
      handler(newParams) {
        const week = parseInt(newParams.week);
        if (!isNaN(week)) {
          this.fetchAssignments(week);
        } else {
          console.error('Invalid route parameters');
        }
      },
    },
  },
};
</script>

<style scoped>
.assignment-wrapper {
  background-color: rgb(247, 246, 246);
  padding: 15px;
  height: 800px;
  overflow-y: auto;
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
  height: 15px;
  padding: 10px;
  color: rgb(8, 25, 250);
  font-size: 12px;
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
</style>
