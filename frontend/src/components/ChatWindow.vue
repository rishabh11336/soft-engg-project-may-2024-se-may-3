<template>
  <div class="chat-window">
    <button @click="handleWindow()" v-if="!isShow">Open Chat</button>
    <div class="chat-window-container" v-if="isShow">
      <div class="close-btn" @click="handleWindow()">X</div>

      <div class="chat-header">
        <p>Chat Window</p>
      </div>
      <div class="chat-wrapper">
        <div class="sender">
          <p>Hello here is my first query, explain it detail with example</p>
        </div>
        <div class="receiver">
          <p>Okay, so here is detailed explaination of your query ...</p>
        </div>
        <div class="sender">
          <p>Hello here is my first query, explain it detail with example</p>
        </div>
        <div class="receiver">
          <p>Okay, so here is detailed explaination of your query ...</p>
        </div>
        <div class="sender">
          <p>Hello here is my first query, explain it detail with example</p>
        </div>
        <div class="receiver">
          <p>Okay, so here is detailed explaination of your query ...</p>
        </div>
        <div class="sender">
          <p>Hello here is my first query, explain it detail with example</p>
        </div>
        <div class="receiver">
          <p>Okay, so here is detailed explaination of your query ...</p>
        </div>
      </div>
      <div class="chat-input">
        <input
          type="text"
          name=""
          id=""
          placeholder="Type your query here ....."
        />
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'ChatWindow',
  data() {
    return {
      isShow: false,
    };
  },
  methods: {
    handleWindow() {
      this.isShow = !this.isShow;
    },
  },
};
</script>
<style scoped>
.chat-window {
  position: fixed;
  right: 0%;
  margin-right: -35px;
  z-index: 100;
  top: 10%;
}

.chat-window button {
  border-top-right-radius: 5px;
  border-top-left-radius: 5px;
  background-color: rgb(243, 234, 234);
  transform: rotate(270deg);
  color: black;
  cursor: pointer;
}

.chat-window .chat-window-container {
  background-color: white;
  width: 350px;
  height: 500px;
  box-shadow: 0px 10px 10px rgb(233, 233, 233);
}

.chat-window-container .chat-header {
  height: 30px;
  background-color: rgb(245, 238, 238);
  padding: 5px 25px 15px 5px;
  border-top-left-radius: 5px;
  margin-bottom: 10px;
}

.chat-header p {
  color: rgb(100, 94, 94);
  font-weight: bold;
  font-size: 16px;
}

.chat-wrapper {
  height: 79%;
  overflow-y: scroll;
  overflow-x: hidden;
}

.chat-input input {
  padding: 10px;
  height: 25px;
  width: 85%;
  border: none;
  background-color: rgba(167, 160, 153, 0.08);
}

.chat-input input::placeholder,
input[type='text'] {
  font-size: 16px;
}

.sender {
  width: 60%;
  margin-left: 150px;
  background-color: rgb(139, 135, 133, 0.2);
  padding: 1px;
  word-wrap: break-word;
  margin-bottom: 10px;
  border-top-left-radius: 5px;
  border-bottom-left-radius: 5px;
}

.receiver {
  width: 60%;
  padding: 1px;
  background-color: rgb(218, 197, 189, 0.4);
  word-wrap: break-word;
  margin-bottom: 10px;
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
}

.close-btn {
  position: fixed;
  right: 0;
  top: 12%;
  background-color: white;
  color: rgb(100, 94, 94);
  border-radius: 50%;
  width: 25px;
  height: 20px;
  text-align: center;
  padding-top: 5px;
  font-weight: bold;
  font-size: 14px;
}
</style>
