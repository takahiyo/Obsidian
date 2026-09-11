---
notion-id: 2f137ce62871800c8516c022f6e6d5c4
テキスト: 下記参照
選択:
  - CloudFlareD1
---
**システム構成とCloudflare D1連携に関する開発記録****作成日:** 2026-01-23**対象バージョン:** v1.0 (commit: a961f3f)  
このドキュメントは、本ツールの現在の技術構成、特にCloudflare D1（データベース）との連携における設計意図、実装の工夫、および将来の開発に向けた改善点をまとめたものです。  
**1. システム構成概要**  
本システムは、静的なフロントエンドと、サーバーレスAPI（Cloudflare Workers）、およびエッジデータベース（Cloudflare D1）から構成される**「サーバーレス・3層アーキテクチャ」**を採用しています。  
**アーキテクチャ図**  
  
`graph TD User[ユーザー (Browser)] -->|HTTPS / Fetch API| Worker[Cloudflare Workers<br>(API Backend)] subgraph Frontend [Static Frontend] HTML[index.html] JS[script.js] Config[config.js] end subgraph Backend [Cloudflare Edge] Worker D1[(Cloudflare D1<br>SQLite Database)] end User -- 操作 --> HTML JS -- 設定参照 --> Config Worker -- SQL (Binding) --> D1 %% Data Flow Worker -- JSON (Password + DB Stats) --> User`  
**コンポーネントの役割**コンポーネント技術スタック役割SSOT/DRYへの取り組み**Frontend**HTML5, CSS3, Vanilla JSUI表示、入力バリデーション、APIコール`config.js` にAPI先やUI定数を集約**Backend**Cloudflare Workersパスワード生成ロジック、DB操作、APIエンドポイント提供バリデーションロジックの再利用（関数化）**Database**Cloudflare D1生成ログの保存 (`request_logs` テーブル)マイグレーションファイルによるスキーマ管理  
**2. Cloudflare D1 連携の設計と工夫**  
Cloudflare D1を採用し、Workerと連携させるにあたり、以下の設計判断を行いました。  
**2.1 同期書き込みと即時フィードバック****実装:**  
`worker.js` 内で `ctx.waitUntil()` を使用せず、`await env.DB.prepare(...).run()` で書き込み完了を待機してからレスポンスを返しています。**意図:**  
• **確実性の担保:** ログ保存が確実に成功したことを確認してからパスワードをユーザーに提示するため。  
• **運用状況の可視化:** レスポンスに `dbCount`（現在の総ログ件数）を含めることで、クライアントサイドで「システムが稼働し、データが蓄積されていること」を確認できるようにしました。これにより、管理者が利用した際にDBの健全性を簡易的にチェックできます。  
**2.2 バインディングによる疎結合とフェイルセーフ****実装:**  
`if (env.DB)` ブロックによる条件分岐。**意図:**  
• **開発環境への配慮:** D1バインディングが存在しないローカル環境や、最小構成でのテスト時において、DB機能が無効でもパスワード生成機能（コア機能）自体は動作するように設計しました。  
• **構成の柔軟性:** 将来的にDBを切り離したり、別のストレージに移行する場合でも、このブロックを変更するだけで対応可能です。  
**2.3 セキュリティ（SQLインジェクション対策）****実装:**  
  
プレースホルダ `?` を使用したプリペアドステートメントの徹底。  
  
`env.DB.prepare("INSERT INTO ... VALUES (?, ?, ?, ?)").bind(...)` **経緯:**  
  
ユーザー入力（MACアドレス）をそのままSQLに埋め込むリスクを排除するため、Cloudflare D1の標準的なベストプラクティスである `bind()` メソッドを全面的に採用しました。  
**3. 次の開発に活かす改善点 (Lessons Learned)**  
現状の構成における課題と、次回開発時に検討すべき事項です。  
**3.1 エラーハンドリングの戦略（Silent Save vs Strict Save）****現状:**  
  
ReadMe.md には「Silent Save（DB失敗でもエラーを出さない）」と記載されていますが、現在の `worker.js` は `try...catch` ブロック内でDBエラーが発生すると `500 Internal Server Error` を返し、パスワード生成も中断されます。**改善案:**  
  
仕様と実装の不一致を解消する必要があります。  
• **A案 (Strict):** ログ保存は必須要件とし、失敗時は生成しない（現状の実装通り）。ReadMeを修正する。  
• **B案 (Silent):** `env.DB` 処理部分を個別の `try...catch` で囲み、DBエラー時はログだけ残してパスワード生成結果を返すように変更する。  
**3.2 フロントエンドとバックエンドの設定共有****現状:**  
`config.js` でフロントエンドの設定を一元化しましたが、バックエンド（`worker.js`）には `FIXED_KEY` やバリデーションロジックが独立して存在しています。**改善案:**  
  
共通定数や共通ロジック（MACアドレスの正規化など）を `shared/` ディレクトリなどに切り出し、ビルドプロセス（esbuild等）を通じて両側から `import` できる構成にすると、DRY（Don't Repeat Yourself）をより徹底できます。  
**3.3 CSS変数とJS設定の完全同期****現状:**  
`config.js` に `UI.COLORS` を定義しましたが、`style.css` の `:root` 変数とは自動連動していません。**改善案:**  
  
JSでの動的スタイル適用、あるいはビルド時のCSS生成ツールを導入し、`config.js` の色定義を `style.css` に注入する仕組みを作ると、デザイン変更時の保守性が向上します。  
**3.4 デプロイ環境の分離 (Dev/Prod)****現状:**  
  
GitHub Actionsの設定上、ブランチによるデプロイ先の明確な切り分け（`wrangler.toml` の環境別設定や環境変数の注入）がファイルから読み取れませんでした。**改善案:**  
`wrangler.toml` に `[env.dev]` セクションを追加し、D1データベースIDやWorker名を明確に分離することで、開発中のデータ混入リスクを完全に排除できます。  
**4. D1 関連のコマンドメモ**  
開発およびトラブルシューティングで頻繁に使用するコマンドです。  
  
`# ローカルでのデータ確認 npx wrangler d1 execute og4xx8xxpassword_db --local --command "SELECT * FROM request_logs" # 本番環境へのスキーマ適用 npx wrangler d1 execute og4xx8xxpassword_db --file=./migrations/001_create_request_logs.sql # 本番データの確認 npx wrangler d1 execute og4xx8xxpassword_db --command "SELECT * FROM request_logs ORDER BY id DESC LIMIT 5"`