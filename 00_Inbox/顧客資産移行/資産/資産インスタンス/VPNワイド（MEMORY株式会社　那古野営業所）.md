---
商材マスタ:
  - "[[VPNワイド]]"
補足情報: cvn5000068072
顧客管理:
  - "[[00_Inbox/顧客資産移行/顧客情報/MEMORY株式会社　那古野営業所|MEMORY株式会社　那古野営業所]]"
主商材:
  - "[[フレッツ光ネクスト（MEMORY株式会社　那古野営業所）]]"
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
[https://miro.com/app/board/uXjVJWceXX4=/?share_link_id=333922916505](https://miro.com/app/board/uXjVJWceXX4=/?share_link_id=333922916505)

[https://bit.ly/46r1hat](https://bit.ly/46r1hat)

```javascript
あさいさんNVR510　借り受け時

ip route default gateway pp 1
ip lan1 address 192.168.2.1/24
pp select 1
 description pp ISP
 pp keepalive interval 30 retry-interval=30 count=12
 pp always-on off
 pppoe use lan2
 pppoe auto connect off
 pppoe auto disconnect off
 pp auth accept pap chap
 pp auth myname f.u6728wf278z@atson.net rumw5et6
 ppp lcp mru on 1454
 ppp ipcp ipaddress on
 ppp ipcp msext on
 ppp ccp type none
 ip pp secure filter in 200003 200020 200021 200022 200023 200024 200025 200030
 200032
 ip pp secure filter out 200013 200020 200021 200022 200023 200024 200025 20002
6 200027 200099 dynamic 200080 200081 200082 200083 200084 200085 200098 200099
 ip pp nat descriptor 1000
 pp enable 1
ip filter 200000 reject 10.0.0.0/8 * * * *
ip filter 200001 reject 172.16.0.0/12 * * * *
ip filter 200002 reject 192.168.0.0/16 * * * *
ip filter 200003 reject 192.168.2.0/24 * * * *
ip filter 200010 reject * 10.0.0.0/8 * * *
ip filter 200011 reject * 172.16.0.0/12 * * *
ip filter 200012 reject * 192.168.0.0/16 * * *
ip filter 200013 reject * 192.168.2.0/24 * * *
ip filter 200020 reject * * udp,tcp 135 *
ip filter 200021 reject * * udp,tcp * 135
ip filter 200022 reject * * udp,tcp netbios_ns-netbios_ssn *
ip filter 200023 reject * * udp,tcp * netbios_ns-netbios_ssn
ip filter 200024 reject * * udp,tcp 445 *
ip filter 200025 reject * * udp,tcp * 445
ip filter 200026 restrict * * tcpfin * www,21,nntp
ip filter 200027 restrict * * tcprst * www,21,nntp
ip filter 200030 pass * 192.168.2.0/24 icmp * *
ip filter 200031 pass * 192.168.2.0/24 established * *
ip filter 200032 pass * 192.168.2.0/24 tcp * ident
ip filter 200033 pass * 192.168.2.0/24 tcp ftpdata *
ip filter 200034 pass * 192.168.2.0/24 tcp,udp * domain
ip filter 200035 pass * 192.168.2.0/24 udp domain *
ip filter 200036 pass * 192.168.2.0/24 udp * ntp
ip filter 200037 pass * 192.168.2.0/24 udp ntp *
ip filter 200099 pass * * * * *
ip filter 500000 restrict * * * * *
ip filter dynamic 200080 * * ftp
ip filter dynamic 200081 * * domain
ip filter dynamic 200082 * * www
ip filter dynamic 200083 * * smtp
ip filter dynamic 200084 * * pop3
ip filter dynamic 200085 * * submission
ip filter dynamic 200098 * * tcp
ip filter dynamic 200099 * * udp
nat descriptor type 1000 masquerade
telnetd host lan
dhcp service server
dhcp server rfc2131 compliant except remain-silent
dhcp scope 1 192.168.2.100-192.168.2.200/24 expire 24:00 maxexpire 24:00
dns host lan1
dns server pp 1
dns server select 500001 pp 1 any . restrict pp 1
dns private address spoof on
dns private name setup.netvolante.jp
analog supplementary-service pseudo call-waiting
analog extension dial prefix sip prefix="9#"
alarm entire off
statistics traffic on
```
