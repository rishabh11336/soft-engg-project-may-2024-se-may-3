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
          <p>Loading Summary....</p>
        </div>
        <div class="chat-input">
          <input v-model="userQuery" type="text" placeholder="Type your query here ....."
            @keyup.enter="handleDoubtBot()" />
          <button @click="handleDoubtBot()" class="ask-btn">Ask</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import downloadIcon from '../assets/download.svg';
import closeIcon from '../assets/close.svg';
import { getLectureSummary, getDoubtBotHelp } from '@/services/apiServices';

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

    let route = this.$route.path;
    let week_number = parseInt(route.charAt(route.length - 1));
    if (
      route === `/course/graded-assignment/${week_number}` ||
      route === `/course/ppa1/${week_number}`
    ) {
      this.showSummary = false;
    } else {
      this.showSummary = true;
    }
  },
  unmounted() {
    document.removeEventListener('click', this.handleClickOutside);
  },
  methods: {
    handleWindow() {
      this.isShow = !this.isShow;
    },
    //Chat export function -- txt format
    handleExport() {
      // Prepare data for export (chat messages)
      const chatsText = this.chatList
        .map((chat) => `You - ${chat.sender} AI - ${chat.receiver}`)
        .join('\n');
      // Create a Blob containing the text
      const blob = new Blob([chatsText], { type: 'text/plain' });
      // Create a temporary URL to the Blob
      const url = URL.createObjectURL(blob);
      // Create a link element
      const link = document.createElement('a');
      link.href = url;
      link.download = 'chat-export.txt'; // Filename
      // Append the link to the body and click it to trigger download
      document.body.appendChild(link);
      link.click();
      // Clean up: remove the temporary URL
      URL.revokeObjectURL(url);
      // Remove the link from the DOM
      document.body.removeChild(link);
    },
    // fetch lecture summary function
    fetchLectureSummary(week_number, lecture_id) {
      this.loading = true;
      getLectureSummary(week_number, lecture_id)
        .then((response) => {
          this.chatList = [
            {
              id: 1,
              receiver: response.data.summary,
            },
          ];
        })
        .catch((error) => {
          console.error('Error while fetching week content', error);
          this.errorMessage = true;
        })
        .finally(() => {
          this.loading = false;
        });
    },
    // summary handler
    handleSummarise() {
      let route = this.$route.path;
      let week_number = parseInt(route.charAt(route.length - 3));
      let lecture_id = parseInt(route.charAt(route.length - 1));
      this.fetchLectureSummary(week_number, lecture_id);
      this.isShow = true;
    },
    handleClickOutside(event) {
      // Check if the clicked element is outside the chat window
      if (
        this.isShow &&
        !this.$refs.chatWindow.contains(event.target) &&
        event.target.closest('.btn-chat') === null
      ) {
        this.isShow = false;
      }
    },

    // DOUBTBOT
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
  right: 0;
  top: 0;
  z-index: 100;
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

.chat-input {
  display: flex;
  gap: 2px;
  background-color: #f5f5f5;
  box-sizing: border-box;
  padding: 10px;
}

.chat-input input {
  padding: 10px;
  height: 45px;
  width: 100%;
  border: none;
  outline: none;
  background-color: rgba(167, 160, 153, 0.08);
  flex-grow: 1;
  font-size: 16px;
  box-sizing: border-box;
}

.chat-input input::placeholder {
  font-size: 16px;
}

.chat-input .ask-btn {
  padding: 10px;
  background: rgb(243, 234, 234);
  border: none;
  cursor: pointer;
  font-size: 16px;
  font-weight: bold;
  height: 45px;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: center;
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
  display: flex;
  align-items: center;
  justify-content: center;
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
  position: fixed;
  right: 10px;
  top: 1.4%;
}
</style>
