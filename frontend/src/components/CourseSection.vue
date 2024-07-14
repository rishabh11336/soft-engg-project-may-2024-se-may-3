<template>
  <div class="course-bar">
    <div class="wrapper" @click="toggleContent('introContent')">
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

    <div class="wrapper" @click="toggleContent('week1Content', 1)">
      <div class="first">
        <input type="radio" name="week1" id="intro" />
        <p>Week 1</p>
      </div>
    </div>

    <div class="content-wrapper" v-if="week1Content">
      <div
        class="first"
        v-for="item in weekContent"
        :key="item.id"
        @click="selectItem(item.id)"
        :class="{ selected: selectedItem === item.id }"
      >
        <input
          type="radio"
          name="course-content"
          :id="`intro-${item.id}`"
          :value="item.id"
          v-model="selectedItem"
        />
        <label :for="`intro-${item.id}`">
          <p>
            {{ item.title }}<br />
            <span>{{ item.type }}</span>
          </p>
        </label>
      </div>
      <div class="first" @click="navigateTo('/course/graded-assignment/1')">
        <input type="radio" name="course-content" id="assignment" />
        <label for="assignment">
          <p>
            Graded Assignment <br />
            <span>Assignment</span>
          </p>
        </label>
      </div>
      <div class="first" @click="navigateTo('/course/ppa1')">
        <input type="radio" name="course-content" id="prog-assignment" />
        <label for="prog-assignment">
          <p>
            Programming Assignment <br />
            <span>Assignment</span>
          </p>
        </label>
      </div>
    </div>
  </div>
</template>

<script>
import { getWeekContent } from '@/services/apiServices';
export default {
  name: 'CourseComp',
  data() {
    return {
      introContent: true,
      week1Content: false,
      week2Content: false,
      weekContent: [],
      selectedItem: null,
    };
  },
  methods: {
    navigateTo(route) {
      this.$router.push(route);
    },
    toggleContent(section, week_number) {
      this[section] = !this[section];
      this.fetchWeekContent(week_number);
    },
    fetchWeekContent(week_number) {
      getWeekContent(week_number)
        .then((response) => {
          this.weekContent = response.data;
        })
        .catch((error) => {
          console.error('Error while fetching week content', error);
        });
    },
    selectItem(id) {
      this.selectedItem = id;
      this.$router.push(
        `/course/${this.weekContent.find((item) => item.id === id).week}/${id}`
      );
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
  overflow-y: scroll;
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
  padding: 0px 10px 15px 5px;
  color: #1c1c28;
}

.content-wrapper .first {
  border-bottom: 1px solid rgba(0, 0, 0, 0.12);
}

hr {
  color: rgba(122, 120, 120, 0.12) !important;
  margin-left: -10px;
}

label p,
p {
  margin-left: 10px;
  font-size: 16px;
  color: #49516c;
  padding-left: 10px;
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

.selected {
  border-left: 4px solid #e2b562;
  background-color: #f7f7fa;
}
</style>
