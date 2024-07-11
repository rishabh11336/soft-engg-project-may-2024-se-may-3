<template>
  <div class="lecture-container">
    <div v-if="lecture" class="lecture-content">
      <h2>{{ lecture.title }}</h2>
      <p>★ ★ ★ ★ ★ -/ 5 (0 reviews) | Submit a review</p>
      <iframe
        width="960"
        height="480"
        :src= "lecture.link"
        :title="lecture.title"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin"
        allowfullscreen
      ></iframe>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
    <div v-if="lecture" class="transcript">
      <div>{{ lecture.transcript }}</div>
    </div>
  </div>
</template>

<script>
// Import necessary services or APIs for fetching data
import { getWeekContent } from '@/services/apiServices';

export default {
  name: 'LectureVideo',
  data() {
    return {
      lecture: null, // To store the fetched lecture content
    };
  },
  methods: {
    fetchWeekContent(week_number, itemId) {
      getWeekContent(week_number)
        .then((response) => {
          const filteredItem = response.data.find((item) => item.id === itemId);
          if (filteredItem) {
            this.lecture = filteredItem;
          } else {
            console.error(
              'Item not found for week and itemId:',
              week_number,
              itemId
            );
          }
        })
        .catch((error) => {
          console.error('Error while fetching week content', error);
        });
    },
  },
  mounted() {
    this.fetchWeekContent();
  },
  watch: {
    '$route.params': {
      immediate: true, // Trigger on component mount
      handler(newParams) {
        const week = parseInt(newParams.week);
        const itemId = parseInt(newParams.itemId);
        if (!isNaN(week) && !isNaN(itemId)) {
          this.fetchWeekContent(week, itemId);
        } else {
          console.error('Invalid route parameters');
        }
      },
    },
  },
};
</script>

<style scoped>
/* Add your component-specific styles here */
.transcript {
  width: 960px;
  height: 200px;
  margin-top: 20px;
  background-color: whitesmoke;
  padding: 10px;
  border-radius: 5px;
  color: rgb(59, 58, 58);
  overflow-y: scroll;
  font-size: 16px;
  line-height: 1.5;
}
</style>
