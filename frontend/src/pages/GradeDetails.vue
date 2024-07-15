<template>
    <div class="content">
        <div class="week">
            <div class="week-header" @click="toggleDetails('week1-details')">
                <h4>Week 1</h4>
                <span>▼</span>
            </div>
            <div class="week-details" id="week1-details" :style="{ display: week1Visible ? 'block' : 'none' }">
                <table>
                    <thead>
                        <tr>
                            <th class="assignment-col">Assignment</th>
                            <th class="score-col">Your Score</th>
                            <th class="score-col">Peer Average</th>
                            <th>Median Score</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="assignment-col">
                                <p class="assignment-heading">Practice Assignment 1 - Not Graded</p>
                                <p class="assessment">Assessment (Due: 31 Jan 2025)</p>
                                <p class="pending">Due Date Pending</p>
                            </td>
                            <td class="score-col">
                                <p>-</p>
                            </td>
                            <td class="score-col">
                                <p>-</p>
                            </td>
                            <td>
                                <p>-</p>
                            </td>
                        </tr>
                        <tr class="graded-row">
                            <td class="assignment-col">
                                <p class="assignment-heading">Graded Assignment 1</p>
                                <p class="assessment">Assessment (Due: 16 June 2024)</p>
                                <p class="submitted">Submitted</p>
                            </td>
                            <td class="score-col">
                                <p>80</p>
                            </td>
                            <td class="score-col">
                                <p>87</p>
                            </td>
                            <td>
                                <p>90%</p>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'GradeDetails',
    data() {
        return {
            week1Visible: false,
        };
    },
    methods: {
        toggleDetails() {
            this.week1Visible = !this.week1Visible;
        },
    },
};
</script>

<style scoped>
.content {
    width: 50vw;
    margin: 20px auto;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    overflow: hidden;
}

.week {
    border-bottom: 1px solid #ddd;
}

.week-header {
    padding: 15px;
    background-color: #f1f1f1;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.week-header h4 {
    margin: 0;
}

.week-details {
    padding: 15px;
}


.assignment-header {
    display: flex;
    justify-content: space-between;
    font-weight: bold;
    margin-bottom: 5px;
}

.assignment-status {
    margin-bottom: 5px;
    color: #777;
}

.assignment-scores span {
    display: block;
    margin-bottom: 5px;
}

.score-details {
    display: flex;
    justify-content: space-between;
}

.assignment {
    margin-bottom: 20px;
    width: 25vw;
    padding-left: 5px;
    border-left: 1px #777;
}

.score .peer {
    border-left: 1px #777;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th {
    font-size: small;
    font-weight: 550;
    color: #424242;
}

.graded-row {
    background: #f5f5f5;
}

th,
td {
    padding: 8px;
    text-align: left;
}

th.assignment-col,
td.assignment-col {
    width: 25vw;
    border-right: 1px solid #ddd;
}

th.score-col,
td.score-col {
    border-right: 1px solid #ddd;
}

.assignment-heading {
    font-size: small;
    font-weight: 600;
    color: #424242;
}

.assessment {
    font-size: small;
    font-weight: lighter;
}

.pending {
    color: #efae35;
    font-size: smaller;
    font-weight: lighter;
}

.submitted {
    color: rgb(29, 176, 29);
    font-size: smaller;
    font-weight: lighter;
}


</style>