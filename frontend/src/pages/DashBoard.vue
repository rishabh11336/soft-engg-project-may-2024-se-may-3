<template>
  <NavBar heading="Dashboard" />
  <div class="container">
    <div class="course-wrapper">
      <span>Python</span>
    </div>
    <div class="link-wrapper">
      <router-link to="/course/about">Go to course ></router-link>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue';
export default {
  name: 'DashBoard',
  components: {
    NavBar,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  width: 250px;
  margin-top: 20px;
}

.course-wrapper {
  min-height: 130px;
  background-color: rgb(75, 30, 30);
  padding: 20px 22px 22px 23px;
  border-top-left-radius: 6px;
  border-top-right-radius: 6px;
  font-size: 22px;
}

.course-wrapper span {
  color: white;
  font-weight: 400;
  overflow-wrap: break-word;
}

.link-wrapper {
  text-align: right;
  font-size: 14px;
  margin-top: -1px;
  border-width: 1px;
  border-style: solid;
  border-color: lightgray;
  border-image: initial;
  border-radius: 2px;
  padding: 9px;
}

.link-wrapper a {
  color: rgb(160, 51, 45);
  text-decoration: none;
}
</style>
