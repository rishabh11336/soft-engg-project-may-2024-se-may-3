<template>
  <div class="prog-assign-container">
    <div class="prog-assign-header">
      <p>The due date for submitting this assignment has passed.</p>
      <p><strong>Due: </strong> 15 Sep 2021 23:59 IST</p>
    </div>
    <div class="question-note">
      <p>
        Print the first 5 positive integers in ascending order, one number on
        each line.
      </p>
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
      <button
        :class="{ active: activeTab === 'response' }"
        @click="activeTab = 'response'"
      >
        Your Response
      </button>
      <button
        :class="{ active: activeTab === 'solution' }"
        @click="activeTab = 'solution'"
      >
        Solution code
      </button>
    </div>

    <div v-if="activeTab === 'response'" class="editor-container">
      <monaco-editor
        v-model="userCode"
        :language="selectedLanguage"
        theme="vs"
        @input="handleCodeChange"
      ></monaco-editor>
    </div>
    <div v-if="activeTab === 'solution'" class="editor-container">
      <monaco-editor
        v-model="solutionCode"
        :language="selectedLanguage"
        theme="vs"
        @input="handleSolutionCodeChange"
      ></monaco-editor>
    </div>
    <button class="run-btn" @click="runCode">Run</button>
    <div v-if="output" class="output">
      <h3>Output:</h3>
      <pre>{{ output }}</pre>
    </div>
  </div>
</template>

<script>
import MonacoEditor from './MonacoEditor.vue';

export default {
  name: 'ProgAssign',
  components: {
    MonacoEditor,
  },
  data() {
    return {
      selectedLanguage: 'python',
      activeTab: 'response',
      userCode: '',
      solutionCode: '',
      output: '',
      pyodide: null,
    };
  },
  methods: {
    changeLanguage() {
      // This method can be used to perform any additional actions needed when the language changes
    },
    handleCodeChange(newCode) {
      this.userCode = newCode;
    },
    handleSolutionCodeChange(newCode) {
      this.solutionCode = newCode;
    },
    async runCode() {
      if (this.selectedLanguage !== 'python') {
        alert('Only Python is supported for now.');
        return;
      }

      if (!window.pyodide) {
        alert('Pyodide is not loaded yet. Please wait a moment.');
        return;
      }

      try {
        await window.pyodide.loadPackage('micropip');
        const output = await window.pyodide.runPythonAsync(this.userCode);
        this.output = output;
      } catch (err) {
        this.output = `Error: ${err.message}`;
      }
    },
  },
};
</script>

<style>
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
  height: 500px; /* Adjust the height as needed */
  border: 1px solid #ccc;
  border-radius: 4px;
  overflow: hidden;
}

.run-btn {
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
