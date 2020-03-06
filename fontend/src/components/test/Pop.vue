<template>
  <div class="yh-popup-page" v-show="visible">
    <div class="yh-block">
      <div class="yh-headder">
        <span>{{title}}</span>
        <button @click="onClose" v-if="closable !== false" class="yh-icon">X</button>
      </div>
      <div class="yh-content">
        <slot></slot>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "PopupPage",
  data() {
    return {
      visible: false
    };
  },
  props: ["title", "closable"],
  methods: {
    onClose() {
      this.$emit("close", this);
    },
    close() {
      this.visible = false;
    },
    show() {
      this.visible = true;
    }
  }
};
</script>
<style scoped>
</style>
