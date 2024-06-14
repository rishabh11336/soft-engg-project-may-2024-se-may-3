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
  margin-top: 20px;
  width: calc(100% - 400px);
}
</style>
