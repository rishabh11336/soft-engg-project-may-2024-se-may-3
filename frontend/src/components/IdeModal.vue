<template>
    <div v-if="show" class="modal-overlay" @click.self="close">
      <div
        class="modal-content"
        ref="modalContent"
        @mousedown="onMouseDown"
        :style="{ top: modalTop + 'px', left: modalLeft + 'px', width: modalWidth + 'px', height: modalHeight + 'px' }"
      >
        <!-- <button class="close-button" @click="close">X</button> -->
        <div class="editor-container">
          <slot></slot>
        </div>
        <div class="resize-handle" @mousedown="onResizeMouseDown">
          <svg height="20" width="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M21 15L15 21M21 8L8 21" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
          </svg>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { nextTick } from 'vue';
  
  export default {
    props: {
      show: {
        type: Boolean,
        required: true,
      },
    },
    data() {
      return {
        isDragging: false,
        isResizing: false,
        modalTop: 0,
        modalLeft: 0,
        modalWidth: 600, // Initial width
        modalHeight: 400, // Initial height
        initialMouseX: 0,
        initialMouseY: 0,
        initialWidth: 0,
        initialHeight: 0,
      };
    },
    methods: {
      close() {
        this.$emit('close');
      },
      onMouseDown(event) {
        this.isDragging = true;
        this.initialMouseX = event.clientX;
        this.initialMouseY = event.clientY;
  
        document.addEventListener('mousemove', this.onMouseMove);
        document.addEventListener('mouseup', this.onMouseUp);
      },
      onMouseMove(event) {
        if (this.isDragging) {
          const deltaX = event.clientX - this.initialMouseX;
          const deltaY = event.clientY - this.initialMouseY;
  
          this.modalTop += deltaY;
          this.modalLeft += deltaX;
  
          this.initialMouseX = event.clientX;
          this.initialMouseY = event.clientY;
        } else if (this.isResizing) {
          const deltaX = event.clientX - this.initialMouseX;
          const deltaY = event.clientY - this.initialMouseY;
  
          this.modalWidth = this.initialWidth + deltaX;
          this.modalHeight = this.initialHeight + deltaY;
        }
      },
      onMouseUp() {
        this.isDragging = false;
        this.isResizing = false;
        document.removeEventListener('mousemove', this.onMouseMove);
        document.removeEventListener('mouseup', this.onMouseUp);
      },
      onResizeMouseDown(event) {
        event.stopPropagation();
        this.isResizing = true;
        this.initialMouseX = event.clientX;
        this.initialMouseY = event.clientY;
        this.initialWidth = this.modalWidth;
        this.initialHeight = this.modalHeight;
  
        document.addEventListener('mousemove', this.onMouseMove);
        document.addEventListener('mouseup', this.onMouseUp);
      },
    },
    watch: {
      show(val) {
        if (val) {
          nextTick(() => {
            const modal = this.$refs.modalContent;
            if (modal) {
              this.modalTop = window.innerHeight / 2 - modal.clientHeight / 2;
              this.modalLeft = window.innerWidth / 2 - modal.clientWidth / 2;
              this.modalWidth = modal.clientWidth;
              this.modalHeight = modal.clientHeight;
            }
          });
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.6);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal-content {
    background: white;
    padding: 20px;
    border-radius: 5px;
    position: absolute;
    cursor: move;
    display: flex;
    flex-direction: column;
  }
  
  .close-button {
    position: absolute;
    top: 1px;
    right: 1px;
    background: none;
    border: none;
    font-size: 18px;
    cursor: pointer;
    color: black;
  }
  
  .editor-container {
    flex: 1;
    overflow: hidden;
  }
  
  /* .resize-handle {
    position: absolute;
    bottom: 0;
    right: 0;
    width: 20px;
    height: 20px;
    background: gray;
    cursor: se-resize;
  } */
  
  .resize-handle {
    position: absolute;
    bottom: 0;
    right: 0;
    width: 20px;
    height: 20px;
    background-color: white;
    cursor: se-resize;
    background-repeat: no-repeat;
    background-position: center;
    background-size: 14px;
  }
  
  </style>