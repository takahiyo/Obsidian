---
notion-id: 86247e47-e86d-4214-8bf5-246832173184
base: "[[顧客資産管理.base]]"
補足情報: 参加者
💼 顧客管理:
  - "[[Notion/顧客情報/顧客管理/株式会社カネコ　名古屋支店/株式会社カネコ　名古屋支店|株式会社カネコ　名古屋支店]]"
主商材: []
オプション商材: []
種別:
  - NTT保守
  - VPN
受注CA: 大野CA
保守企業: []
---
# user01/05拠点

```javascript
# N1200 Rev.10.01.26 (Fri Jan 21 19:45:55 2011)
# MAC Address : 00:a0:de:68:38:91, 00:a0:de:68:38:92, 00:a0:de:68:38:93
# Memory 128Mbytes, 3LAN, 1BRI
# main:  N1200 ver=c0 serial=D2B001986 MAC-Address=00:a0:de:68:38:91 MAC-Addres
s=00:a0:de:68:38:92 MAC-Address=00:a0:de:68:38:93
# Reporting Date: Oct 9 14:41:27 2024
administrator password *
security class 1 on on
ip route default gateway pp 2
ip route 192.168.2.0/24 gateway tunnel 1
ip route 192.168.3.0/24 gateway tunnel 2
ip route 192.168.4.0/24 gateway tunnel 3
ip route 192.168.5.0/24 gateway tunnel 4
ip route 192.168.6.0/24 gateway tunnel 5
ip route 192.168.7.0/24 gateway tunnel 6
ip route 192.168.8.0/24 gateway tunnel 7
ip route 192.168.9.0/24 gateway tunnel 8
ip route 192.168.101.2 gateway pp 1
ip route 192.168.101.3 gateway pp 1
ip route 192.168.101.4 gateway pp 1
ip route 192.168.101.5 gateway pp 1
ip route 192.168.101.6 gateway pp 1
ip route 192.168.101.7 gateway pp 1
ip route 192.168.101.8 gateway pp 1
ip route 192.168.101.9 gateway pp 1
ipv6 prefix 1 ra-prefix@lan2::/64
ip lan1 address 192.168.1.1/24
ipv6 lan1 prefix ra-prefix@lan2::/64
ipv6 lan1 rtadv send 1
pp select 1
 pp always-on on
 pppoe use lan2
 pppoe auto disconnect off
 pp auth accept pap chap
 pp auth myname user01@cvn5000004209 user01
 ppp lcp mru on 1454
 ppp ccp type none
 ip pp address 192.168.101.1/32
 ip pp mtu 1454
 pp enable 1
pp select 2
 description pp PRV/PPPoE/1:OCN
 pp keepalive interval 30 retry-interval=30 count=12
 pp always-on on
 pppoe use lan2
 pppoe auto disconnect off
 pp auth accept pap chap
 pp auth myname w429y1xm@one.ocn.ne.jp mjwc82
 ppp lcp mru on 1454
 ppp ipcp ipaddress on
 ppp ipcp msext on
 ppp ccp type none
 ip pp secure filter in 201003 201020 201021 201022 201023 201024 201025 201030 201032 201080
 ip pp secure filter out 201013 201020 201021 201022 201023 201024 201025 201026 201027 201099 dynamic 201080 201081 201082 201083 201084 201098 201099
 ip pp nat descriptor 1100
 pp enable 2
tunnel select 1
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.1 192.168.101.2
 ip tunnel tcp mss limit auto
 tunnel enable 1
tunnel select 2
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.1 192.168.101.3
 ip tunnel tcp mss limit auto
 tunnel enable 2
tunnel select 3
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.1 192.168.101.4
 ip tunnel tcp mss limit auto
 tunnel enable 3
tunnel select 4
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.1 192.168.101.5
 ip tunnel tcp mss limit auto
 tunnel enable 4
tunnel select 5
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.1 192.168.101.6
 ip tunnel tcp mss limit auto
 tunnel enable 5
tunnel select 6
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.1 192.168.101.7
 ip tunnel tcp mss limit auto
 tunnel enable 6
tunnel select 7
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.1 192.168.101.8
 ip tunnel tcp mss limit auto
 tunnel enable 7
tunnel select 8
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.1 192.168.101.9
 ip tunnel tcp mss limit auto
 tunnel enable 8
ip filter 201000 reject 10.0.0.0/8 * * * *
ip filter 201001 reject 172.16.0.0/12 * * * *
ip filter 201002 reject 192.168.0.0/16 * * * *
ip filter 201003 reject 192.168.1.0/24 * * * *
ip filter 201010 reject * 10.0.0.0/8 * * *
ip filter 201011 reject * 172.16.0.0/12 * * *
ip filter 201012 reject * 192.168.0.0/16 * * *
ip filter 201013 reject * 192.168.1.0/24 * * *
ip filter 201020 reject * * udp,tcp 135 *
ip filter 201021 reject * * udp,tcp * 135
ip filter 201022 reject * * udp,tcp netbios_ns-netbios_ssn *
ip filter 201023 reject * * udp,tcp * netbios_ns-netbios_ssn
ip filter 201024 reject * * udp,tcp 445 *
ip filter 201025 reject * * udp,tcp * 445
ip filter 201026 restrict * * tcpfin * www,21,nntp
ip filter 201027 restrict * * tcprst * www,21,nntp
ip filter 201030 pass * 192.168.1.0/24 icmp * *
ip filter 201031 pass * 192.168.1.0/24 established * *
ip filter 201032 pass * 192.168.1.0/24 tcp * ident
ip filter 201033 pass * 192.168.1.0/24 tcp ftpdata *
ip filter 201034 pass * 192.168.1.0/24 tcp,udp * domain
ip filter 201035 pass * 192.168.1.0/24 udp domain *
ip filter 201036 pass * 192.168.1.0/24 udp * ntp
ip filter 201037 pass * 192.168.1.0/24 udp ntp *
ip filter 201080 pass * 192.168.1.1 4 * *
ip filter 201099 pass * * * * *
ip filter dynamic 201080 * * ftp
ip filter dynamic 201081 * * domain
ip filter dynamic 201082 * * www
ip filter dynamic 201083 * * smtp
ip filter dynamic 201084 * * pop3
ip filter dynamic 201098 * * tcp
ip filter dynamic 201099 * * udp
nat descriptor type 1100 masquerade
nat descriptor masquerade static 1100 105 192.168.1.1 4
dhcp service server
dhcp scope 1 192.168.1.10-192.168.1.50/24
dns server pp 2
dns server select 500002 pp 2 any . restrict pp 2
dns private address spoof on
snmp sysname ntt-n1200-00a0de683891
schedule at 1 */* 09:42:00 * ntpdate ntp-tk01.ocn.ad.jp syslog
statistics cpu on
statistics memory on
```

