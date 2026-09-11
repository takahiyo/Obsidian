---
notion-id: 2a337ce62871800191b2e944aa87c29e
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - アプリ
ファイル&メディア:
  - "[[OG4xx8XXPasswordMakingTool-main.zip]]"
---
---

[[CloudstoreFireBaseDatabeseの秘密鍵]]

# プロジェクト分析レポート

## 📋 プロジェクト概要

このプロジェクトは、**OG4xx/OG8xx VoIPゲートウェイ機器のパスワード生成ツール**です。MACアドレスから特定のアルゴリズムでパスワードを生成するWebアプリケーションで、以下の3層構造で構成されています：

```
[ブラウザ (HTML/JS)] → [Cloudflare Workers (プロキシ)] → [Google Apps Script (パスワード生成ロジック)]
```

### プロジェクトの目的

- VoIP機器のMACアドレスから管理用パスワードを生成
- ブラウザから簡単にアクセスできるWebインターフェース提供
- CORS問題の回避とセキュアな通信経路の確保

---

## 📂 ファイル構成と詳細

### 1. **index.html** (フロントエンド UI)

### 役割

ユーザーインターフェースを提供するシングルページアプリケーション。

### 主な機能

**UIコンポーネント:**

- **MACアドレス入力欄**: ユーザーがMACアドレスを入力（例: 00:11:22:33:44:55）
- **生成ボタン**: パスワード生成を実行
- **パスワード表示欄**: 生成されたパスワードを表示（読み取り専用）
- **コピーボタン**: クリップボードへのコピー機能
- **接続チェックボタン**: 通信経路の診断機能

**通信処理 (2段階のフォールバック機構):**

```jsx
// 第1段階: Fetch API経由のPOSTリクエスト (優先)
async function requestPasswordViaFetch(mac) {
  // タイムアウト設定: 8秒
  // application/x-www-form-urlencodedでPOST
  // エラー時は第2段階へフォールバック
}

// 第2段階: JSONPフォールバック (Fetch失敗時)
function requestPasswordViaJsonp(mac, previousErrorMessage) {
  // <script>タグによる動的読み込み
  // Fetch APIが使えない環境でも動作
}
```

**バリデーション処理:**

- MACアドレスの正規化（コロン、ハイフン、ドット、空白を除去）
- 12文字の16進数文字列チェック
- エラーメッセージの表示

**診断機能:**

- Fetch経由の通信テスト
- JSONPフォールバックのテスト
- 応答時間の計測
- 詳細なエラーメッセージとアドバイス表示

**セキュリティ対策:**

- パスワードのマスキング表示（診断結果で表示時）
- タイムアウト処理（8秒）
- エラーハンドリング

---

### 2. **ClaudFlare_worker.js** (Cloudflare Workers - プロキシ層)

### 役割

ブラウザとGoogle Apps Script間のプロキシとして動作し、CORS問題を解決する中間層。

### 主な機能

**エンドポイント処理:**

```jsx
export default {
  async fetch(request, env) {
    // GET/POST/OPTIONSリクエストを処理
    // GASへプロキシしてCORSヘッダーを付与
  }
}
```

**サポートする通信方式:**

1. **GET リクエスト**: クエリパラメータでMACアドレスを受信
2. **POST リクエスト**: 以下の3形式をサポート
	- `application/json`
	- `application/x-www-form-urlencoded`
	- `text/plain`

**CORS対応:**

```jsx
"Access-Control-Allow-Origin": "*"  // すべてのオリジンを許可
"Access-Control-Allow-Methods": "GET,POST,OPTIONS"
"Access-Control-Allow-Headers": "Content-Type"
"Access-Control-Max-Age": "86400"  // 24時間キャッシュ
```

**JSONPサポート:**

- `callback`パラメータがある場合、JSONP形式で応答
- コールバック名のサニタイジング（英数字とアンダースコア、ドットのみ許可、最大100文字）

**エラーハンドリング:**

- MACアドレス未指定エラー（400）
- GAS呼び出し失敗エラー（502）
- JSON解析エラー（502）
- 内部エラー（500）

**環境変数:**

- `ALLOW_ORIGIN`: CORS許可オリジン（デフォルト: ）
- `GAS_ENDPOINT`: GASのURL（デフォルト値が定数で定義済み）

---

### 3. **GAS_code.gs** (Google Apps Script - ビジネスロジック層)

### 役割

MACアドレスからパスワードを生成する核心ロジックを実装。

### パスワード生成アルゴリズム

```jsx
const FIXED_KEY = 'VoIPGateway48231';  // 固定鍵

function generatePassword(macRaw) {
  // 1. MACアドレスの正規化（12桁の16進数に変換）
  // 2. 特定位置の文字を抽出: mac[2:12] + mac[6:12]
  //    例: 001122334455 → 1122334455334455 (16文字)
  // 3. ビットOR演算でパスワード生成
  for (let i = 0; i < mac16enc.length; i++) {
    const m = mac16enc.charCodeAt(i);    // MAC文字のASCIIコード
    const k = FIXED_KEY.charCodeAt(i % FIXED_KEY.length);  // 鍵文字
    let p = String.fromCharCode(m | k);   // ビットOR演算

    // 使用可能文字チェック（0-9A-Za-z/_- および印字可能範囲）
    if (!(/[0-9A-Za-z\/_-]/.test(p)) || code < 0x21 || code > 0x7e) {
      p = '_';  // 不正な文字は '_' に置換
    }
    password += p;
  }
}
```

