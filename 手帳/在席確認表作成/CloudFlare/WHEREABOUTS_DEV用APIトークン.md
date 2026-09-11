---
notion-id: 2ee37ce6287180a1b996c007b28c5d1f
---
アカウントの管理  
**アカウント API トークン**  
アカウント API トークンを管理します。ユーザー API トークンは、[マイ プロフィール] セクションにあります。

すべての API がアカウント API トークンの使用をサポートするとは保証されません。サポートされている API は開発者向けドキュメントに記載されています。

**Cloudflare Workers を編集する API トークンの作成に成功しました**  
  
Cloudflare API にアクセスするためにこのトークンをコピーします。セキュリティ上の理由のため、これは再び表示されません。[詳細](https://developers.cloudflare.com/fundamentals/api/how-to/create-via-api/)  
47OdgX9RK7XwDMAFajdGJiPsZHycTGJeXnZ0iZMD  
**このトークンをテストする**  
トークンが正しく機能していることを確認するには、テストするターミナル シェルに以下の CURL コマンドをコピーして貼り付けます。  
  
`curl "https://api.cloudflare.com/client/v4/accounts/01f96b532d61f9cebe2c01bd3e4082f2/tokens/verify" \ -H "Authorization: Bearer 47OdgX9RK7XwDMAFajdGJiPsZHycTGJeXnZ0iZMD"`