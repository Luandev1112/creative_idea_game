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
                  <h1 class="mb-4"><span>Practice</span></h1>
                  <ul class="mb-4">
                    <li class="mb-4">
                      We'll begin with three practice rounds prior to the main game.
                    </li>
                    <li class="mb-4">
                      You'll be shown an object and must type three creative uses for it, hitting
                      enter after each use.
                    </li>
                  </ul>
                </div>
                <div class="text-center">
                  <router-link to="/">
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
  name: "Guide2",
  props: {
    msg: String
  },
  beforeCreate() {
    authService.checkUserSession().catch((err) => {
      this.loginError = err.response.data
    })
  },
  data() {
    return {
      userId: ""
    }
  },
  mounted() {
    console.log("mounted")
  },
  computed: {},
  methods: {}
}
</script>