```javascript
#拠点向け通信とISPのデフォルトゲートウェイを確認する

console prompt user01
ip route 192.168.2.0/24 gateway tunnel 1
ip route 192.168.3.0/24 gateway tunnel 2
ip route 192.168.4.0/24 gateway tunnel 3
ip route 192.168.5.0/24 gateway tunnel 4
ip route 192.168.6.0/24 gateway tunnel 5
ip route 192.168.7.0/24 gateway tunnel 6
ip route 192.168.8.0/24 gateway tunnel 7
ip route 192.168.9.0/24 gateway tunnel 8
ip route 192.168.101.2 gateway pp 1
ip route 192.168.101.3 gateway pp 1
ip route 192.168.101.4 gateway pp 1
ip route 192.168.101.5 gateway pp 1
ip route 192.168.101.6 gateway pp 1
ip route 192.168.101.7 gateway pp 1
ip route 192.168.101.8 gateway pp 1
ip route 192.168.101.9 gateway pp 1
#IPv6を有効化するなら維持する
ipv6 prefix 1 ra-prefix@lan2::/64
ipv6 lan1 prefix ra-prefix@lan2::/64
ipv6 lan1 rtadv send 1
#VPNワイド用PP
pp select 1
 pp always-on on
 pppoe use lan2
 pppoe auto disconnect off
 pp auth accept pap chap
 pp auth myname user01@cvn5000004209 user01
 ppp lcp mru on 1454
 ppp ccp type none
 ip pp address 192.168.101.1/32
 ip pp mtu 1454
 pp enable 1
#ISP用PP
pp select 2
 description pp PRV/PPPoE/1:OCN
 pp keepalive interval 30 retry-interval=30 count=12
 pp always-on on
 pppoe use lan2
 pppoe auto disconnect off
 pp auth accept pap chap
 pp auth myname w429y1xm@one.ocn.ne.jp mjwc82
 ppp lcp mru on 1454
 ppp ipcp ipaddress on
 ppp ipcp msext on
 ppp ccp type none
 ip pp secure filter in 201003 201020 201021 201022 201023 201024 201025 201030 201032 201080
 ip pp secure filter out 201013 201020 201021 201022 201023 201024 201025 201026 201027 201099 dynamic 201080 201081 201082 201083 201084 201098 201099
 ip pp nat descriptor 1100
 pp enable 2
 #tunnel
tunnel select 1
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.1 192.168.101.2
 ip tunnel tcp mss limit auto
 tunnel enable 1
tunnel select 2
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.1 192.168.101.3
 ip tunnel tcp mss limit auto
 tunnel enable 2
tunnel select 3
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.1 192.168.101.4
 ip tunnel tcp mss limit auto
 tunnel enable 3
tunnel select 4
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.1 192.168.101.5
 ip tunnel tcp mss limit auto
 tunnel enable 4
tunnel select 5
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.1 192.168.101.6
 ip tunnel tcp mss limit auto
 tunnel enable 5
tunnel select 6
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.1 192.168.101.7
 ip tunnel tcp mss limit auto
 tunnel enable 6
tunnel select 7
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.1 192.168.101.8
 ip tunnel tcp mss limit auto
 tunnel enable 7
tunnel select 8
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.1 192.168.101.9
 ip tunnel tcp mss limit auto
 tunnel enable 8

#NTPは有効にしておくが、GUIで良かろう
schedule at 1 */* 09:42:00 * ntpdate ntp-tk01.ocn.ad.jp syslog
```

