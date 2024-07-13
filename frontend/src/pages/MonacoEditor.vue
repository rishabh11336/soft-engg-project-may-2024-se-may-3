<template>
  <div ref="container" class="editor-container"></div>
</template>

<script>
import * as monaco from 'monaco-editor';

export default {
  name: 'MonacoEditor',
  props: {
    value: {
      type: String,
      required: true,
    },
    language: {
      type: String,
      default: 'python',
    },
    theme: {
      type: String,
      default: 'vs', // Change to 'vs' for light theme
    },
  },
  mounted() {
    this.editor = monaco.editor.create(this.$refs.container, {
      value: this.value,
      language: this.language,
      theme: this.theme,
      automaticLayout: true,
      lineNumbers: 'on',
    });

    this.editor.onDidChangeModelContent(() => {
      this.$emit('input', this.editor.getValue());
    });
  },
  beforeUnmount() {
    if (this.editor) {
      this.editor.dispose();
    }
  },
  watch: {
    value(newVal) {
      if (this.editor && newVal !== this.editor.getValue()) {
        this.editor.setValue(newVal);
      }
    },
    language(newVal) {
      if (this.editor) {
        monaco.editor.setModelLanguage(this.editor.getModel(), newVal);
      }
    },
    theme(newVal) {
      if (this.editor) {
        monaco.editor.setTheme(newVal);
      }
    },
  },
};
</script>

<style>
.editor-container {
  height: 400px !important; /* Adjust the height as needed */
  border: 1px solid #ccc;
  border-radius: 4px;
  overflow: hidden;
}
</style>
