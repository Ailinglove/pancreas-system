<template>
  <div>
    <div id="tab-bar">
      <slot></slot>
    </div>
  </div>
</template>

<script>
  export default {
    name: "TabBar"
  }
</script>

<style scoped>
  #tab-bar{
    display: flex;
    text-align: center;
    background: #f6f6f6;

    box-shadow: 0 -1px 1px rgba(100,100,100,0.2);

    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
  }

</style>