# user03拠点

```javascript
# NVR510 Rev.15.01.14 (Fri Nov 16 16:15:56 2018)
# MAC Address : ac:44:f2:66:23:70, ac:44:f2:66:23:71
# Memory 256Mbytes, 2LAN, 1ONU
# main:  NVR510 ver=00 serial=M4X142347 MAC-Address=ac:44:f2:66:23:70 MAC-Addre
ss=ac:44:f2:66:23:71
# Reporting Date: Mar 27 13:43:32 2025
security class 1 on on off
console prompt user03
ip route default gateway tunnel 1
ip route 192.168.101.0/24 gateway pp 1
ipv6 prefix 1 ra-prefix@lan2::/64
ip lan1 address 192.168.3.1/24
ipv6 lan1 address ra-prefix@lan2::1/64
ipv6 lan1 rtadv send 1 o_flag=on
ipv6 lan1 dhcp service server
ipv6 lan2 dhcp service client ir=on
ngn type lan2 ntt
pp select 1
 pp always-on on
 pppoe use lan2
 pppoe auto disconnect off
 pp auth accept pap chap
 pp auth myname user03@cvn5000004209 user03
 ppp lcp mru on 1454
 ppp ipcp ipaddress on
 ppp ccp type none
 ip pp mtu 1454
 pp enable 1
tunnel select 1
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.3 192.168.101.1
 ip tunnel tcp mss limit auto
 tunnel enable 1
telnetd host lan
dhcp service server
dhcp server rfc2131 compliant except remain-silent
dhcp scope 1 192.168.3.60-192.168.3.80/24
dhcp client release linkdown on
dns server 192.168.1.1
dns private address spoof on
dns private name setup.netvolante.jp
analog supplementary-service pseudo call-waiting
analog extension dial prefix sip prefix="9#"
dashboard accumulate traffic on
```

```javascript
ログインパス：なし
アドミンパス：なし
ネット集約：あり

##　管理拠点をuser01からuser05へ変更　##

tunnel select 1
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.3 192.168.101.5
 ip tunnel tcp mss limit auto
 tunnel enable 1

dns server 192.168.5.1

##　他拠点から設定変更できるように設定、不要であれば削除で構いません　##

telnetd host any

save


```

# user08拠点

