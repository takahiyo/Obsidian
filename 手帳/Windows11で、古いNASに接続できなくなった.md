---
notion-id: 29637ce62871804a865cde54d57ac0e2
URL: https://chatgpt.com/g/g-p-68f09315215081918004668886be89bd-za-tan/shared/c/68f86f54-e054-8321-920e-d952cb1ae34e?owner_user_id=user-T8VkAYhH2UJGNj5nTVcxVCWM
更新されました: Invalid date
作成日時: Invalid date
---
# QUICが原因かも

```jsx
🔍 QUICとは

QUIC（Quick UDP Internet Connections） は、Google が開発し
現在は IETF（国際標準）で採用されている UDPベースの高速通信プロトコル です。

HTTP/3（ウェブ通信の最新版）や、
Windows の「SMB over QUIC」にも使われています。

特徴は：

TCPより高速（接続確立が1往復で完了）

TLS（暗号化）を必ず内包

中間機器（ファイアウォール等）に影響を受けにくい

モバイルやVPN経由の通信でも途切れにくい

💡 SMB over QUIC とは

従来の「ファイル共有（SMB）」通信は TCP 445番ポート を使いますが、
SMB over QUIC はこれを UDP 443番（HTTPSと同じ） に置き換えて
TLS暗号化付きで行う新方式です。

項目	従来SMB	SMB over QUIC
通信プロトコル	TCP	UDP(QUIC)
暗号化	任意（署名のみ）	TLS必須
通信ポート	445	443
接続対象	LAN内NASなど	クラウド／VPN越しサーバー想定
対応環境	SMB2/3以上	Windows Server 2022 以降、Azure Files など
```

## 症状が起きる条件

- QUIC導入後のWindowsOSで、初めてQUIC非対応のNASにアクセスする場合
- 同じOSバージョンでも、以前にSMB3以前で接続履歴があるOSをアップグレードした場合だと、接続履歴があるSMBでの接続が優先される

## QUICの確認方法

```jsx
Get-SmbClientConfiguration | Select EnableSMBQUIC
```

- 結果がTrueならQUICが有効、Falseなら無効
	- SMB接続後にアップグレードしたOSだと、Trueでも古いNASが利用できる

## QUICを無効化する

```jsx
クライアント側
Set-SmbClientConfiguration -EnableSMBQUIC $false

サーバー側　※ローカル共有側。通常はやらなくても良い
Set-SmbServerConfiguration -EnableSMBQUIC $false
```

- Falseになったら、再起動する