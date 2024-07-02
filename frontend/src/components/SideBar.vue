<template>
  <div class="sidebar">
    <div
      :class="{ active: activeTab === 'module' }"
      class="module"
      @click="activeTab = 'module'"
    >
      <img :src="moduleLogo" alt="module" />
      <div>Module</div>
    </div>
    <div
      :class="{ active: activeTab === 'ide' }"
      class="module"
      @click="activeTab = 'ide'"
    >
      <img :src="codeIDELogo" alt="ide" />

      <div>Code IDE</div>
    </div>
  </div>
</template>
<script>
import moduleLogo from '../assets/module.png';
import codeIDELogo from '../assets/ide.png';
export default {
  name: 'SideBar',
  data() {
    return {
      moduleLogo,
      codeIDELogo,
      activeTab: 'module',
    };
  },
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
