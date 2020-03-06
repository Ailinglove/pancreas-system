<template>
  <div class="yh-page">
    <h1>弹出框演示</h1>

    <el-button @click="showPopup">显示弹出框</el-button>
    <yh-popup-page ref="popup" title="弹出框" @close="onClose">
      <div>
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="名称" prop="name">
            <el-input v-model="form.name" style="width:300px;" size="small"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button class="yh-primary" @click.prevent="submitForm">提交</el-button>
            <el-button>重置</el-button>
          </el-form-item>
        </el-form>
      </div>
    </yh-popup-page>
  </div>
</template>
<script>
import popuppage from "../test/Pop";
export default {
  name: "PopupPageDemo",
  data() {
    return {
      form: {
        name: ""
      }
    };
  },
  methods: {
    showPopup() {
      this.$refs.popup.show();
    },
    onClose(page) {
      page.close();
    },
    submitForm() {
      this.$refs.popup.close();
    }
  },
  components: {
    "yh-popup-page": popuppage
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scope>
</style>
