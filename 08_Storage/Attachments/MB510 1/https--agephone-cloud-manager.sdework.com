<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="robots" content="noindex, nofollow">
  <title>ログイン</title>
  <link rel="stylesheet" href="./css/jquery-ui.css" />
  <link rel="stylesheet" href="./css/style.css" />
</head>
<body id="main-login" class="hidden">
  <div id="v-header-public"></div>
  <div id="v-login" class="main">
    <div class="content-wide">
      <form @submit.prevent="login">
        <input-container :label="label.acLoginIdPublic" :err="getErr('acLoginId')">
          <input type="text" v-model="form.acLoginId" @input="validate('acLoginId')">
        </input-container>
        <input-container :label="label.acPassword" :err="getErr('acPassword')">
          <input type="password" v-model="form.acPassword" @input="validate('acPassword')">
        </input-container>
        <input-container :label="label.acConPassword" :err="getErr('acConPassword')">
          <input type="password" v-model="form.acConPassword" @input="validate('acConPassword')">
        </input-container>
        <input type="submit" class="mb" value="ログイン" >
      </form>
    </div>
  </div>

  <div id="v-footer-public"></div>

  <!-- ライブラリ -->
  <script src="./js/lib/jquery-3.4.1.min.js"></script>
  <script src="./js/lib/jquery-ui.min.js"></script>
  <script src="./js/lib/vue.min.js"></script>
  <script src="./js/lib/jquery.blockUI.js"></script>
  <!-- 共通 -->
  <script src="./js/app.js"></script>
  <script src="./js/shared.js"></script>
  <script src="./js/api.js"></script>
  <script src="./js/session.js"></script>
  <script src="./js/validator.js"></script>
  <script src="./js/v-common.js"></script>
  <!-- 個別 -->
  <script src="./js/v-header.js"></script>
  <script src="./js/v-login.js"></script>
  <script src="./js/v-footer.js"></script>
</body>
</html>