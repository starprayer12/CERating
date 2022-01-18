<template>
  <div class="context">
    <div class="con-img"></div>
    <div class="left-container">
      <div class="logo-box">
        <img src="../assets/logo.png" alt="" />
        <span>CERating</span>
      </div>
      <div class="text-box">
        <h3>让标准</h3>
        <p>成为人与自然之间的桥梁</p>
      </div>
      <div class="footer-box">
        <span class="footer-list">
          <a class="footer-about" target="_blank" href="/about"> 关于我们 </a>
          <span class="footer-line"></span>
          <a class="footer-help" target="_blank" href="">帮助</a>
        </span>
        <span class="footer-copyright"> 2022 ©CERating </span>
      </div>
    </div>
    <div class="container">
      <div class="form-box">
        <!-- 注册 -->
        <div class="register-box hidden">
          <h1>register</h1>
          <el-form
            ref="refRegisterForm"
            :model="registerForm"
            :rules="rulesRegister"
            class=""
          >
            <el-form-item prop="username">
              <el-input
                v-model="registerForm.username"
                placeholder="Username"
                class="lr-input"
              ></el-input>
            </el-form-item>
            <el-form-item prop="email">
              <el-input
                v-model="registerForm.email"
                placeholder="Email"
                class="lr-input"
              ></el-input>
            </el-form-item>
            <el-form-item prop="password">
              <el-input
                v-model="registerForm.password"
                type="password"
                placeholder="Password"
                class="lr-input"
              ></el-input>
            </el-form-item>
            <el-form-item prop="checkpassword">
              <el-input
                v-model="registerForm.checkpassword"
                type="password"
                placeholder="Enter your password again"
                class="lr-input"
              ></el-input>
            </el-form-item>
            <el-form-item>
              <el-button
                @click="handleRegister('refRegisterForm')"
                type="primary"
                >register</el-button
              >
            </el-form-item>
          </el-form>
        </div>
        <!-- 登录 -->
        <div class="login-box">
          <h1>login</h1>
          <el-form
            ref="refLoginForm"
            :model="loginForm"
            :rules="rulesLogin"
            class=""
          >
            <el-form-item prop="account">
              <el-input
                v-model="loginForm.account"
                placeholder="Account"
                class="lr-input"
              ></el-input>
            </el-form-item>
            <el-form-item prop="password">
              <el-input
                v-model="loginForm.password"
                type="password"
                placeholder="Password"
                class="lr-input"
              ></el-input>
            </el-form-item>
            <el-form-item>
              <el-button @click="handleLogin('refLoginForm')" type="primary"
                >login</el-button
              >
            </el-form-item>
          </el-form>
        </div>
      </div>
      <div class="con-box left">
        <h2>欢迎来到</h2>
        <h2><span>碳排放评测系统</span></h2>
        <p>来实时测评<span>碳排放</span>吧</p>
        <!-- <video src="../assets/login_register.mp4" muted loop autoplay></video> -->
        <img src="../assets/login_1.jpeg" alt="" />
        <p>已有账户？</p>
        <button id="login" @click="tologin">去登录</button>
      </div>
      <div class="con-box right">
        <h2>欢迎来到</h2>
        <h2><span>碳排放评测系统</span></h2>
        <p>来试一下测评<span>碳排放等级</span>吧</p>
        <!-- <video src="../assets/login_register.mp4" muted loop autoplay></video> -->
        <img src="../assets/login_2.jpeg" alt="" />
        <p>没有账户？</p>
        <button id="register" @click="toregister">去注册</button>
      </div>
    </div>
  </div>
</template>
<script>
import { getCurrentInstance } from "vue";
import { loginForm, rulesLogin } from "@/utils/loginValidators";
import { registerForm, rulesRegister } from "@/utils/registerValidators";
export default {
  name: "LoginRegister",
  components: {},
  setup() {
    const { ctx } = getCurrentInstance();

    // 登录/注册触发所有检验
    const handleRegister = (formName) => {
      ctx.$refs[formName].validate((valid) => {
        if (valid) {
          alert("submit!");
        } else {
          alert("error submit!");
          return false;
        }
      });
    };
    const handleLogin = (formName) => {
      ctx.$refs[formName].validate((valid) => {
        if (valid) {
          alert("submit!");
        } else {
          alert("error submit!");
          return false;
        }
      });
    };

    return {
      loginForm,
      registerForm,
      rulesRegister,
      rulesLogin,
      handleRegister,
      handleLogin,
    };
  },
  methods: {
    tologin() {
      document.getElementsByClassName("form-box")[0].style.transform =
        "translateX(0%)";
      document
        .getElementsByClassName("register-box")[0]
        .classList.add("hidden");
      document
        .getElementsByClassName("login-box")[0]
        .classList.remove("hidden");
    },
    toregister() {
      document.getElementsByClassName("form-box")[0].style.transform =
        "translateX(80%)";
      document.getElementsByClassName("login-box")[0].classList.add("hidden");
      document
        .getElementsByClassName("register-box")[0]
        .classList.remove("hidden");
    },
  },
};
</script>


