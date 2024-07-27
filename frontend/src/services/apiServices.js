import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000/api';

export const getWeekContent = (week_number) => {
  return axios.get(`${API_BASE_URL}/coursecontent/${week_number}`);
};

export const getAssignments = (week_number) => {
  return axios.get(`${API_BASE_URL}/questions/${week_number}`);
};

export function submitAnswers(submissionData) {
  return axios.post(`${API_BASE_URL}/gasubmit`, submissionData);
}

export const getProgrammingAssignments = (week_number) => {
  return axios.get(`${API_BASE_URL}/programmingassignments/${week_number}`);
};

export function submitProgrammingAssignments(submissionData) {
  return axios.post(`${API_BASE_URL}/pasubmit`, submissionData);
}

export const runPythonCode = (code) => {
  return axios.post(`${API_BASE_URL}/run-python`, { code });
};

export const getLectureSummary = (week_number, lecture_id) => {
  return axios.get(
    `${API_BASE_URL}/genai/summary/${week_number}/${lecture_id}`
  );
};

export const getTheoryQuestionExplaination = (question_number) => {
  return axios.get(`${API_BASE_URL}/genai/explaintheory/${question_number}`);
};

export const getProgrammingQuestionExplaination = (question_id) => {
  return axios.get(`${API_BASE_URL}/genai/explainprogramming/${question_id}`);
};

export const getDoubtBotHelp = (video_id) => {
  return axios.get(`${API_BASE_URL}/genai/doubtbot/${video_id}`);
};