<template>
  <div class="sidebar">
    <div class="module active">
      <img :src="moduleLogo" alt="module" />
      <div>Module</div>
    </div>
    <div class="module">
      <img :src="codeIDELogo" alt="module" />

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
    };
  },
};
</script>
<style>
.sidebar {
  width: max-content;
  height: 881px;
  overflow-y: auto;
  top: 16px;
  bottom: 16px;
  width: max-content;
  background-color: #49516c;
  padding-top: 12px;
  padding-bottom: 12px;
  border-right: solid 1px rgba(0, 0, 0, 0.12);
  margin-right: 10px;
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

.sidebar .active div {
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
