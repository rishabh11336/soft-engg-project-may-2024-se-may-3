import { createRouter, createWebHistory } from 'vue-router';
import DashBoard from '@/pages/DashBoard.vue';
import CourseComp from '@/pages/CourseComp.vue';
import AboutCourse from '@/pages/AboutCourse.vue';
import IntroVideo from '@/pages/IntroVideo.vue';
import GradedAssign from '@/pages/GradedAssign.vue';
import ProgAssign from '@/pages/ProgAssign.vue';
import LectureVideo from '@/pages/LectureVideo.vue';
import CodeEditor from '@/components/CodeEditor.vue';
import GradeDetails from '@/pages/GradeDetails.vue';
import QuizQuestions from '@/pages/QuizQuestions.vue';

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
      { path: 'ppa/:week', component: ProgAssign, props: true },
      { path: '', redirect: 'about' },
      { path: '/CodeEditor', component: CodeEditor },
      { path: '/grade-details', name: 'GradeDetails', component: GradeDetails },
      // { path: '/quiz/:week', name: 'QuizQuestions', component: QuizQuestions },
      { path: '/quiz', name: 'QuizQuestions', component: QuizQuestions },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
