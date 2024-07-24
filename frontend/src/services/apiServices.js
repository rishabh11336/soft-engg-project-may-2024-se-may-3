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

export const runProgAssignCode = ({ code, input }) => {
  return axios.post(`${API_BASE_URL}/run-pa-code`, { code, input });
};

