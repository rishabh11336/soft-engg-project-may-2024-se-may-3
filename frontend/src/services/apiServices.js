import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000/api';

export const getWeekContent = (week_number) => {
  return axios.get(`${API_BASE_URL}/coursecontent/${week_number}`);
};

export const getAssignments = (week_number) => {
  return axios.get(`${API_BASE_URL}/questions/${week_number}`);
};
