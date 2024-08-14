<template>
  <div class="content-container">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'ContentSection',
};
</script>
<style>
.content-container {
  margin-left: 30px;
  margin-right: 30px;
  height: 880px;
  margin-top: 55px;
  overflow: auto;
  width: calc(100vw - 350px);
}
</style>
