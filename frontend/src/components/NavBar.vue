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
  background-color: #fff;
  font-size: 1.4rem;
  box-shadow: 0 3px 3px 1px #00000012;
  display: flex;
  align-items: center;
  top: 0;
  position: sticky;
  z-index: 1;
  height: 20px;
}

.navbar img {
  width: 120px;
  margin-right: 12px;
  margin-top: 5px;
}

.navbar h5 {
  line-height: 24px;
  color: #212225;
  font-weight: 500;
}
</style>
