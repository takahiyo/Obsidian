---
notion-id: 3d808e80948b40b1906d969e00be245b
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - 仕事
  - 知識
  - 記事
---
# 概要

## **ヤマハルーター　DNSサーバー優先順位**

[https://www.noblehero.jp/2023/06/10/ヤマハルーター　dnsサーバー優先順位/](https://www.noblehero.jp/2023/06/10/%E3%83%A4%E3%83%9E%E3%83%8F%E3%83%AB%E3%83%BC%E3%82%BF%E3%83%BC%E3%80%80dns%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E5%84%AA%E5%85%88%E9%A0%86%E4%BD%8D/)

- 優先順位
	1. **dns server select** コマンド
	2. **dns server** コマンド
	3. **dns server pp** コマンド
	4. **dns server dhcp** コマンド

## ヤマハルータのDNSの設定見直しの勧め

https://note.com/sasakipochi/n/n27467541412c

- 最近ではリカーシブクエリの増大によって、TCPによる解決が必要になる場合が増えてきている
- YAMAHAはTCPによるリカーシブクエリ解決ができないため、遅延の原因になる
- DNSを8.8.8.8などに手動で設定するか、リカーシブサーバー機能を無効化した方が良い
    
	- DHCPによる払い出しDNS設定例
    
	```python
	dhcp scope option 1 dns=1.1.1.1,8.8.8.8
	```