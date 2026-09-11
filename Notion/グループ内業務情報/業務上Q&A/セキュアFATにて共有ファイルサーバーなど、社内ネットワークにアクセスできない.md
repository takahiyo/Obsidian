---
notion-id: b7dbe3d1-1b02-41e8-9cd2-941f6176a673
base: "[[業務上Q&A.base]]"
タグ: []
---
# 対処方法

1. 【WiFi接続確認・再接続】
	1. WiFiが接続されていることを確認ください。
	2. 接続されている場合は、切断ボタンを押してください。
	3. 切断確認後、接続ボタンを押してください。
2. 【Zscalerアプリケーション起動】
	4. 画面左下のWindowsマークを左クリック
	5. 一覧内にある　Zscaler　を選択
	6. Zscalerをクリックしアプリケーションの起動を確認
3. 【Zscaler内の操作方法：状況確認】
	7. Zscaler画面左側にある　Private Accese を左クリック
	8. 右側2行目に記載の　Service Status が ON（緑色の文字）になっているかを確認
		- ONではない場合は、authenticate　を行い再認証を行うことで ON になります。
4. 【Zscaler内の操作方法：対処方法】
	9. Zscaler画面左側にある　More　を左クリック
	10. Zscaler画面右側　About　内の　Update Policy　を左クリック　    →　ウィンドウが立ち上がり完了後消えます。
	11. Zscaler画面右側　Troubleshoot　内の　Clear Logs　を左クリック    →　ウィンドウが立ち上がり完了後消えます。
	12. Zscaler画面右側　Troubleshoot　内の　Restart Service　を左クリック
		- continueボタンが表示された際はボタンを左クリックすることで Restart が実施されます。上記完了後に　共有ファイルサーバー（bf-cldstrg-001）　へのアクセスをお試しくださいませ。
5. 上記を一通りやっても共有フォルダにアクセスできない場合は、一度OSからサインアウト→サインインすれば復活する場合がある
	13. この場合は、DdreamではなくOSのサインアウトで良い
