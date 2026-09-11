---
商材マスタ:
  - "[[VPNワイド(404号室)]]"
補足情報: cvn5000068072
顧客管理:
  - "[[00_Inbox/顧客資産移行/顧客情報/MEMORY株式会社|MEMORY株式会社]]"
主商材:
  - "[[フレッツ光ネクスト（MEMORY株式会社）]]"
オプション商材: []
種別:
  - NTT保守
  - サブスクリプション
  - VPN
受注CA: 飯島CA
保守企業:
  - "[[00_Inbox/顧客資産移行/顧客情報/NTT西日本ビジネスフロント株式会社|NTT西日本ビジネスフロント株式会社]]"
資産区分: 個別配備
---
```javascript
ip lan1 address 192.168.2.1/24
ip route default gateway tunnel 1
ip route 192.168.101.0/24 gateway pp 1

#VPNワイド接続設定
pp select 1
pp always-on on
pppoe use lan2
pp auth accept pap chap
pp auth myname user02@cvn5000068072 user02
ppp lcp mru on 1454
ip pp address 192.168.101.2/32
ip pp mtu 1454
ip pp secure filter in 2 4
ip pp secure filter out 1 3
pp enable 1

#トンネル設定
tunnel select 1
ipsec tunnel 1
ipsec sa policy 1 1 esp aes-cbc sha-hmac
ipsec ike keepalive use 1 on
ipsec ike local address 1 192.168.101.2
ipsec ike pre-shared-key 1 text vpnwide
ipsec ike remote address 1 192.168.101.1
ip tunnel tcp mss limit auto
tunnel enable 1

tunnel select 2
ipsec tunnel 2
ipsec sa policy 2 2 esp aes-cbc sha-hmac
ipsec ike keepalive use 2 on
ipsec ike local address 2 192.168.101.2
ipsec ike pre-shared-key 2 text vpnwide
ipsec ike remote address 2 192.168.101.3
ip tunnel tcp mss limit auto
tunnel enable 2

#IPsec設定
ipsec auto refresh on
ip filter 1 pass * 192.168.101.0/24 udp * 500
ip filter 2 pass 192.168.101.0/24 * udp * 500
ip filter 3 pass * 192.168.101.0/24 esp
ip filter 4 pass 192.168.101.0/24 * esp

#DHCPの設定
dhcp service server
dhcp server rfc2131 compliant except remain-silent
dhcp scope 1 192.168.2.2-192.168.2.191/24

#DNSの設定
dns host lan1
dns server 192.168.1.254
dns private address spoof on
```
