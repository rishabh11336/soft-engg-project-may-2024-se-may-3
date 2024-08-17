<template>
  <div v-if="lecture && !loading" class="lecture-container">
    <div class="lecture-content">
      <h2>{{ lecture.index }} {{ lecture.title }}</h2>
      <iframe
        width="960"
        height="480"
        :src="`https://www.youtube.com/embed/${lecture.link}`"
        :title="lecture.title"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin"
        allowfullscreen
      ></iframe>
    </div>
    <div class="transcript">
      <div>{{ lecture.transcript }}</div>
    </div>
  </div>
  <div v-else class="loading">Loading...</div>
</template>

<script>
// Import necessary services or APIs for fetching data
import { getLectureContent } from '@/services/apiServices';

export default {
  name: 'LectureVideo',
  data() {
    return {
      lecture: null, // To store the fetched lecture content
      loading: false,
    };
  },
  methods: {
    fetchWeekContent(itemId) {
      this.loading = true;
      getLectureContent(itemId)
        .then((response) => {
          const filteredItem = response.data;
          if (filteredItem) {
            this.lecture = filteredItem;
          } else {
            console.error('Item not found for week and itemId:', itemId);
          }
        })
        .catch((error) => {
          console.error('Error while fetching week content', error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
  mounted() {
    const itemId = parseInt(this.$route.params.itemId);
    if (!isNaN(itemId)) {
      this.fetchWeekContent(itemId);
    } else {
      console.error('Invalid route parameters');
    }
  },
  watch: {
    '$route.params': {
      immediate: true, // Trigger on component mount
      handler(newParams) {
        const itemId = parseInt(newParams.itemId);
        if (!isNaN(itemId)) {
          this.fetchWeekContent(itemId);
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

.lecture-container {
  max-width: 100%;
}

.loading {
  text-align: center;
  font-size: 30px;
  margin-top: 150px;
}
</style>
