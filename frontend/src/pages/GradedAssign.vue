<template>
  <div v-if="assignments">
    <h2>Graded Assignment 1</h2>
    <div class="assignment-wrapper">
      <strong>
        You may submit any number of times before the due date. The final
        submission will be considered for grading.
      </strong>
      <form @submit.prevent="submitAnswers">
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
              <label :for="`option1_${question.number}`">{{ question.option1 }}</label>
            </div>
            <div v-if="question.option4">
              <input
                type="radio"
                :name="`answer_${question.number}`"
                :id="`option2_${question.number}`"
                :value="question.option2"
                v-model="selectedAnswers[question.number]"
              />
              <label :for="`option2_${question.number}`">{{ question.option2 }}</label>
            </div>
            <div v-if="question.option4">
              <input
                type="radio"
                :name="`answer_${question.number}`"
                :id="`option3_${question.number}`"
                :value="question.option3"
                v-model="selectedAnswers[question.number]"
              />
              <label :for="`option3_${question.number}`">{{ question.option3 }}</label>
            </div>
            <div v-if="question.option4">
              <input
                type="radio"
                :name="`answer_${question.number}`"
                :id="`option4_${question.number}`"
                :value="question.option4"
                v-model="selectedAnswers[question.number]"
              />
              <label :for="`option4_${question.number}`">{{ question.option4 }}</label>
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
        </div>
        <button type="submit">Submit Answers</button>
      </form>
    </div>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script>
import { getAssignments, submitAnswers } from '@/services/apiServices';

export default {
  name: 'GradedAssign',

  data() {
    return {
      assignments: [],
      selectedAnswers: {},
    };
  },
  methods: {
    fetchAssignments(week_number) {
      getAssignments(week_number).then((response) => {
        this.assignments = response.data;
        console.log(this.assignments);
      });
    },
    submitAnswers() {
      const submissionData = this.assignments.map((question) => ({
        number: question.number,
        weeknumber: question.weeknumber,
        submitted_answers: [
          this.selectedAnswers[question.number] || "",
          "",
          "",
          ""
        ],
      }));
      
      submissionData.forEach(submission => {
        submitAnswers(submission)
          .then(response => {
            console.log("Submission successful:", response.data);
          })
          .catch(error => {
            console.error("Error submitting answers:", error);
          });
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
<style>
.assignment-wrapper {
  background-color: rgb(247, 246, 246);
  padding: 15px;
  height: 800px;
  overflow-y: auto;
  position: relative;
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
  background-color: rgb(241, 239, 239);
  height: 15px;
  padding: 10px;
  color: rgb(27, 187, 53);
  font-size: 12px;
  border: 1px solid gray;
  border-radius: 5px;
  margin-bottom: 5px;
}

.answer input {
  width: 50px;
  padding: 5px;
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
}
</style>
