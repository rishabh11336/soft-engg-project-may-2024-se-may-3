<template>
  <NavBar heading="Python" />
  <div class="course-container">
    <SideBar />
    <CourseMenu />
    <ContentSection />
    <ChatWindow />
  </div>
</template>
<script>
import NavBar from '@/components/NavBar.vue';
import SideBar from '@/components/SideBar.vue';
import CourseMenu from '@/components/CourseMenu.vue';
import ContentSection from '@/components/ContentSection.vue';
import ChatWindow from '@/components/ChatWindow.vue';
export default {
  name: 'CourseComp',
  components: {
    NavBar,
    SideBar,
    CourseMenu,
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
