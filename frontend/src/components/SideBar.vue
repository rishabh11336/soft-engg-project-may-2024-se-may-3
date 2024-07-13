<template>
  <div class="sidebar">
    <div :class="{ active: activeTab === 'module' }" class="module" @click="activeTab = 'module'">
      <img :src="moduleLogo" alt="module" />
      <div>Module</div>
    </div>
    <div class="module" :class="{ active: activeTab === 'grade-details' }" @click="activateGradeDetails">
      <svg width="24" height="26" viewBox="0 0 24 26" fill="none" xmlns="http://www.w3.org/2000/svg">
        <g clip-path="url(#clip0_1_146)">
          <path
            d="M22.6555 8.56802V0.732995C22.6555 0.328426 22.3386 0 21.9482 0H7.90139C7.68441 0 7.48996 0.10203 7.36016 0.261929L1.54972 6.4802C1.416 6.62233 1.34988 6.80609 1.34988 6.99036C1.34988 7.51624 1.34939 8.04264 1.34939 8.56954C1.28816 8.55584 1.22547 8.54975 1.16229 8.54975C0.849796 8.54975 0.578939 8.71624 0.378613 8.95381C0.161144 9.20964 0 9.61117 0 9.94619V24.6584C0 25.0274 0.14596 25.364 0.380083 25.6061C0.614204 25.8487 0.93845 26 1.29502 26H22.705C23.0616 26 23.3858 25.8487 23.6199 25.6061C23.854 25.364 24 25.0274 24 24.6584V9.94619C24 9.60914 23.833 9.19949 23.6101 8.94061C23.5259 8.84315 23.4274 8.75685 23.3211 8.69188L23.3143 8.68832C23.1713 8.60102 23.0116 8.54873 22.8372 8.54873C22.7765 8.54873 22.7158 8.55533 22.6555 8.56802ZM1.58939 24.5335L9.28604 17.5431L11.6557 19.6878C11.9197 19.9274 12.3213 19.931 12.5897 19.6822L14.8222 17.6147L22.4395 24.5335H1.58939ZM8.21535 16.5731L1.41502 22.7492V10.4162L1.44147 10.4401C1.51935 10.5817 1.64229 10.6934 1.78922 10.7548L8.21535 16.5731ZM22.585 22.7228L15.8811 16.6345L22.585 10.4269V22.7228ZM2.76294 9.69645V7.95939H8.64245C9.03282 7.95939 9.34972 7.63096 9.34972 7.2264V1.4665H21.241V9.71421L14.376 16.07L14.3221 16.1203L12.1146 18.164L2.76294 9.69645ZM3.50204 6.49289L7.93518 1.74873V6.49289H3.50204Z"
            fill="white" />
        </g>
        <defs>
          <clipPath id="clip0_1_146">
            <rect width="24" height="26" fill="white" transform="matrix(-1 0 0 1 24 0)" />
          </clipPath>
        </defs>
      </svg>
      <div>Grades</div>
    </div>
    <div :class="{ active: activeTab === 'ide' }" class="module" @click="activeTab = 'ide'">
      <img :src="codeIDELogo" alt="ide" @click="openModal" />

      <div>Code IDE</div>
    </div>
    <IdeModal :show="isModalOpen" @close="isModalOpen = false">
      <CodeEditor />
    </IdeModal>
  </div>
</template>
<script>
import moduleLogo from '../assets/module.png';
import codeIDELogo from '../assets/ide.png';
import IdeModal from './IdeModal.vue';
import CodeEditor from './CodeEditor.vue';

export default {
  name: 'SideBar',
  components: {
    IdeModal,
    CodeEditor,
  },
  data() {
    return {
      moduleLogo,
      codeIDELogo,
      activeTab: 'module',
      isModalOpen: false,
    };
  },
  methods: {
    openModal() {
      console.log("Modal toggled");
      this.isModalOpen = true;
    },
    activateGradeDetails() {
      this.activeTab = 'grade-details';
      this.grade_details();
    },
    grade_details() {
      this.$router.push({ name: 'GradeDetails' });
    }
  }
};
</script>
<style>
.sidebar {
  width: max-content;
  overflow-y: auto;
  background-color: #49516c;
  padding-top: 12px;
  padding-bottom: 12px;
  border-right: solid 1px rgba(0, 0, 0, 0.12);
  margin-right: 10px;
  position: fixed;
  margin-left: -10px;
  margin-top: 25px;
  height: 100%;
  z-index: 0;
}

.sidebar .module {
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 16px 8px;
  position: relative;
}

.sidebar div.active div {
  color: coral !important;
}

.sidebar .module div {
  color: #fff;
  width: 100%;
  text-align: center;
  margin-top: 4px;
  font-size: 0.9em;
}

.module img {
  width: 50px;
  height: 50px;
}
</style>
