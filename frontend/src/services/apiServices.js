import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000/api';

// API for week content
export const getWeekContent = (week_number) => {
  return axios.get(`${API_BASE_URL}/coursecontent/${week_number}`);
};

// API for lecture content
export const getLectureContent = (lecture_id) => {
  return axios.get(`${API_BASE_URL}/videocontent/${lecture_id}`);
};

// API for assignments
export const getAssignments = (week_number) => {
  return axios.get(`${API_BASE_URL}/questions/${week_number}`);
};

// API for submit theory assignment
export function submitAnswers(submissionData) {
  return axios.post(`${API_BASE_URL}/gasubmit`, submissionData);
}

// API for Programming assignment
export const getProgrammingAssignments = (week_number) => {
  return axios.get(`${API_BASE_URL}/programmingassignments/${week_number}`);
};

// API for submit Programming assignment
export function submitProgrammingAssignments(submissionData) {
  return axios.post(`${API_BASE_URL}/pasubmit`, submissionData);
}

// API to run code
export const runPythonCode = (code) => {
  return axios.post(`${API_BASE_URL}/run-python`, { code });
};

// API to run programming code
export const runProgAssignCode = ({ code, input }) => {
  return axios.post(`${API_BASE_URL}/run-pa-code`, { code, input });
};

// API to get lecture summary
export const getLectureSummary = (week_number, lecture_id) => {
  return axios.get(
    `${API_BASE_URL}/genai/summary/${week_number}/${lecture_id}`
  );
};

// API for doubt bot
export const getDoubtBotHelp = (video_id, userQuery) => {
  return axios.get(`${API_BASE_URL}/genai/doubtbot/${video_id}/${userQuery}`);
};

// API for Assignment question explanation
export const getTheoryQuestionExplaination = (question_number) => {
  return axios.get(`${API_BASE_URL}/genai/explaintheory/${question_number}`);
};

// API for Programming Assignment question explanation
export const getProgrammingQuestionExplaination = (question_id) => {
  return axios.get(`${API_BASE_URL}/genai/explainprogramming/${question_id}`);
};

// API for Assignment marks
export const getMarksForWeek = (week_number) => {
  return axios.get(`${API_BASE_URL}/marks/${week_number}`);
};

// API for Programming Assignment marks
export const getProgrammingAssignmentMarks = (week_number, assignment_id) => {
  return axios.get(
    `${API_BASE_URL}/programmingassignments/${week_number}/marks/${assignment_id}`
  );
};

// GET REQUEST => GET QUIZ QUESTIONS
export const getQuizQuestions = () => {
  return axios.get(`${API_BASE_URL}/quizquestion`);
};