**入力パラメータ抽出:**

```jsx
function extractMac(e) {
  // 1. URLパラメータから取得 (e.parameter.mac)
  // 2. POSTボディから取得:
  //    - JSON形式
  //    - URLエンコード形式
  //    - プレーンテキスト形式
}
```

**バリデーション:**

- MACアドレスの存在チェック
- 長さチェック（12文字）
- 16進数チェック（0-9A-F）

**レスポンス形式:**

```jsx
// 成功時
{ "password": "生成されたパスワード" }

// エラー時
{ "error": "エラーメッセージ" }
```

**CORS対応:**

- すべてのレスポンスにCORSヘッダーを付与
- GET/POST/OPTIONSメソッドをサポート

**JSONPサポート:**

- `callback`パラメータが指定された場合、JavaScript形式で応答
- `callback({"password":"..."});` 形式

---

## 🔄 システムフロー

### 正常系の処理フロー

```
1. ユーザーがMACアドレスを入力（例: 00:11:22:33:44:55）
   ↓
2. [index.html] クライアント側でバリデーション
   - コロン等を除去して正規化 → 001122334455
   - 12桁の16進数チェック
   ↓
3. [index.html] Cloudflare WorkersへPOSTリクエスト
   - URL: https://og4xx8xxpasswordmakingtool.taka-hiyo.workers.dev/
   - Body: mac=001122334455
   ↓
4. [ClaudFlare_worker.js] リクエストを受信
   - MACパラメータを抽出
   - CORSヘッダーを付与
   ↓
5. [ClaudFlare_worker.js] GASへPOSTリクエスト
   - URL: https://script.google.com/macros/s/.../exec
   - Body: mac=001122334455
   ↓
6. [GAS_code.gs] パスワード生成
   - 正規化: 001122334455
   - 抽出: 1122334455334455
   - ビットOR演算でパスワード生成
   ↓
7. [GAS_code.gs] JSON応答を返却
   - { "password": "生成されたパスワード" }
   ↓
8. [ClaudFlare_worker.js] CORSヘッダー付きで転送
   ↓
9. [index.html] パスワードを画面に表示
   - ユーザーはコピーボタンでクリップボードにコピー可能
```

### フォールバック機構

```
Fetch API失敗時 (ネットワークエラー、CORS問題など)
   ↓
JSONP方式に自動切り替え
   ↓
<script>タグを動的に挿入してGETリクエスト
   ↓
コールバック関数でパスワードを受信
```

---

## 🔒 セキュリティ設計

### 1. **入力サニタイジング**

- MACアドレスの正規化と厳格なバリデーション
- JSONPコールバック名のサニタイジング

### 2. **CORS設定**

- Cloudflare Workersで適切なCORSヘッダーを付与
- プリフライトリクエスト（OPTIONS）のサポート

### 3. **タイムアウト処理**

- 8秒のタイムアウトで無限待機を防止

### 4. **エラーハンドリング**

- 各層で適切なエラーメッセージを返却
- ユーザーに診断機能を提供

---

## 🎨 ユーザー体験 (UX)

### レスポンシブデザイン

```css
@media (max-width: 480px) {
  /* モバイル対応のスタイル調整 */
}
```

### アクセシビリティ

- `aria-live="polite"` による診断結果の読み上げサポート
- ラベルとフォーム要素の適切な関連付け

### エラー表示

- 視認性の高い赤色のエラーメッセージ
- 具体的なエラー内容と対処方法の提示

---

## 🛠️ 技術スタック

|層|技術|用途|
|---|---|---|
|**フロントエンド**|HTML5, CSS3, Vanilla JavaScript|UI/UX、クライアント側処理|
|**プロキシ層**|Cloudflare Workers|CORS対応、リクエスト転送|
|**バックエンド**|Google Apps Script|パスワード生成ロジック|

---

## 🔧 設定箇所

### エンドポイントURL設定

```jsx
// index.html (121行目)
const GAS_ENDPOINT = "https://og4xx8xxpasswordmakingtool.taka-hiyo.workers.dev/";

// ClaudFlare_worker.js (3行目)
const DEFAULT_GAS_ENDPOINT = "https://script.google.com/macros/s/.../exec";
```

---

## 📊 まとめ

このプロジェクトは、**シンプルながら堅牢な3層アーキテクチャ**を採用しています：

### 強み

✅ **冗長性**: Fetch失敗時のJSONPフォールバック

✅ **CORS対応**: Cloudflare Workersによる完全な解決

✅ **診断機能**: ユーザー自身で問題を特定可能

✅ **セキュリティ**: 入力検証、タイムアウト、エラーハンドリング

✅ **ユーザビリティ**: 直感的なUI、クリップボードコピー機能

### 用途

VoIP機器（OG4xx/OG8xxシリーズ）の管理者が、機器のMACアドレスから管理用パスワードを迅速に生成するための専用ツールです。

---

以上が、現在のコードベースの詳細な分析レポートです。何か追加で確認したい点や、改善提案が必要な箇所があればお知らせください！