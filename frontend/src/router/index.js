import { createRouter, createWebHistory } from 'vue-router';
import DashBoard from '@/pages/DashBoard.vue';
import CourseComp from '@/components/CourseComp.vue';
import AboutCourse from '@/pages/AboutCourse.vue';
import VideoLect from '@/pages/VideoLect.vue';
import FirstLecture from '@/pages/FirstLecture.vue';
import SecondLecture from '@/pages/SecondLecture.vue';
import GradedAssign from '@/pages/GradedAssign.vue';
import ProgAssign from '@/pages/ProgAssign.vue';
import CodeEditor  from '@/components/CodeEditor.vue';

const routes = [
  { path: '/', component: DashBoard },
  {
    path: '/course',
    component: CourseComp,
    children: [
      { path: 'about', component: AboutCourse },
      { path: 'video', component: VideoLect },
      { path: 'intro', component: FirstLecture },
      { path: 'intro-to-replit', component: SecondLecture },
      { path: 'graded-assignment', component: GradedAssign },
      { path: 'ppa1', component: ProgAssign },
      { path: '', redirect: 'about' },
      {path: '/CodeEditor', component: CodeEditor}
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
