<template>
  <div ref="chatWindow">
    <button @click="handleSummarise()" v-if="showSummary" class="btn-summarise">
      Summarise Video
    </button>
    <div class="chat-window">
      <button @click="handleWindow()" v-if="!isShow" class="btn-chat">
        Open Chat
      </button>
      <div class="chat-window-container" v-if="isShow">
        <div class="close-btn" @click="handleWindow()">
          <img :src="closeIcon" alt="" />
        </div>
        <div class="chat-header">
          <div>
            <p>Chat Window</p>
            <div class="export" @click="handleExport()">
              <img :src="downloadIcon" alt="" />
            </div>
          </div>
        </div>
        <div class="chat-wrapper" v-if="!loading && chatList">
          <div v-for="chat in chatList" :key="chat.id">
            <div class="sender" v-if="chat.sender">
              <p>{{ chat.sender }}</p>
            </div>
            <div class="receiver" v-if="chat.receiver">
              <p>{{ chat.receiver }}</p>
            </div>
          </div>
        </div>
        <div v-else-if="!loading && !chatList && errorMessage">
          <p>Something went wrong</p>
        </div>
        <div v-else class="loading">
          <p>Loading ....</p>
        </div>
        <div class="chat-input">
          <input
            v-model="userQuery"
            type="text"
            name=""
            id=""
            placeholder="Type your query here ....."
            @keyup.enter="handleDoubtBot()"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import downloadIcon from '../assets/download.svg';
import closeIcon from '../assets/close.svg';
import { getLectureSummary, getDoubtBotHelp} from '@/services/apiServices';


