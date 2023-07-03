import axios from "axios"
// const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').getAttribute("value")0
const csrftoken = document.getElementsByName("csrfmiddlewaretoken")[0].value
console.log("csrftoken : ", csrftoken)
let http = axios.create({
  baseURL: "https://creativegame.pythonanywhere.com/api",
  timeout: 10000,
  headers: {
    "X-CSRFToken": csrftoken,
    Accept: "application/json",
    withCredentials: true
  }
})
export default http
