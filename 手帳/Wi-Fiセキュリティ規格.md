---
notion-id: 72273cc14e7b452e80bde437200bff49
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - セキュリティ
  - 仕事
  - 知識
---
【認証方式】

|   |   |   |   |
|---|---|---|---|
|名称|制定日|概要|解読状況|
|WEP|1997年|40ビットか128ビットの暗号鍵|☓|
|WPA|2002年10月|WEPの脆弱性を解決するために生まれたTKIPによる定期的な暗号鍵変更|☓|
|WPA2|2004年9月|AES導入により最大256ビットの暗号鍵|△※1|
|WPA3|2018年6月|SAEハンドシェイクにより、パスワード漏洩時でも暗号化※2辞書攻撃に対し、一定回数の失敗でロックされる機能追加EasyConnect、EnhancedOpen等利便性を向上させる機能追加|○|

※

1. 2017年10月にKRACKSと呼ばれる脆弱性が発見されている
    
	ただし、公表前にメーカーへの情報提供及び対策が行われており、実際にこの脆弱性を利用した被害は発生していない
    
2. 暗号鍵の確認時、送受信者は互いにハッシュ値による確認で整合を取るが、暗号鍵自体は通信させないことにより暗号化が解かれない
    
	また、クライアントがWPA3に対応していない場合はWPA2として通信できるため、互換性が保たれている
    

【暗号化方式/暗号化アルゴリズム】

|   |   |   |
|---|---|---|
|認証方式|暗号化方式|暗号化アルゴリズム|
|WPA2-PSK|CCMP|AES|
|TKIP|RC4||
|WPA-PSK|CCMP|AES|
|TKIP|RC4||
|WEP|WEP|RC4|

※一般に、AESはCCMPと同一視されいることから、以降CCMPと表記するべき場合でもAESとする

この通り、WPAでもAESは使用できるようになっている

WEPの脆弱性が問題になったことから、急遽開発段階だった規格を使用してWPAが制定されている

こういった経緯から、初期値ではWPAはTKIP、WPA2はAESとなっている場合が多い

【参考】

|   |   |   |   |   |
|---|---|---|---|---|
|Standard|WEP|WPA|WPA2|WPA3|
|**Release**|1997|2003|2004|2018|
|**Encryption**|RC4|TKIP with RC4|AES-CCMP|AES-CCMP & AES-**GCM**P|
|**Key Size(s)**|64-bit and 128|128-bit|128-bit|128 and 256 bit|
|**Cipher Type**|Stream|Stream|Block|Block|
|**Authentication**|Open System & Shared Key|PSK & 802.1x with EAP variant|PSK & 802.1x with EAP variant|**SAE** & 802.1x with EAP variant|

参考：https://tex2e.github.io/blog/crypto/wifi-wpa3