<style scoped>
.context {
  margin: 0;
  padding: 0;
  /* 100%窗口高度 */
  height: 100vh;
  /* 弹性布局  水平+垂直居中 */
  display: flex;
  justify-content: center;
  align-items: center;
  /* 渐变背景 */
  /* background: linear-gradient(200deg, #f3e7e9, #e3eeff); */
  /* background-image: url("../assets/login_background.jpg"); */
}
.con-img {
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background: url("../assets/login_background.jpg") no-repeat;
  background-size: cover;
}
.text-box {
  position: fixed;
  left: 10%;
  top: 45%;
  color: #fff;
  display: block;
  text-align: left;
}
.text-box h3 {
  font-size: 54px;
  letter-spacing: 0;
  font-weight: 700;
}
.text-box p {
  font-size: 32px;
  letter-spacing: 3.81px;
  font-weight: 300;
}
/* 窗口变化会导致text-box隐藏 */
@media all and (max-width: 1000px) {
  /* max screen size */
  .text-box {
    display: none;
  }
}
.logo-box {
  position: fixed;
  left: 7%;
  top: 10%;
  color: #fff;
  text-align: left;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.logo-box span {
    margin-left: 10px;
    font-size: 30px;
    font-family: Times;
}
.logo-box img {
  height: 50px;
  width: 50px;
}
.footer-box {
  position: fixed;
  opacity: 0.78;
  left: 8%;
  bottom: 10%;
  font-size: 14px;
  color: #fff;
}
.footer-box a {
  text-decoration: none;
}
.footer-box a:hover {
  text-decoration: underline;
  /* font-weight: bold; */
  /* color: #BDCEFC; */
  opacity: 1;
}
.footer-box a:visited {
  color: #fff;
}
.footer-about .footer-help {
  opacity: 0.8;
  text-decoration: none;
  color: #fff;
  cursor: pointer;
}
.footer-line {
  display: inline-block;
  width: 2px;
  height: 12px;
  filter: alpha(opacity=78);
  opacity: 0.78;
  margin: 0 12px 0 13px;
  background: #fff;
  position: relative;
  top: 1px;
}
.footer-copyright {
  opacity: 0.54;
  font-size: 12px;
  color: #fff;
  display: inline-block;
  padding-left: 30px;
}
.container {
  background: rgba(255, 255, 255, 0.9);
  top: 16%;
  right: 7.5%;
  width: 660px;
  height: 450px;
  border-radius: 12px;
  overflow: hidden;
  /* 阴影 */
  box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.1);
  /* 相对定位 */
  position: absolute;
}
.form-box {
  position: absolute;
  left: 5%;
  background: linear-gradient(0, #d0dcf0, #bdcefc);
  width: 330px;
  height: 450px;
  /* border-radius: 5px; */
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2;
  /* 动画过渡 加速后减速 */
  transition: 0.5s ease-in-out;
}
.form-box:hover {
  box-shadow: 2px 0 5px 5px rgb(0 0 0 / 5%);
  transition: 0.5s;
}
.form-box button {
  width: 100%;
  margin-top: 20px;
  background-color: #f6f6f6;
  outline: none;
  border-radius: 5px;
  padding: 13px;
  color: #bdcefc;
  letter-spacing: 2px;
  border: none;
  cursor: pointer;
}
.form-box button:hover {
  background-color: #bdcefc;
  color: #f6f6f6;
  transition: background-color 0.5s ease;
}
.register-box,
.login-box {
  /* 弹性布局 垂直排列 */
  display: flex;
  flex-direction: column;
  align-items: center;
  widows: 100%;
}
.hidden {
  display: none;
  transition: 0.5s;
}
h1 {
  text-align: center;
  margin-bottom: 25px;
  /* 大写 */
  text-transform: uppercase;
  color: #fff;
  /* 字间距 */
  letter-spacing: 5px;
}
input {
  background-color: transparent;
  width: 70%;
  color: #fff;
  border: none;
  /* 下边框样式 */
  border-bottom: 1px solid rgba(255, 255, 255, 0.4);
  padding: 10px 0;
  text-indent: 10px;
  margin: 8px 0;
  font-size: 14px;
  letter-spacing: 2px;
}
input::placeholder {
  opacity: 0;
}
input:focus {
  color: #bdcefc;
  outline: none;
  border-bottom: 1px solid #a9b9ff;
  transition: 0.5s;
}
input:focus::placeholder {
  opacity: 0;
}
.con-box {
  width: 50%;
  /* 弹性布局 垂直排列 居中 */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  /* 绝对定位 居中 */
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
.con-box.left {
  left: -2%;
}
.con-box.right {
  right: -2%;
}
.con-box h2 {
  color: #8e9aaf;
  font-size: 18px;
  font-weight: bold;
  letter-spacing: 3px;
  text-align: center;
  margin-bottom: 4px;
}
.con-box p {
  font-style: 10px;
  letter-spacing: 2px;
  color: #8e9aaf;
  text-align: center;
}
.con-box span {
  color: #bdcefc;
}
.con-box video {
  width: 280px;
  height: 450px;
  object-fit: cover;
  opacity: 0.9;
  margin: 40px 0;
  position: fixed;
  z-index: -1;
}
.con-box img {
  width: 200px;
  height: 200px;
  opacity: 0.9;
  margin: 10px 0;
}
.con-box button {
  margin-top: 3%;
  background-color: #fff;
  color: #a9b9ff;
  border: 1px solid #bdcefc;
  padding: 6px 10px;
  border-radius: 5px;
  letter-spacing: 1px;
  outline: none;
  cursor: pointer;
}
.con-box button:hover {
  background-color: #bdcefc;
  color: #fff;
}
</style>