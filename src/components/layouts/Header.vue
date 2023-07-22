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
        </div>
        <ul class="nav header-navbar-rht">
          <li class="nav-item">
            <!-- <router-link class="nav-link" to="/login">New Study Code</router-link> -->
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script>
import Util from "../../assets/utils/utils"
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
