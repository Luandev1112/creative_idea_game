import api from "@/services/api"
import { ref } from "vue"
import router from "../router"

// it would be better to store refresh token and then use it to get a new access token
const LOCALSTORARGE_TOKEN_KEY = "myapp_access_token"
let access_token = localStorage.getItem(LOCALSTORARGE_TOKEN_KEY)
let user = ref()

api.interceptors.request.use((config) => {
  if (access_token) {
    config.headers["Authorization"] = `Bearer ${access_token}`
  }
  return config
})

export default {
  user,
  login(payload) {
    if (!payload.username || !payload.password) {
      return Promise.reject("Username and password are required.")
    }

    return api.post(`dj-rest-auth/login/`, payload).then((response) => {
      access_token = response.data.access_token
      localStorage.setItem(LOCALSTORARGE_TOKEN_KEY, access_token)
      user.value = response.data.user
      return response.data.user
    })
  },
  logout() {
    return api.post(`dj-rest-auth/logout/`).then((response) => {
      access_token = undefined
      localStorage.removeItem(LOCALSTORARGE_TOKEN_KEY)
      user.value = undefined
      return response.data
    })
  },
  register(payload) {
    if (!payload.username || !payload.password1 || !payload.password2) {
      return Promise.reject("Username and password1 and password2 are required.")
    }

    return api.post(`dj-rest-auth/registration/`, payload).then((response) => {
      access_token = response.data.access_token
      user.value = response.data.user
      return response.data.user
    })
  },
  // allows to relogin with saved token
  getUser() {
    return api.get(`dj-rest-auth/user/`).then((response) => {
      user.value = response.data
    })
  },

  checkUserKey(payload) {
    if (!payload.userKey || !payload.prolificId ) {
      return Promise.reject("User Key is requred.")
    }
    let formdata = new FormData()
    formdata.append("user_key", payload.userKey)
    formdata.append("prolific_id", payload.prolificId)
    return api.post(`checkUserKey/`, formdata).then((response) => {
      if (response.data == 1) {
        router.push({ name: "guide-1" })
      } else {
        console.log("Invalid User Key")
      }
    })
  },

  checkUserSession() {
    return api.get(`checkUserSession/`).then((response) => {
      if (response.data.status == 0) {
        router.push({ name: "login" })
      }
    })
  }
}
