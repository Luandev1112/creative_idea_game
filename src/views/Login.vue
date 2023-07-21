<!-- eslint-disable prettier/prettier -->
<template>
  <div class="account-page">
    <div class="main-wrapper">
      <!-- Page Content -->
      <div class="bg-pattern-style">
        <div class="content">
          <!-- Login Tab Content -->
          <div class="account-content">
            <div class="account-box">
              <div class="login-right">
                <div class="text-center mt-4 mb-4">
                  <img src="../assets/images/logo.svg" class="img-fluid w-25" alt="Logo" />
                </div>
                <div class="login-header text-center">
                  <h3>Welcome to <span>COG</span></h3>
                  <p class="text-muted">Please enter your Prolific ID and Study Code</p>
                </div>
                <form>
                  <div class="form-group">
                    <label class="form-control-label">Prolific ID</label>
                    <input type="text" class="form-control" v-model="prolificId" />
                  </div>

                  <div class="form-group">
                    <label class="form-control-label">Study Code</label>
                    <input type="text" class="form-control" v-model="userId" />
                  </div>
                  <button class="btn btn-primary login-btn" type="button" @click="checkUserId">
                    Confirm
                  </button>
                </form>
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
  name: "Login",
  props: {
    msg: String
  },
  data() {
    return {
      userId: "",
      prolificId: ""
    }
  },
  mounted() {
    console.log("mounted")
  },
  computed: {},
  methods: {
    checkUserId() {
      console.log(this.userId)
      console.log(this.prolificId)
      this.loginError = ""
      authService
        .register({
          userKey: this.userId,
          prolificId: this.prolificId
        })
        .catch((err) => {
          this.loginError = err.response.data
        })
    }
  }
}
</script>
