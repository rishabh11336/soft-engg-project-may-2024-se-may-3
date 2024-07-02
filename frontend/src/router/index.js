import { createRouter, createWebHistory } from 'vue-router';
import DashBoard from '@/pages/DashBoard.vue';
import CourseComp from '@/components/CourseComp.vue';
import AboutCourse from '@/pages/AboutCourse.vue';
import IntroVideo from '@/pages/IntroVideo.vue';
import GradedAssign from '@/pages/GradedAssign.vue';
import ProgAssign from '@/pages/ProgAssign.vue';
import LectureVideo from '@/pages/LectureVideo.vue';

const routes = [
  { path: '/', component: DashBoard },
  {
    path: '/course',
    component: CourseComp,
    children: [
      { path: 'about', component: AboutCourse },
      { path: 'video', component: IntroVideo },
      { path: ':week/:itemId', component: LectureVideo, props: true },
      { path: 'graded-assignment/:week', component: GradedAssign, props: true },
      { path: 'ppa1', component: ProgAssign },
      { path: '', redirect: 'about' },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
