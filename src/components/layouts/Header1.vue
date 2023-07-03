<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<template>
  <!-- Header -->
  <header class="header">
    <div class="header-fixed">
      <nav class="navbar navbar-expand-lg header-nav">
        <div class="navbar-header">
          <a id="mobile_btn" href="javascript:void(0);">
            <span class="bar-icon">
              <span></span>
              <span></span>
              <span></span>
            </span>
          </a>
          <router-link to="/" class="navbar-brand logo">
            <img src="../../assets/images/logo.svg" class="img-fluid" alt="Logo" />
          </router-link>
        </div>
        <div class="main-menu-wrapper">
          <div class="menu-header">
            <router-link to="/" class="menu-logo">
              <img src="../../assets/images/logo.svg" class="img-fluid" alt="Logo" />
            </router-link>
            <a id="menu_close" class="menu-close" href="javascript:void(0);">
              <i class="fas fa-times"></i>
            </a>
          </div>
          <ul class="main-nav">
            <li v-bind:class="{ active: currentPath == 'index' }">
              <router-link to="/">Home</router-link>
            </li>
            <li class="has-submenu" v-bind:class="{ active: mentorMenu }">
              <a href="">Mentor <i class="fas fa-chevron-down"></i></a>
              <ul class="submenu">
                <li v-bind:class="{ active: currentPath == 'mentor-dashboard' }">
                  <router-link to="/mentor/index">Mentor Dashboard</router-link>
                </li>
                <li v-bind:class="{ active: currentPath === 'mentor-bookings' }">
                  <router-link to="/mentor/my-bookings">Bookings</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'mentor-schedule-timings' }">
                  <router-link to="/mentor/schedule-timings">Schedule Timing</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'mentor-mentee-list' }">
                  <router-link to="/mentor/mentee-list">Mentee List</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'mentor-mentee-profile' }">
                  <router-link to="/mentor/mentee-profile">Mentee Profile</router-link>
                </li>
                <li
                  class="has-submenu"
                  v-bind:class="{
                    active:
                      currentPath == 'mentor-blog' ||
                      currentPath == 'add-blog' ||
                      currentPath == 'edit-blog'
                  }"
                >
                  <router-link to="/mentor/blog">Blog</router-link>
                  <ul class="submenu">
                    <li v-bind:class="{ active: currentPath == 'mentor-blog' }">
                      <router-link to="/mentor/blog">Blog</router-link>
                    </li>
                    <li><router-link to="/mentor/blog-details">Blog View</router-link></li>
                    <li v-bind:class="{ active: currentPath == 'add-blog' }">
                      <router-link to="/mentor/add-blog">Add Blog</router-link>
                    </li>
                    <li v-bind:class="{ active: currentPath == 'edit-blog' }">
                      <router-link to="/mentor/edit-blog">Edit Blog</router-link>
                    </li>
                  </ul>
                </li>
                <li v-bind:class="{ active: currentPath == 'mentor-chat' }">
                  <router-link to="/mentor/chat">Chat</router-link>
                </li>
                <li
                  v-bind:class="{
                    active: currentPath == 'mentor-invoices' || currentPath == 'mentor-invoice-view'
                  }"
                >
                  <router-link to="/mentor/invoices">Invoices</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'mentor-profile-settings' }">
                  <router-link to="/mentor/profile-settings">Profile Settings</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'mentor-reviews' }">
                  <router-link to="/mentor/reviews">Reviews</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'mentor-register' }">
                  <router-link to="/mentor/register">Mentor Register</router-link>
                </li>
              </ul>
            </li>
            <li class="has-submenu" v-bind:class="{ active: menteeMenu }">
              <a href="">Mentee <i class="fas fa-chevron-down"></i></a>
              <ul class="submenu">
                <li
                  class="has-submenu"
                  v-bind:class="{ active: currentPath == 'map-grid' || currentPath == 'map-list' }"
                >
                  <a href="#">Mentors</a>
                  <ul class="submenu">
                    <li v-bind:class="{ active: currentPath == 'map-grid' }">
                      <router-link to="/mentee/map-grid">Map Grid</router-link>
                    </li>
                    <li v-bind:class="{ active: currentPath == 'map-list' }">
                      <router-link to="/mentee/map-list">Map List</router-link>
                    </li>
                  </ul>
                </li>
                <li v-bind:class="{ active: currentPath == 'mentor-search-results' }">
                  <router-link to="/mentee/mentor-search">Search Mentor</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'mentee-mentor-profile' }">
                  <router-link to="/mentee/mentor-profile">Mentor Profile</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'mentee-bookings' }">
                  <router-link to="/mentee/bookings">Bookings</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'mentee-checkout' }">
                  <router-link to="/mentee/checkout">Checkout</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'booking-success' }">
                  <router-link to="/mentee/booking-success">Booking Success</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'mentee-dashboard' }">
                  <router-link to="/mentee/index">Mentee Dashboard</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'mentee-favourites' }">
                  <router-link to="/mentee/favourites">Favourites</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'mentee-chat' }">
                  <router-link to="/mentee/chat">Chat</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'mentee-profile-settings' }">
                  <router-link to="/mentee/profile-settings">Profile Settings</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'change-password' }">
                  <router-link to="/mentee/change-password">Change Password</router-link>
                </li>
              </ul>
            </li>
            <li class="has-submenu" v-bind:class="{ active: pagesMenu }">
              <a href="">Pages <i class="fas fa-chevron-down"></i></a>
              <ul class="submenu">
                <li v-bind:class="{ active: currentPath == 'voice-call' }">
                  <router-link to="/pages/voice-call">Voice Call</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'video-call' }">
                  <router-link to="/pages/video-call">Video Call</router-link>
                </li>
                <li><router-link to="/mentee/mentor-search">Search Mentors</router-link></li>
                <li v-bind:class="{ active: currentPath == 'page-components' }">
                  <router-link to="/pages/components">Components</router-link>
                </li>
                <li class="has-submenu">
                  <router-link to="/mentor/invoices">Invoices</router-link>
                  <ul class="submenu">
                    <li><router-link to="/mentor/invoices">Invoices</router-link></li>
                    <li><router-link to="/mentor/invoice-view">Invoice View</router-link></li>
                  </ul>
                </li>
                <li v-bind:class="{ active: currentPath == 'blank-page' }">
                  <router-link to="/pages/blank-page">Starter Page</router-link>
                </li>
                <li><router-link to="/pages/login">Login</router-link></li>
                <li><router-link to="/pages/register">Register</router-link></li>
                <li><router-link to="/pages/forgot-password">Forgot Password</router-link></li>
              </ul>
            </li>
            <li class="has-submenu" v-bind:class="{ active: blogMenu }">
              <a href="">Blog <i class="fas fa-chevron-down"></i></a>
              <ul class="submenu">
                <li v-bind:class="{ active: currentPath == 'blog-list' }">
                  <router-link to="/blog/blog-list">Blog List</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'blog-grid' }">
                  <router-link to="/blog/blog-grid">Blog Grid</router-link>
                </li>
                <li v-bind:class="{ active: currentPath == 'mentor-blog-details' }">
                  <router-link to="/mentor/blog-details">Blog Details</router-link>
                </li>
              </ul>
            </li>
            <li>
              <router-link to="/admin/index" target="_blank">Admin</router-link>
            </li>
            <li class="login-link">
              <router-link to="/pages/login">Login / Signup</router-link>
            </li>
          </ul>
        </div>
        <ul class="nav header-navbar-rht">
          <!-- User Menu -->
          <li class="nav-item dropdown has-arrow logged-item">
            <a href="#" class="dropdown-toggle nav-link" data-toggle="dropdown">
              <span class="user-img">
                <img
                  class="rounded-circle"
                  src="../../assets/images/user/user.jpg"
                  width="31"
                  alt="Darren Elder"
                />
              </span>
            </a>
            <div class="dropdown-menu dropdown-menu-right">
              <div class="user-header">
                <div class="avatar avatar-sm">
                  <img
                    src="../../assets/images/user/user.jpg"
                    alt="User Image"
                    class="avatar-img rounded-circle"
                  />
                </div>
                <div class="user-text">
                  <h6>Jonathan Doe</h6>
                  <p class="text-muted mb-0">Mentor</p>
                </div>
              </div>
              <router-link class="dropdown-item" to="/mentor/index">Dashboard</router-link>
              <router-link class="dropdown-item" to="/mentor/profile-settings"
                >Profile Settings</router-link
              >
              <router-link class="dropdown-item" to="/pages/login">Logout</router-link>
            </div>
          </li>
          <!-- /User Menu -->
        </ul>
      </nav>
    </div>
  </header>
  <!-- /Header -->
