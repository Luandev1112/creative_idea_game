<template>
  <div class="account-page">
    <div class="main-wrapper">
      <!-- Page Content -->
      <div class="bg-pattern-style">
        <div class="content">
          <!-- Login Tab Content -->
          <div class="account-content">
            <div class="text-center mt-4 mb-4">
              <img src="../assets/images/logo.svg" class="img-fluid w-25" alt="Logo" />
            </div>
            <div class="guide-box mb-5 pt-5 pb-5">
              <div class="login-right">
                <div class="guide-header text-center">
                  <h1 class="mb-4"><span>Welcome!</span></h1>
                  <ul class="mb-4">
                    <li class="mb-4">Welcome to COG, the Creative Objects Game!</li>
                    <li>
                      The goal is to think of creative uses for everyday objects, like a brick.
                      You’ll see an object and type creative uses for it.
                    </li>
                  </ul>
                </div>
                <div class="text-center">
                  <router-link to="/guide-2">
                    <button class="btn btn-primary guide-btn w-50" type="button">Next</button>
                  </router-link>
                </div>
              </div>
            </div>
          </div>
          <!-- /Login Tab Content -->
        </div>
      </div>
      <!-- /Page Content -->
    </div>
  </div>
</template>

<script>
import authService from "../services/authService"
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Guide1",
  props: {
    msg: String
  },
  data() {
    return {
      userId: ""
    }
  },
  beforeCreate() {
    authService.checkUserSession().catch((err) => {
      this.loginError = err.response.data
    })
  },
  mounted() {
    console.log("mounted")
  },
  computed: {},
  methods: {}
}
</script>
