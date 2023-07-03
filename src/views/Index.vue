<template>
  <div class="main-wrapper">
    <layout-header />
    <HomeBanner />
    <!-- <layout-footer /> -->
  </div>
</template>

<script>
import { defineComponent } from "vue"
import HomeBanner from "../components/HomeBanner.vue"

export default defineComponent({
  name: "TodoItem",
  components: {
    HomeBanner
  }
})
</script>
