<template>
  <div v-for="week in weeks" :key="week.number">
    <!-- All 12 week header -->
    <div class="wrapper" @click="toggleContent(week.number)">
      <div class="first">
        <input
          type="radio"
          :name="`week${week.number}`"
          :id="`week${week.number}`"
        />
        <p>Week {{ week.number }}</p>
      </div>
    </div>
    <hr v-if="!week.showContent" />
    <div class="content-wrapper" v-if="week.showContent">
      <!-- All 12 week content -->
      <div
        class="first"
        v-for="item in weekContent"
        :key="item.id"
        @click="navigateTo(`/course/${week.number}/${item.id}`)"
      >
        <input type="radio" name="course-content" :id="`intro-${item.id}`" />
        <label :for="`intro-${item.id}`">
          <p>
            {{ item.title }}<br />
            <span>{{ item.type }}</span>
          </p>
        </label>
      </div>
      <!-- Graded Assignment -->

      <div
        v-if="theory_assignments.length > 0"
        class="first"
        @click="navigateTo(`/course/graded-assignment/${week.number}`)"
      >
        <input
          type="radio"
          name="course-content"
          :id="`intro-${week.number}`"
        />
        <label :for="`intro-${week.number}`">
          <p>
            Theory Assignment <br />
            <span>Assignment</span>
          </p>
        </label>
      </div>

      <!-- Conditionally render programming assignments -->
      <div
        v-if="prog_assignments.length > 0"
        class="first"
        @click="navigateTo(`/course/ppa/${week.number}`)"
      >
        <input
          type="radio"
          name="week-content"
          :id="`intro-prog-${week.number}`"
        />
        <label :for="`intro-prog-${week.number}`">
          <p>
            Programming Assignment<br />
            <span> Assignment</span>
          </p>
        </label>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WeekContent',
  props: {
    weeks: {
      type: Array,
      required: true,
    },
    toggleContent: {
      type: Function,
      required: true,
    },
    weekContent: {
      type: Array,
      required: true,
    },
    prog_assignments: {
      type: Array,
      required: true,
    },
    theory_assignments: {
      type: Array,
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