export default {
  name: 'ChatWindow',
  data() {
    return {
      isShow: false,
      loading: false,
      showSummary: true,
      errorMessage: false,
      downloadIcon,
      closeIcon,
      chatList: [],
      userQuery: '',
    };
  },
  mounted() {
    document.addEventListener('click', this.handleClickOutside);
    this.updateShowSummary(this.$route.path);
  },
  unmounted() {
    document.removeEventListener('click', this.handleClickOutside);
  },
  watch: {
    $route(to) {
      this.updateShowSummary(to.path);
    },
  },
  methods: {
    updateShowSummary(route) {
      if (
        route.startsWith('/course/graded-assignment') ||
        route.startsWith('/course/ppa1') ||
        route.startsWith('/course/about')
      ) {
        this.showSummary = false;
      } else {
        this.showSummary = true;
      }
    },
    handleWindow() {
      this.isShow = !this.isShow;
    },
    handleExport() {
      const chatsText = this.chatList
        .map((chat) => `You - ${chat.sender} AI - ${chat.receiver}`)
        .join('\n');

      const blob = new Blob([chatsText], { type: 'text/plain' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = 'chat-export.txt';

      document.body.appendChild(link);
      link.click();

      URL.revokeObjectURL(url);
      document.body.removeChild(link);
    },

    fetchLectureSummary(week_number, lecture_id) {
      this.loading = true;
      getLectureSummary(week_number, lecture_id)
        .then((response) => {
          this.chatList.push({
            id: this.chatList.length + 1,
            receiver: response.data.summary,
          });
        })
        .catch((error) => {
          console.error('Error while fetching week content', error);
          this.errorMessage = true;
          this.chatList = [
            {
              id: 3,
              receiver: 'Sorry, someting went wrong, try again...',
            },
          ];
        })
        .finally(() => {
          this.loading = false;
        });
    },
    handleSummarise() {
      let route = this.$route.path;
      let week_number = parseInt(route.charAt(route.length - 3));
      let lecture_id = parseInt(route.charAt(route.length - 1));

      this.fetchLectureSummary(week_number, lecture_id);
      this.isShow = true;
    },

    handleClickOutside(event) {
      if (
        this.isShow &&
        !this.$refs.chatWindow.contains(event.target) &&
        event.target.closest('.btn-chat') === null
      ) {
        this.isShow = false;
      }
    },
    // handleDoubtBot() {
    //   if (this.userQuery.trim()) {
    //     postDoubtBotQuery(this.videoId, this.userQuery)
    //       .then((response) => {
    //         console.log("Response from DoubtBot:", response.data);
    //       })
    //       .catch((error) => {
    //         console.error("Error posting query to DoubtBot:", error);
    //       });
    //     this.userQuery = "";
    //   }
    // },
    handleDoubtBot() {
      if (!this.userQuery.trim()) return;
      this.loading = true;
      let route = this.$route.path;
      let video_id = parseInt(route.charAt(route.length - 1));

      getDoubtBotHelp(video_id, this.userQuery)
        .then((response) => {
          this.chatList.push({
            id: this.chatList.length + 1,
            sender: this.userQuery,
            receiver: response.data.response,
          });
          this.userQuery = '';
        })
        .catch((error) => {
          console.error('Error while fetching doubt bot response', error);
          this.errorMessage = true;
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
};
</script>

<style>
::-webkit-scrollbar {
  width: 5px;
}

::-webkit-scrollbar-track {
  background: #49516c;
  box-shadow: inset 0 0 5px #49516c;
  border-radius: 10px;
}
</style>
<style scoped>
.chat-window {
  position: fixed;
  right: 0%;
  margin-right: -35px;
  z-index: 100;
  top: 0%;
}

.btn-chat,
.btn-summarise {
  background-color: rgb(243, 234, 234);
  border: none;
  padding: 10px;
  color: black;
  cursor: pointer;
  font-size: 16px;
  font-weight: bold;
}

.chat-window .btn-chat {
  border-top-right-radius: 5px;
  border-top-left-radius: 5px;
  transform: rotate(270deg);
  margin-top: 350px;
}

.btn-summarise {
  border-radius: 5px;
  height: 40px;
  margin-top: 70px;
  z-index: 1;
  min-width: max-content;
  margin-left: auto;
}

.chat-window .chat-window-container {
  background-color: white;
  width: 350px;
  height: 95vh;
  box-shadow: 0px 10px 10px rgb(233, 233, 233);
}

.chat-window-container .chat-header {
  height: 30px;
  background-color: rgb(245, 238, 238);
  padding: 5px 25px 15px 5px;
  border-top-left-radius: 5px;
  margin-bottom: 10px;
}

.chat-header div {
  display: flex;
}

.chat-header div p {
  color: rgb(100, 94, 94);
  font-weight: bold;
  font-size: 16px;
}

.chat-header div .export img {
  margin: auto;
  cursor: pointer;
  width: 20px;
  height: 20px;
  margin-left: 150px;
  /* border: 2px solid rgb(77, 75, 75); */
  border-radius: 50%;
  padding: 3px;
  position: fixed;
  right: 40px;
  top: 1.5%;
}

.chat-wrapper {
  height: calc(91% - 25px);
  overflow-y: scroll;
  overflow-x: hidden;
}

.chat-input input {
  padding: 10px;
  height: 25px;
  width: 85%;
  border: none;
  outline: none;
  background-color: rgba(167, 160, 153, 0.08);
  display: flex;
}

.chat-input input::placeholder,
input[type='text'] {
  font-size: 16px;
}

.sender {
  width: 60%;
  margin-left: auto;
  background-color: rgb(139, 135, 133, 0.2);
  padding: 5px 10px;
  word-wrap: break-word;
  margin-bottom: 10px;
  border-top-left-radius: 5px;
  border-bottom-left-radius: 5px;
}

.receiver {
  width: 60%;
  padding: 5px 10px;
  background-color: rgb(218, 197, 189, 0.4);
  word-wrap: break-word;
  margin-bottom: 10px;
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
}

.loading {
  height: 85%;
  margin: auto;
}

.loading p {
  text-align: center;
  font-size: 24px;
}

.close-btn img {
  margin: auto;
  cursor: pointer;
  width: 27px;
  height: 27px;
  margin-left: 150px;
  position: fixed;
  right: 10px;
  top: 1.4%;
}
</style>