</template>
<script>
import Util from "../../../assets/utils/utils"
import { onMounted, computed } from "vue"
import { useRoute } from "vue-router"

export default {
  setup() {
    const currentPath = computed(() => {
      return useRoute().name
    })

    const mentorMenu = computed(() => {
      return Util.mentorMenu(useRoute().name)
    })

    const menteeMenu = computed(() => {
      return Util.menteeMenu(useRoute().name)
    })

    const pagesMenu = computed(() => {
      return Util.pagesMenu(useRoute().name)
    })

    const blogMenu = computed(() => {
      return Util.blogMenu(useRoute().name)
    })

    onMounted(() => {
      $(".header-fixed").append('<div class="sidebar-overlay"></div>')
      $(document).on("click", "#mobile_btn", function () {
        $("main-wrapper").toggleClass("slide-nav")
        $(".sidebar-overlay").toggleClass("opened")
        $("html").addClass("menu-opened")
        return false
      })

      $(document).on("click", ".sidebar-overlay", function () {
        $("html").removeClass("menu-opened")
        $(this).removeClass("opened")
        $("main-wrapper").removeClass("slide-nav")
      })

      $(document).on("click", "#menu_close", function () {
        $("html").removeClass("menu-opened")
        $(".sidebar-overlay").removeClass("opened")
        $("main-wrapper").removeClass("slide-nav")
      })

      if ($(window).width() <= 991) {
        var Sidemenu = function () {
          this.$menuItem = $(".main-nav a")
        }
      }
      let $wrapper = $(".main-wrapper")
      $(".main-nav a").on("click", function (e) {
        if ($(this).parent().hasClass("has-submenu")) {
          e.preventDefault()
        } else {
          $wrapper.removeClass("slide-nav")
          $(".sidebar-overlay").removeClass("opened")
          $("html").removeClass("menu-opened")
        }
        if (!$(this).hasClass("submenu")) {
          $("ul", $(this).parents("ul:first")).slideUp(350)
          $("a", $(this).parents("ul:first")).removeClass("submenu")
          $(this).next("ul").slideDown(350)
          $(this).addClass("submenu")
        } else if ($(this).hasClass("submenu")) {
          $(this).removeClass("submenu")
          $(this).next("ul").slideUp(350)
        }
      })
    })

    return { currentPath, mentorMenu, menteeMenu, pagesMenu, blogMenu }
  }
}
</script>
