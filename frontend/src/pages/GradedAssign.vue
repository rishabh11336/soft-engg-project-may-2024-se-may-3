<template>
  <div v-if="assignments.length">
    <h2>Graded Assignment {{ currentWeekNumber }}</h2>
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
        <button
          class="help-btn"
          @click="fetchQuestionExplanation(question.number)"
        >
          Get help
        </button>
        <div :key="question.number" v-if="showExplanation[question.number]">
          <div v-if="loading[question.number]" class="loading">
            <p>Loading explanation...</p>
          </div>
          <div v-else-if="explanations[question.number]" class="explanation">
            <p><strong>Explanation:</strong></p>
            <p v-html="explanations[question.number]"></p>
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
      currentWeekNumber: null, // Track the current week number
    };
  },
  methods: {
    // method to fetch assignment
    fetchAssignments(weekNumber) {
      getAssignments(weekNumber).then((response) => {
        this.assignments = response.data;
        this.currentWeekNumber = weekNumber;
      });
    },

    // method to submit assignment
    submitAnswers() {
      const submissionData = this.assignments.map((question) => ({
        number: question.number,
        weeknumber: this.currentWeekNumber,
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

    // method to fetch Assignment question explanation
    fetchQuestionExplanation(question_number) {
      this.showExplanation[question_number] =
        !this.showExplanation[question_number];
      this.loading[question_number] = true;
      getTheoryQuestionExplaination(question_number)
        .then((response) => {
          this.explanations[question_number] = this.formattedExplanation(
            response.data.explanation
          );
        })
        .catch((error) => {
          this.explanations[question_number] = this.formattedExplanation(
            'Sorry, something went wrong'
          );
          console.error(error);
        })
        .finally(() => {
          this.loading[question_number] = false;
        });
    },

    // method to format summary
    formattedExplanation(explanation) {
      // Replace newline characters with <br> tags
      return explanation
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>') // Replace **text** with <strong>text</strong>
        .replace(/\n/g, '<br>'); // Replace newline characters with <br> tags;
    },
  },
  mounted() {
    const weekNumber = parseInt(this.$route.params.week);
    if (!isNaN(weekNumber)) {
      this.fetchAssignments(weekNumber);
    } else {
      console.error('Invalid route parameters');
    }
  },

  watch: {
    '$route.params': {
      immediate: true,
      handler(newParams) {
        const weekNumber = parseInt(newParams.week);
        if (!isNaN(weekNumber)) {
          this.fetchAssignments(weekNumber);
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
</style>
