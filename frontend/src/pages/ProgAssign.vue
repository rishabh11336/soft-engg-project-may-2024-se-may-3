<template>
  <div class="prog-assign-container" v-if="assignment">
    <div class="prog-assign-header">
      <p>The due date for submitting this assignment has passed.</p>
      <p><strong>Due: </strong> 15 Sep 2021 23:59 IST</p>
    </div>
    <div class="question-note">
      <p>{{ assignment.question }}</p>
      <button class="help-btn" @click="fetchProgrammingQuestionTheory(assignment.id)">
        Get help
      </button>
      <div :key="assignment.id" v-if="showExplanation">
        <div v-if="loading" class="loading">
          <p>Loading explanation...</p>
        </div>
        <div v-else-if="explanation" class="explaination">
          <div><strong>Explanation:</strong> {{ explanation }}</div>
        </div>
      </div>
      <p>
        Note: Do not worry about the
        <strong style="color: red; font-weight: 200">\n </strong>that you
        observe in the expected output. It can be ignored.
      </p>
      <p class="instruction">
        This assignment has public test cases. Please click on "Test Run" button
        to see the status of public test cases. Assignment will be evaluated
        only after submitting using "Submit" button below. If you only test run
        the program, your assignment will not be graded and you will not see
        your score after the deadline.
      </p>
    </div>
    <div class="header">
      <select v-model="selectedLanguage" @change="changeLanguage">
        <option value="" disabled>Choose Language</option>
        <option value="python">Python3</option>
        <!-- Add more languages as needed -->
      </select>
    </div>

    <div class="tabs">
      <button :class="{ active: activeTab === 'response' }" @click="activeTab = 'response'">
        Your Response
      </button>
      <button :class="{ active: activeTab === 'solution' }" @click="activeTab = 'solution'">
        Solution code
      </button>
    </div>

    <div v-if="activeTab === 'response'" class="editor-container">
      <codemirror v-model="userCode" placeholder="Write your code here..." :style="{ height: '100%', width: '100%' }"
        :autofocus="true" :indent-with-tab="true" :tab-size="2" :extensions="extensions" @ready="handleReady" />
    </div>
    <div v-if="activeTab === 'solution'" class="editor-container">
      <codemirror v-model="solutionCode" placeholder="Solution..." :style="{ height: '100%', width: '100%' }"
        :autofocus="true" :indent-with-tab="true" :tab-size="2" :extensions="extensions" @ready="handleReady" />
    </div>


    <p class="msg">(Please run code before submitting)</p>
    <div class="btn-container">
      <button @click="runCode" class="run-btn">Run</button>
      <button @click="submitAnswers" :disabled="!isSubmitEnabled">Submit</button>
    </div>

    <!-- <div class="console">
      <h2 class="console-header">Console</h2>
      <hr>
      <pre>>>> {{ output }}</pre>
    </div> -->
    <div class="test-cases">
      <h3>Public Test Cases:</h3>
      <div v-for="(testCase, index) in publicTestCases" :key="index" class="test-case">
        <p><strong>Test Case {{ index + 1 }}:</strong> Input: {{ testCase.input }}</p>
        <div class="test-case-results">
          <div>
            <label>Expected Output:</label>
            <pre>{{ testCase.expectedOutput }}</pre>
          </div>
          <div>
            <label>Your Output:</label>
            <pre
              :class="{ passed: testCase.userOutput === testCase.expectedOutput, failed: testCase.userOutput !== testCase.expectedOutput }">{{ testCase.userOutput }}</pre>
          </div>
        </div>
      </div>
    </div>
    <!-- <div class="test-cases">
      <h3>Private Test Cases:</h3>
      <div v-for="(testCase, index) in privateTestCases" :key="index" class="test-case">
        <p><strong>Test Case {{ index + 1 }}:</strong> Input: {{ testCase.input }}</p>
        <div class="test-case-results">
          <div>
            <label>Expected Output:</label>
            <pre>{{ testCase.expectedOutput }}</pre>
          </div>
          <div>
            <label>Your Output:</label>
            <pre
              :class="{ passed: testCase.userOutput === testCase.expectedOutput, failed: testCase.userOutput !== testCase.expectedOutput }">{{ testCase.userOutput }}</pre>
          </div>
        </div>
      </div>
    </div> -->

  </div>
  <div v-else>
    Loading assignment...
  </div>
