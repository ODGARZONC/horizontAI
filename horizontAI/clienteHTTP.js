import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';


const API = axios.create({ baseURL: 'http://127.0.0.1:8000/' });

export default API;

