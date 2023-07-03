<template>
  <div>
    <router-view />
  </div>
</template>

<script lang="ts">
import { onMounted } from "vue";

export default {
  name: "App",
  setup() {
    onMounted(() => {
      console.log("mounted")
    })
  }
}
</script>