</template>

<script>
import { defineComponent, ref, shallowRef } from 'vue';
import { Codemirror } from 'vue-codemirror';
import { python } from '@codemirror/lang-python';
import {
  getProgrammingAssignments,
  submitProgrammingAssignments,
  getProgrammingQuestionExplaination,
  runProgAssignCode,
} from '@/services/apiServices';

export default defineComponent({
  name: 'ProgAssign',
  components: {
    Codemirror,
  },

  setup() {
    const selectedLanguage = ref('python');
    const activeTab = ref('response');
    const userCode = ref('');
    const solutionCode = ref('');
    const output = ref('');
    const extensions = [python()];
    const view = shallowRef(null);
    const assignments = ref([]);
    const publicTestCases = ref([]);
    const privateTestCases = ref([]);
    const assignment = ref(null);
    const userOutputs = ref([]);
    const explanation = ref('');
    const loading = ref(false);
    const showExplanation = ref(false);
    const isSubmitEnabled = ref(false);

    const handleReady = (payload) => {
      view.value = payload.view;
    };

    // #3
    const runCode = async () => {
      if (selectedLanguage.value !== 'python') {
        alert('Only Python is supported for now.');
        return;
      }

      try {
        console.log(`Running code: ${userCode.value}`);

        const results = {
          public: [],
          private: []
        };

        // Running public test cases
        for (const testCase of publicTestCases.value) {
          console.log(`Running test case with input: ${testCase.input}`);
          const response = await runProgAssignCode({
            code: userCode.value,
            input: String(testCase.input)  // Passing input as string
          });
          const userOutput = response.data.output.trim();

          testCase.userOutput = userOutput;
          results.public.push({
            ...testCase,
            passed: userOutput === testCase.expectedOutput
          });
        }

        // Running private test cases
        for (const testCase of privateTestCases.value) {
          console.log(`Running test case with input: ${testCase.input}`);
          const response = await runProgAssignCode({
            code: userCode.value,
            input: String(testCase.input)
          });
          const userOutput = response.data.output.trim();

          testCase.userOutput = userOutput;
          results.private.push({
            ...testCase,
            passed: userOutput === testCase.expectedOutput
          });
        }

        output.value = `Public Test Cases: ${results.public.filter(r => r.passed).length} passed, ${results.public.filter(r => !r.passed).length} failed\n`;
        output.value += `Private Test Cases: ${results.private.filter(r => r.passed).length} passed, ${results.private.filter(r => !r.passed).length} failed\n`;

        isSubmitEnabled.value = true;

      } catch (err) {
        console.error('Error running code:', err);
        output.value = `Error: ${err.message}`;
        isSubmitEnabled.value = true;
      }
    };


    // fetch Porgramming questions
    const fetchProgAssignments = (week_number) => {
      getProgrammingAssignments(week_number).then((response) => {
        assignments.value = response.data;
        assignment.value = response.data[0]; // assuming one assignment for now
        publicTestCases.value = [
          {
            input: assignment.value.public_test_case1,
            expectedOutput: assignment.value.output_public_test_case1,
            userOutput: '',
          },
          {
            input: assignment.value.public_test_case2,
            expectedOutput: assignment.value.output_public_test_case2,
            userOutput: '',
          },
          {
            input: assignment.value.public_test_case3,
            expectedOutput: assignment.value.output_public_test_case3,
            userOutput: '',
          },
        ];
        privateTestCases.value = [
          {
            input: assignment.value.private_test_case1,
            expectedOutput: assignment.value.output_private_test_case1,
            userOutput: '',
          },
          {
            input: assignment.value.private_test_case2,
            expectedOutput: assignment.value.output_private_test_case2,
            userOutput: '',
          },
          {
            input: assignment.value.private_test_case3,
            expectedOutput: assignment.value.output_private_test_case3,
            userOutput: '',
          },
        ];
      });
    };

    // submit answer method
    const submitAnswers = () => {
      const submissionData = {
        assignment_id: assignment.value.id,
        weeknumber: assignment.value.weeknumber,
        user_output_public_test_case1: publicTestCases.value[0].userOutput,
        user_output_public_test_case2: publicTestCases.value[1].userOutput,
        user_output_public_test_case3: publicTestCases.value[2].userOutput,
        user_output_private_test_case1: privateTestCases.value[0].userOutput,
        user_output_private_test_case2: privateTestCases.value[1].userOutput,
        user_output_private_test_case3: privateTestCases.value[2].userOutput,
        submitted_code: userCode.value,
      };

      submitProgrammingAssignments(submissionData)
        .then(response => {
          console.log("Submission successful:", response.data);

          const marks = response.data.marks_awarded;

          window.alert(`Submission Successful!\nMarks: ${marks}`);
        })
        .catch(error => {
          console.error("Error submitting answers:", error);
        });
    };

    // fetch Programming question explanation
    const fetchProgrammingQuestionTheory = (question_id) => {
      showExplanation.value = !showExplanation.value;
      loading.value = true;
      getProgrammingQuestionExplaination(question_id)
        .then((response) => {
          explanation.value = response.data.explanation;
        })
        .catch((error) => {
          console.error(error);
          explanation.value = 'Sorry, something went wrong';
        })
        .finally(() => {
          loading.value = false;
        });
    };

    return {
      selectedLanguage,
      activeTab,
      userCode,
      solutionCode,
      output,
      extensions,
      view,
      assignments,
      publicTestCases,
      privateTestCases,
      userOutputs,
      assignment,
      handleReady,
      runCode,
      fetchProgAssignments,
      submitAnswers,
      showExplanation,
      explanation,
      loading,
      fetchProgrammingQuestionTheory,
      isSubmitEnabled,
    };
  },

  watch: {
    '$route.params': {
      immediate: true, // Trigger on component mount
      handler(newParams) {
        const week = parseInt(newParams.week);
        if (!isNaN(week)) {
          this.fetchProgAssignments(week);
        } else {
          console.error('Invalid route parameters');
        }
      },
    },
  },
});
</script>

