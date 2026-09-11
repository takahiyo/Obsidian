---
notion-id: 990a4be7827b4608a403f40f76546a40
更新されました: Invalid date
作成日時: Invalid date
---
1. インターネットにおける最適なMTUを確認する
    
	https://www.speedguide.net/analyzer.php
    
	※参考値にはなるが、手順2以降で1ずつ確認した方が正確
    
2. PINGでMTUの断片化状況をコマンドプロンプトで確認する
    
	ping /f /l 1472 [www.google.com](http://www.google.com/)
    
	※/fで断片化禁止必須
    
	※この場合、1472+28でMTU1500は有効と判断する
    
3. 現在のMTU値をコマンドプロンプトで確認する
    
	netsh interface ipv4 show interface
    
4. MTU値をコマンドプロンプトで変更する
    
	netsh interface ipv4 set interface ? mtu=1500