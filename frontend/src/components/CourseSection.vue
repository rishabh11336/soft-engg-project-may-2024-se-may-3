<template>
  <div class="course-bar">
    <div class="wrapper" @click="toggleContent('introContent')">
      <div class="first">
        <input type="radio" name="course" id="intro" />
        <p>Course Introduction</p>
      </div>
    </div>

    <hr v-if="!introContent" />

    <div class="content-wrapper" v-if="introContent">
      <div class="first" @click="navigateTo('/course/about')">
        <input type="radio" name="course-content" id="intro" />
        <p>About the Course</p>
      </div>
      <div class="first" @click="navigateTo('/course/video')">
        <input type="radio" name="course-content" id="intro" />
        <p>
          How to submit a programming assignment
          <br />
          <span>Video</span>
        </p>
      </div>
    </div>
    <div class="wrapper" @click="toggleContent('week1Content')">
      <div class="first">
        <input type="radio" name="week1" id="intro" />
        <p>Week1</p>
      </div>
    </div>
    <div class="content-wrapper" v-if="week1Content">
      <div class="first" @click="navigateTo('/course/intro')">
        <input type="radio" name="week1-content" id="intro" />
        <p>
          L1.1: Indtroduction<br />
          <span>Video</span>
        </p>
      </div>
      <div class="first" @click="navigateTo('/course/intro-to-replit')">
        <input type="radio" name="week1-content" id="intro" />
        <p>
          L1.2: Introduction to Replit<br />
          <span>Video</span>
        </p>
      </div>
      <div class="first" @click="navigateTo('/course/graded-assignment')">
        <input type="radio" name="week1-content" id="intro" />
        <p>
          Graded Assignment 1<br />
          <span>Assignment</span>
        </p>
      </div>
      <div class="first" @click="navigateTo('/course/ppa1')">
        <input type="radio" name="week1-content" id="intro" />
        <p>
          PPA 1 - Not Graded<br />
          <span>Programming Assignment</span>
        </p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'CourseComp',
  data() {
    return {
      introContent: true,
      week1Content: false,
    };
  },
  methods: {
    navigateTo(route) {
      this.$router.push(route);
    },
    toggleContent(section) {
      this[section] = !this[section];
    },
  },
};
</script>

<style>
.course-bar {
  min-width: 150px;
  max-width: 300px;
  flex: 1 1 25%;
  border-right: 1px solid rgba(0, 0, 0, 0.12);
  transition: max-width 0.2s linear 0s;
}

div {
  cursor: pointer;
}

.course-bar section {
  height: 869px;
  overflow-y: auto;
}

.wrapper {
  padding: 10px;
  color: #1c1c28;
}

.wrapper .first p {
  font-weight: bold;
  font-size: 16px;
}

.first {
  display: flex;
  justify-content: start;
}

.content-wrapper {
  display: block;
  padding: 0px 10px 15px 15px;
  color: #1c1c28;
}

.content-wrapper .first {
  border-bottom: 1px solid rgba(0, 0, 0, 0.12);
}

hr {
  color: rgba(122, 120, 120, 0.12) !important;
  margin-left: -10px;
}

p {
  margin-left: 10px;
}

.content-wrapper span {
  color: rgb(173, 169, 169);
  font-size: 12px;
}
</style>
