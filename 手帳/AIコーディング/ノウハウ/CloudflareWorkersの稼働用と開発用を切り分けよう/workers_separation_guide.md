---
notion-id: 2ee37ce6287181f9ab04e5c3173ca5aa
---
# Cloudflare Workers 環境分離ガイド

## 🎯 なぜ Workers を分離するのか

### 問題：開発と本番が同じ Workers だと…

- 🔥 **開発中のバグが本番ユーザーに影響する**
- 💥 **データ構造の変更でキャッシュが壊れる**
- 😱 **テスト中に本番データを誤って更新してしまう**
- 🚫 **安心して実験的なコードを試せない**

### 解決：環境を完全分離すると…

- ✅ **本番に影響を与えずに開発できる**
- ✅ **KV キャッシュも独立して安全**
- ✅ **いつでもロールバック可能**
- ✅ **GitHub Actions で自動デプロイ**

---

## 📋 やるべきこと（チェックリスト）

新しいプロジェクトで Workers を分離する際は、以下の手順で進めます。

### ステップ 1: `wrangler.toml` の設定

Workers の環境設定ファイルを編集して、本番と開発を定義します。

```toml
# 本番環境（デフォルト）
name = "my-worker"
main = "src/index.js"
compatibility_date = "2024-01-01"

# KV バインディング（本番用）
[[kv_namespaces]]
binding = "MY_CACHE"
id = "本番用のKV ID"  # Cloudflare ダッシュボードで確認

# 環境変数（本番用）
[vars]
ENVIRONMENT = "production"

# 開発環境
[env.dev]
name = "my-worker-dev"  # 重要：-dev を付ける

# KV バインディング（開発用）
[[env.dev.kv_namespaces]]
binding = "MY_CACHE"
id = "開発用のKV ID"  # 本番とは別のKV Namespace

# 環境変数（開発用）
[env.dev.vars]
ENVIRONMENT = "development"
```

**ポイント**:  
- `name` に `-dev` を付けて別の Worker として扱う  
- KV Namespace の `id` を本番と開発で分ける（これが超重要！）  
- 環境変数 `ENVIRONMENT` で判別できるようにしておく

---

### ステップ 2: KV Namespace を2つ作成

Cloudflare ダッシュボードで KV を作成します。

1. **Cloudflare ダッシュボード** → **Workers & Pages** → **KV**
2. **Create namespace** をクリック
3. 以下の2つを作成:
	- `MY_CACHE` (本番用)
	- `MY_CACHE_DEV` (開発用)
4. 作成後に表示される **ID** をコピーして `wrangler.toml` に貼り付け

---

### ステップ 3: GitHub ブランチ戦略

開発と本番でブランチを分けます。

```
main               ← 本番環境用
  └─ dev           ← 開発環境用（または develop, staging など）
```

**ブランチごとの役割**:  
- `main`: 本番デプロイ用。マージ前に十分な検証が必要  
- `dev`: 開発中のコード。自由に push して試せる

---

### ステップ 4: GitHub Actions で自動デプロイ

`.github/workflows/deploy-dev.yml` を作成します。

```yaml
name: Deploy to Development

on:
push:
branches:
- dev  # dev ブランチへの push でトリガー

jobs:
deploy:
runs-on: ubuntu-latest
name: Deploy to Cloudflare Workers (Dev)
steps:
-uses: actions/checkout@v4

-name: Deploy to Cloudflare Workers
uses: cloudflare/wrangler-action@v3
with:
apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
command: deploy --env dev  # --env dev が重要！
```

**GitHub Secrets の設定**:  
1. GitHub リポジトリ → **Settings** → **Secrets and variables** → **Actions**  
2. **New repository secret** をクリック  
3. 名前: `CLOUDFLARE_API_TOKEN`  
4. 値: Cloudflare の API トークン（ダッシュボードで生成）

---

### ステップ 5: 本番デプロイの設定

本番は手動デプロイか、Cloudflare の Git 連携を使います。

### 方法 A: 手動デプロイ（推奨）

```bash
# main ブランチに切り替え
git checkout main

# 本番環境にデプロイ
wrangler deploy
```

