<template>
  <NavBar heading="Python" />
  <div class="course-container">
    <SideBar />
    <CourseSection />
    <ContentSection />
    <ChatWindow />
  </div>
</template>
<script>
import NavBar from './NavBar.vue';
import SideBar from './SideBar.vue';
import CourseSection from './CourseSection.vue';
import ContentSection from './ContentSection.vue';
import ChatWindow from './ChatWindow.vue';

export default {
  name: 'CourseComp',
  components: {
    NavBar,
    SideBar,
    CourseSection,
    ContentSection,
    ChatWindow,
  },
};
</script>
<style>
.course-container {
  display: flex;
  height: 910px;
}
</style>