<style scoped>
.prog-assign-header {
  background-color: brown;
  padding: 10px;
}

.prog-assign-header p {
  color: white;
}

.question-note p {
  font-size: 16px;
}

.instruction {
  font-weight: bold;
  font-size: 15px;
  color: red;
}

.header {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin-bottom: 10px;
}

select {
  width: 350px;
  padding: 10px;
  border-radius: 5px;
  background-color: white;
  border: 1px solid lightgray;
  color: #212529;
  font-size: 14px;
}

.tabs {
  display: flex;
  border-bottom: 2px solid #ccc;
  margin-bottom: 10px;
}

.tabs button {
  padding: 10px 20px;
  border: none;
  border-bottom: 2px solid transparent;
  background: none;
  cursor: pointer;
  color: black;
}

.tabs button.active {
  border-bottom: 2px solid #a0332d;
  color: #a0332d;
}

.editor-container {
  height: 200px;
  /* Adjust the height as needed */
  border: 1px solid #ccc;
  border-radius: 4px;
  overflow: hidden;
  cursor: text;
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
  margin-bottom: 30px;
}

.run-button {
  margin-top: 8px;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  background-color: #4caf50;
  color: white;
  cursor: pointer;
}

.output {
  margin-top: 20px;
}

.test-cases,
.console {
  margin-top: 5px;
  max-height: 400px;
  overflow-y: auto;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding-right: 10px;
  padding-left: 10px;
}

.test-case {
  margin-bottom: 10px;
}

.test-case-results {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.test-case-results>div {
  flex: 1;
  margin-right: 10px;
}

.btn-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.run-btn {
  margin-right: 8px;
}

.explaination {
  background-color: rgb(233, 228, 228);
  padding: 5px 10px;
  margin-top: 10px;
}

.help-btn {
  margin: auto;
}

.loading p {
  color: coral;
  font-size: 18px;
}

.msg {
  font-size: small;
  text-align: center;
}

.btn-container button:disabled {
  background-color: #d3d3d3;
  /* Light gray background for disabled state */
  cursor: not-allowed;
  /* Not-allowed cursor */
  color: #a1a1a1;
  /* Light gray text for disabled state */
}

.btn-container button:disabled:hover {
  cursor: not-allowed;
}
</style>