### 方法 B: Cloudflare Git 連携

1. Cloudflare ダッシュボード → **Workers & Pages**
2. **Create application** → **Pages** → **Connect to Git**
3. GitHub リポジトリを選択
4. ブランチを `main` に設定
5. デプロイコマンド: `wrangler deploy`

---

### ステップ 6: フロントエンドの接続先切り替え

JavaScript で接続先を環境ごとに切り替えます。

```jsx
// config.js

const CONFIG = {
  // 環境に応じて切り替え
  workerUrl: import.meta.env.MODE === 'production'
    ? 'https://my-worker.your-subdomain.workers.dev'
    : 'https://my-worker-dev.your-subdomain.workers.dev',
};

export default CONFIG;
```

または、ブランチごとに手動で書き換える方法も:

```jsx
// dev ブランチの config.js
const CONFIG = {
  workerUrl: 'https://my-worker-dev.your-subdomain.workers.dev',
};

// main ブランチの config.js
const CONFIG = {
  workerUrl: 'https://my-worker.your-subdomain.workers.dev',
};
```

---

## 🔄 開発ワークフロー

実際の開発手順は以下の通りです。

### 1. 開発開始

```bash
# dev ブランチに切り替え
git checkout dev

# 最新の main を取り込む（必要に応じて）
git merge main
```

### 2. コード修正

```bash
# ローカルで開発
wrangler dev  # ローカルサーバーで動作確認

# コミット & プッシュ
git add .
git commit -m "新機能を追加"
git push origin dev
```

### 3. 自動デプロイ

- GitHub に push すると GitHub Actions が自動実行
- `my-worker-dev` に自動デプロイされる
- 開発環境 URL で動作確認: `https://my-worker-dev.your-subdomain.workers.dev`

### 4. 本番反映

```bash
# main ブランチに切り替え
git checkout main

# dev をマージ
git merge dev

# プッシュ（手動デプロイの場合）
git push origin main

# 本番デプロイ
wrangler deploy
```

---

## ⚠️ よくあるミス

### ❌ KV の ID を間違える

```toml
# ダメな例：本番と開発で同じ ID
[[kv_namespaces]]
id = "同じID"

[env.dev.kv_namespaces]
id = "同じID"  # これだとキャッシュが混ざる！
```

### ❌ Worker 名を分けない

```toml
# ダメな例
name = "my-worker"

[env.dev]
name = "my-worker"  # 同じ名前だと上書きされる！
```

### ❌ デプロイコマンドを間違える

```bash
# ダメな例：開発環境に本番用をデプロイしてしまう
wrangler deploy  # --env dev を忘れた！
```

正しくは:

```bash
wrangler deploy --env dev
```

---

## 🎓 応用：さらに環境を増やす

開発・ステージング・本番の3環境構成も可能です。

```toml
# 本番
name = "my-worker"

# ステージング
[env.staging]
name = "my-worker-staging"
[[env.staging.kv_namespaces]]
binding = "MY_CACHE"
id = "ステージング用ID"

# 開発
[env.dev]
name = "my-worker-dev"
[[env.dev.kv_namespaces]]
binding = "MY_CACHE"
id = "開発用ID"
```

デプロイコマンド:

```bash
wrangler deploy --env dev       # 開発
wrangler deploy --env staging   # ステージング
wrangler deploy                 # 本番
```

---

## 📚 参考リンク

- [Cloudflare Workers - Environments](https://developers.cloudflare.com/workers/wrangler/configuration/#environments)
- [Wrangler Configuration](https://developers.cloudflare.com/workers/wrangler/configuration/)
- [GitHub Actions - Wrangler Action](https://github.com/cloudflare/wrangler-action)

---

## ✅ まとめ

環境分離で得られるメリット:

1. **安全性**: 本番に影響を与えずに開発
2. **効率性**: GitHub Actions で自動デプロイ
3. **柔軟性**: いつでもロールバック可能
4. **独立性**: KV キャッシュも完全分離

新しいプロジェクトを始める際は、最初から環境分離を設定しておくことを強く推奨します！