```javascript
# RTX1210 Rev.14.01.20 (Thu Jun  1 07:52:40 2017)
# MAC Address : ac:44:f2:6b:99:32, ac:44:f2:6b:99:33, ac:44:f2:6b:99:34
# Memory 256Mbytes, 3LAN, 1BRI
# main:  RTX1210 ver=00 serial=S4H164117 MAC-Address=ac:44:f2:6b:99:32 MAC-Addr
ess=ac:44:f2:6b:99:33 MAC-Address=ac:44:f2:6b:99:34
# Reporting Date: Mar 27 14:19:42 2025
security class 1 on on off
console prompt user08
ip route default gateway pp 2
ip route 192.168.0.0/16 gateway tunnel 1
ip route 192.168.101.0/24 gateway pp 1
ipv6 prefix 1 ra-prefix@lan2::/64
ip lan1 address 192.168.8.1/24
ipv6 lan1 address ra-prefix@lan2::1/64
ipv6 lan1 rtadv send 1 o_flag=on
ipv6 lan1 dhcp service server
ipv6 lan2 dhcp service client ir=on
ngn type lan2 ntt
pp select 1
 pp always-on on
 pppoe use lan2
 pppoe auto disconnect off
 pp auth accept pap chap
 pp auth myname user08@cvn5000004209 user08
 ppp lcp mru on 1454
 ppp ipcp ipaddress on
 ppp ccp type none
 ip pp mtu 1454
 pp enable 1
pp select 2
 pp keepalive interval 30 retry-interval=30 count=12
 pp always-on on
 pppoe use lan2
 pppoe auto disconnect off
 pp auth accept pap chap
 pp auth myname a65k7037@one.ocn.ne.jp xrik46
 ppp lcp mru on 1454
 ppp ipcp ipaddress on
 ppp ipcp msext on
 ppp ccp type none
 ip pp secure filter in 201003 201020 201021 201022 201023 201024 201025 201030
 201032
 ip pp secure filter out 201013 201020 201021 201022 201023 201024 201025 20102
6 201027 201099 dynamic 201080 201081 201082 201083 201084 201098 201099
 ip pp nat descriptor 1100
 pp enable 2
tunnel select 1
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.8 192.168.101.1
 ip tunnel tcp mss limit auto
 tunnel enable 1
ip filter 201000 reject 10.0.0.0/8 * * * *
ip filter 201001 reject 172.16.0.0/12 * * * *
ip filter 201002 reject 192.168.0.0/16 * * * *
ip filter 201003 reject 192.168.8.0/24 * * * *
ip filter 201010 reject * 10.0.0.0/8 * * *
ip filter 201011 reject * 172.16.0.0/12 * * *
ip filter 201012 reject * 192.168.0.0/16 * * *
ip filter 201013 reject * 192.168.8.0/24 * * *
ip filter 201020 reject * * udp,tcp 135 *
ip filter 201021 reject * * udp,tcp * 135
ip filter 201022 reject * * udp,tcp netbios_ns-netbios_ssn *
ip filter 201023 reject * * udp,tcp * netbios_ns-netbios_ssn
ip filter 201024 reject * * udp,tcp 445 *
ip filter 201025 reject * * udp,tcp * 445
ip filter 201026 restrict * * tcpfin * www,21,nntp
ip filter 201027 restrict * * tcprst * www,21,nntp
ip filter 201030 pass * 192.168.8.0/24 icmp * *
ip filter 201031 pass * 192.168.8.0/24 established * *
ip filter 201032 pass * 192.168.8.0/24 tcp * ident
ip filter 201033 pass * 192.168.8.0/24 tcp ftpdata *
ip filter 201034 pass * 192.168.8.0/24 tcp,udp * domain
ip filter 201035 pass * 192.168.8.0/24 udp domain *
ip filter 201036 pass * 192.168.8.0/24 udp * ntp
ip filter 201037 pass * 192.168.8.0/24 udp ntp *
ip filter 201099 pass * * * * *
ip filter dynamic 201080 * * ftp
ip filter dynamic 201081 * * domain
ip filter dynamic 201082 * * www
ip filter dynamic 201083 * * smtp
ip filter dynamic 201084 * * pop3
ip filter dynamic 201098 * * tcp
ip filter dynamic 201099 * * udp
nat descriptor type 1100 masquerade
dhcp service server
dhcp server rfc2131 compliant except remain-silent
dhcp scope 1 192.168.8.60-192.168.8.80/24
dhcp client release linkdown on
dns server pp 2
dns private address spoof on
dashboard accumulate traffic on
```

```javascript
ログインパス：なし
アドミンパス：なし
ネット集約：なし

##　管理拠点をuser01からuser05へ変更　##

tunnel select 1
 tunnel encapsulation ipip
 tunnel endpoint address 192.168.101.8 192.168.101.5
 ip tunnel tcp mss limit auto
 tunnel enable 1

##　他拠点から設定変更できるように設定、不要であれば削除で構いません　##

telnetd host any

save


```