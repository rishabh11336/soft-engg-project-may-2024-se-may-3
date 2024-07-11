<template>
  <div class="navbar">
    <router-link to="/"><img :src="LogoIcon" alt="logo" /></router-link>
    <h5>{{ heading }}</h5>
  </div>
</template>
<script>
import LogoIcon from '@/assets/iitm-logo.png';
export default {
  name: 'NavBar',
  props: {
    heading: {
      type: String,
      required: true,
    },
  },
  data() {
    return { LogoIcon };
  },
};
</script>
<style>
.navbar {
  width: 100%;
  padding: 15px 16px 20px 20px;
  background-color: #efefef;
  font-size: 1.4rem;
  box-shadow: 0 3px 3px 1px #00000012;
  display: flex;
  align-items: center;
  top: 0;
  position: fixed;
  z-index: 1;
  height: 20px;
  margin-left: -10px;
  border-bottom: 2px solid rgb(210, 205, 205);
}

.navbar img {
  width: 120px;
  margin-right: 12px;
  margin-top: 5px;
}

.navbar h5 {
  font-size: 16px;
  line-height: 24px;
  color: #49516c;
  font-weight: 500;
}
</style>
