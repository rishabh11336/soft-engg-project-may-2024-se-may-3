<template>
    <div class="editor-container">
        <div class="editor">
            <codemirror v-model="code" placeholder="Write your Python code here..."
                :style="{ height: '100%', width: '100%' }" :autofocus="true" :indent-with-tab="true" :tab-size="2"
                :extensions="extensions" @ready="handleReady" @change="log('change', $event)" />
            <button class="run-button" @click="runCode">Run Code</button>
        </div>
        <div class="console">
            <h2 class="console-header">Console</h2>
            <hr>
            <pre>>>> {{ output }}</pre>
        </div>
    </div>
</template>

<script>
import { defineComponent, ref, shallowRef } from 'vue';
import { Codemirror } from 'vue-codemirror';
import { python } from '@codemirror/lang-python';

export default defineComponent({
    name: 'CodeEditor',
    components: {
        Codemirror,
    },
    setup() {
        const code = ref('');
        const output = ref('');
        const extensions = [python()];
        const view = shallowRef(null);

        const handleReady = (payload) => {
            view.value = payload.view;
        };

        const runCode = async () => {
            try {
                const response = await fetch('http://localhost:5000/api/run-python', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ code: code.value }),
                });
                const result = await response.json();
                output.value = result.output;
            } catch (error) {
                output.value = 'Error running code';
            }
        };

        const log = (event, payload) => {
            console.log(event, payload);
        };

        return {
            code,
            output,
            extensions,
            handleReady,
            runCode,
            log,
        };
    },
});
</script>

<style scoped>
.editor-container {
    display: flex;
    height: 80vh;
    background-color: #f5f5f5;
    text-align: start;
}

.editor {
    flex: 1;
    display: flex;
    flex-direction: column;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 4px;
}

.console-header {
    text-align: center;
    margin-top: 2px;
    margin-bottom: 2px;
}

.console {
    flex: 1;
    border-left: 1px solid #ddd;
    padding: 5px 16px 16px 16px;
    background-color: #eee;
    overflow: auto;
    font-family: monospace;
    text-align: start;
}

.run-button {
    margin-top: 8px;
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    background-color: #4CAF50;
    color: white;
    cursor: pointer;
}

.codemirror {
    text-align: left;
}
</style>