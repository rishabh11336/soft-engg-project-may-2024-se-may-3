<template>
  <NavBar />
  <div class="dashboard">
    <div class="menu">
      <h4>MY DASHBOARD</h4>
      <p>- My Courses</p>
    </div>
    <div class="container">
      <div class="course-wrapper">
        <span>Python</span>
      </div>
      <div class="link-wrapper">
        <router-link to="/course/about">Go to course ></router-link>
      </div>
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
.dashboard {
  display: flex;
}

.menu {
  width: 250px;
  background-color: #efefef;
  box-shadow: 0px 0px 0px lightgray;
  padding-top: 12px;
  padding-bottom: 12px;
  border-right: solid 1px rgba(0, 0, 0, 0.12);
  margin-right: 10px;
  margin-top: 25px;
  height: 880px;
  padding-left: 20px;
}

.menu h4 {
  padding: 10px;
}

.menu p {
  color: #a0322c;
}

.container {
  width: 250px;
  margin-top: 75px;
  margin-left: 20px;
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
