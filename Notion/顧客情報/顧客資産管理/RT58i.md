---
notion-id: 1cf37ce6-2871-8061-aa89-ff74df5e1676
base: "[[顧客資産管理.base]]"
補足情報: ""
💼 顧客管理:
  - "[[Notion/顧客情報/顧客管理/浄西寺/浄西寺|浄西寺]]"
主商材: []
オプション商材: []
種別: []
保守企業: []
---
[]()

```javascript
# tftpで取得や更新を行うための設定情報です。
# この設定をルータに再設定する場合には、tftpクライアントをご利用ください。

#	N58i Rev.9.01.36 (Fri Nov 21 18:14:37 2008)
#		MAC Address : 00:a0:de:54:77:34, 00:a0:de:54:77:35
#		Memory 32Mbytes, 2LAN, 1BRI
#		main:  N58i ver=c0 serial=D29002463 MAC-Address=00:a0:de:54:77:34 MAC-Address=00:a0:de:54:77:35
# Reporting Date: Jan 6 03:51:34 1980
ip route default gateway pp 1 filter 500000 gateway pp 1
ipv6 prefix 1 ra-prefix@lan2::/64
ip lan1 address 192.168.1.1/24
ip lan1 secure filter in 100000 100001 100002 100003 100004 100005 100006 100007 100099
ipv6 lan1 prefix ra-prefix@lan2::/64
ipv6 lan1 rtadv send 1
ipv6 lan2 rip send off
ipv6 lan2 rip receive off
provider type isdn-terminal
provider filter routing connection
provider lan1 name LAN:
provider lan2 name PPPoE/0/1/5/0/0/0:plala
pp select 1
 pp name PRV/1/1/5/0/0/0:plala
 pp keepalive interval 30 retry-interval=30 count=12
 pp always-on on
 pppoe use lan2
 pppoe auto disconnect off
 pppoe call prohibit auth-error count off
 pp auth accept pap chap
 pp auth myname 578fj8783@plala.or.jp zyc7twhj8vfuz
 ppp lcp mru on 1454
 ppp ipcp ipaddress on
 ppp ipcp msext on
 ppp ccp type none
 ip pp secure filter in 200003 200020 200021 200022 200023 200024 200025 200030 200032
 ip pp secure filter out 200013 200020 200021 200022 200023 200024 200025 200026 200027 200099 dynamic 200080 200081 200082 200083 200084 200098 200099
 ip pp nat descriptor 1000
 pp enable 1
provider set 1 plala
 provider dns server pp 1 1
 provider select 1
ip filter 100000 reject * * udp,tcp 135 *
ip filter 100001 reject * * udp,tcp * 135
ip filter 100002 reject * * udp,tcp netbios_ns-netbios_dgm *
ip filter 100003 reject * * udp,tcp * netbios_ns-netbios_dgm
ip filter 100004 reject * * udp,tcp netbios_ssn *
ip filter 100005 reject * * udp,tcp * netbios_ssn
ip filter 100006 reject * * udp,tcp 445 *
ip filter 100007 reject * * udp,tcp * 445
ip filter 100099 pass * * * * *
ip filter 200000 reject 10.0.0.0/8 * * * *
ip filter 200001 reject 172.16.0.0/12 * * * *
ip filter 200002 reject 192.168.0.0/16 * * * *
ip filter 200003 reject 192.168.1.0/24 * * * *
ip filter 200010 reject * 10.0.0.0/8 * * *
ip filter 200011 reject * 172.16.0.0/12 * * *
ip filter 200012 reject * 192.168.0.0/16 * * *
ip filter 200013 reject * 192.168.1.0/24 * * *
ip filter 200020 reject * * udp,tcp 135 *
ip filter 200021 reject * * udp,tcp * 135
ip filter 200022 reject * * udp,tcp netbios_ns-netbios_ssn *
ip filter 200023 reject * * udp,tcp * netbios_ns-netbios_ssn
ip filter 200024 reject * * udp,tcp 445 *
ip filter 200025 reject * * udp,tcp * 445
ip filter 200026 restrict * * tcpfin * www,21,nntp
ip filter 200027 restrict * * tcprst * www,21,nntp
ip filter 200030 pass * 192.168.1.0/24 icmp * *
ip filter 200031 pass * 192.168.1.0/24 established * *
ip filter 200032 pass * 192.168.1.0/24 tcp * ident
ip filter 200033 pass * 192.168.1.0/24 tcp ftpdata *
ip filter 200034 pass * 192.168.1.0/24 tcp,udp * domain
ip filter 200035 pass * 192.168.1.0/24 udp domain *
ip filter 200036 pass * 192.168.1.0/24 udp * ntp
ip filter 200037 pass * 192.168.1.0/24 udp ntp *
ip filter 200098 reject-nolog * * established
ip filter 200099 pass * * * * *
ip filter 500000 restrict * * * * *
ip filter dynamic 200080 * * ftp
ip filter dynamic 200081 * * domain
ip filter dynamic 200082 * * www
ip filter dynamic 200083 * * smtp
ip filter dynamic 200084 * * pop3
ip filter dynamic 200098 * * tcp
ip filter dynamic 200099 * * udp
nat descriptor type 1000 masquerade
dhcp service server
dhcp server rfc2131 compliant except remain-silent
dhcp scope 1 192.168.1.101-192.168.1.191/24
dns server pp 1
dns server select 500001 pp 1 any . restrict pp 1
dns private address spoof on
analog supplementary-service pseudo call-waiting
analog extension dial prefix line
analog extension dial prefix sip prefix="9#"
```