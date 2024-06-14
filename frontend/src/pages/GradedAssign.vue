<template>
  <div>
    <h2>Graded Assignment 1</h2>
    <div class="assignment-wrapper">
      <strong
        >You may submit any number of times before the due date. The final
        submission will be considered for grading.
      </strong>
      <div class="question-answer">
        <div class="question-wrapper">
          <p>1. What is the type of the following expression?</p>
          <strong>1 point</strong>
        </div>
        <div class="question">1 | 1 + 4 / 2</div>
        <div>
          <input type="radio" name="quest1" id="answer" />
          <p>int</p>
        </div>
        <div>
          <input type="radio" name="quest1" id="answer" />
          <p>float</p>
        </div>
        <div>
          <input type="radio" name="quest1" id="answer" />
          <p>str</p>
        </div>
        <div>
          <input type="radio" name="quest1" id="answer" />
          <p>bool</p>
        </div>
      </div>
      <div class="question-answer">
        <div class="question-wrapper">
          <p>2. What is the type of the following expression?</p>
          <strong>1 point</strong>
        </div>
        <div class="question">1 | 1 > 0 and 1 == 1</div>
        <div>
          <input type="radio" name="quest2" id="answer" />
          <p>str</p>
        </div>
        <div>
          <input type="radio" name="quest2" id="answer" />
          <p>True</p>
        </div>
        <div>
          <input type="radio" name="quest2" id="answer" />
          <p>False</p>
        </div>
        <div>
          <input type="radio" name="quest2" id="answer" />
          <p>bool</p>
        </div>
      </div>
      <div class="question-answer">
        <div class="question-wrapper">
          <p>
            3. How does the Python interpreter parenthesize the following
            expression?
          </p>
          <strong>2 points</strong>
        </div>
        <div class="question">1 | 1 + 3 / 4 ** 2 * 0</div>
        <div>
          <input type="radio" name="quest3" id="answer" />
          <p>1 + (((3 / 4) ** 2) * 0)</p>
        </div>
        <div>
          <input type="radio" name="quest3" id="answer" />
          <p>1 + ((3 / (4 ** 2)) * 0)</p>
        </div>
        <div>
          <input type="radio" name="quest3" id="answer" />
          <p>(1 + 3 / 4) ** (2 * 0)</p>
        </div>
        <div>
          <input type="radio" name="quest3" id="answer" />
          <p>All of the above</p>
        </div>
      </div>
      <button type="submit">Submit Answers</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'GradedAssign',
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

.question-answer div {
  display: flex;
}

.question-wrapper {
  display: flex;
  justify-content: space-between;
}

.question {
  background-color: rgb(241, 239, 239);
  height: 15px;
  padding: 10px;
  color: rgb(27, 187, 53);
  font-size: 12px;
  border: 1px solid gray;
  border-radius: 5px;
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
