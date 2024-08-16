<template>
  <!-- Course Introduction Section -->
  <div class="wrapper" @click="toggleIntro">
    <div class="first">
      <input type="radio" name="course" id="course-intro" />
      <p>Course Introduction</p>
    </div>
  </div>

  <hr v-if="!introContent" />

  <div class="content-wrapper" v-if="introContent">
    <div class="first" @click="navigateTo('/course/about')">
      <input type="radio" name="course-content" id="about" />
      <label for="about" class="intro-label">About the Course</label>
    </div>
    <div class="first" @click="navigateTo('/course/video')">
      <input type="radio" name="course-content" id="intro" />
      <label for="intro" class="intro-label">
        How to submit a programming assignment
        <br />
        <span>Video</span>
      </label>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CourseIntro',
  props: {
    introContent: {
      type: Boolean,
      required: true,
    },
    toggleIntro: {
      type: Function,
      required: true,
    },
  },
  methods: {
    navigateTo(route) {
      this.$router.push(route);
    },
  },
};
</script>
