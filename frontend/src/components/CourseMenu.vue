<template>
  <div class="course-bar">
    <!-- Course Introduction Section -->
    <CourseIntro :introContent="introContent" :toggleIntro="toggleIntro" />

    <!-- Weeks Section -->
    <WeekContent
      :weeks="weeks"
      :toggleContent="toggleContent"
      :weekContent="weekContent"
      :prog_assignments="prog_assignments"
    />
  </div>
</template>

<script>
import {
  getWeekContent,
  getProgrammingAssignments,
} from '@/services/apiServices';
import CourseIntro from './CourseIntro.vue';
import WeekContent from './WeekContent.vue';

export default {
  name: 'CourseMenu',
  components: {
    CourseIntro,
    WeekContent,
  },
  data() {
    return {
      introContent: true,
      weeks: [
        { number: 1, showContent: false },
        { number: 2, showContent: false },
        { number: 3, showContent: false },
        { number: 4, showContent: false },
        { number: 5, showContent: false },
        { number: 6, showContent: false },
        { number: 7, showContent: false },
        { number: 8, showContent: false },
        { number: 9, showContent: false },
        { number: 10, showContent: false },
        { number: 11, showContent: false },
        { number: 12, showContent: false },
      ],
      weekContent: [],
      prog_assignments: [],
      prog_assign_count: 0,
    };
  },
  methods: {
    // method to send route
    navigateTo(route) {
      this.$router.push(route);
    },

    // method to toggle Week Content
    toggleContent(weekNumber) {
      this.weeks.forEach((week) => {
        if (week.number === weekNumber) {
          week.showContent = !week.showContent;
          this.introContent = false;
          if (week.showContent) {
            this.fetchWeekContent(weekNumber);
            this.fetchProgAssignments(weekNumber);
          }
        } else {
          week.showContent = false;
        }
      });
    },

    // toggle method for intro section
    toggleIntro() {
      this.introContent = !this.introContent;
    },

    // fetch method to get week content
    fetchWeekContent(week_number) {
      getWeekContent(week_number)
        .then((response) => {
          this.weekContent = response.data;
        })
        .catch((error) => {
          console.error('Error while fetching week content', error);
        });
    },

    // fetch method to get programming assignment
    fetchProgAssignments(week_number) {
      getProgrammingAssignments(week_number).then((response) => {
        this.prog_assignments = response.data;
        this.prog_assign_count = response.data.length;
      });
    },
  },
};
</script>

<style>
.course-bar {
  min-width: 250px !important;
  max-width: 300px;
  flex: 1 1 25%;
  border-right: 1px solid rgba(0, 0, 0, 0.12);
  transition: max-width 0.2s linear 0s;
  overflow-y: auto;
  margin-left: 80px;
  margin-top: 55px;
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
  border: 1px solid rgba(72, 70, 70, 0.2) !important;
  margin-left: -10px;
}

label p,
p {
  margin-left: 10px;
  font-size: 16px;
  color: #49516c;
}

.intro-label {
  padding: 10px 5px;
  margin-left: 10px;
  color: #49516c;
}

.content-wrapper span {
  color: rgb(173, 169, 169);
  font-size: 12px;
}

input[type='selected'] {
  background-color: aquamarine;
}
</style>
