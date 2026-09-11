---
notion-id: a5c3a3b7f4854ba5979a40c6c4475015
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - アプリ
  - 個人
---
- [[コード作成時の参照レポート]] — ![[PythonNetworkGuiReport.txt]] / NetworkChange.pyを作成した際、完成するまでにあった試行錯誤をレポートにしたもの
- [[実行アプリ選択ダイアログ表示]] — ![[AppSelect.bat]]![[08_Storage/Attachments/実行アプリ選択ダイアログ表示/appselect.pyw|appselect.pyw]]![[08_Storage/Attachments/実行アプリ選択ダイアログ表示/AppSelect_Settings.json|AppSelect_Settings.json]] / １．ZIPファイル等に「AppSelect.bat」を紐づける  <br>２．appselect.pywがAppSelect__Setting.jsonを参照し、実行アプリのボタンを表示する  <br>３．選んだアプリに対して実行したファイルのパスを渡す
- [[ネットワークアダプター設定チェンジャー]] — ![[NetworkChange.py]]![[networkchange.rar]] / CUIとGUIの自動切り替え対応  <br>実行すると、ネットワークアダプターの一覧が表示される  <br>その後、コード内で準備しておいた固定アドレスにするか、DHCPに戻すかを選択する
- [[Windowsのスクリーンセーバーや画面オフを一時停止する]] — ![[ScreenOff_Stopper.pyw]] / 実行するとタスクトレイにシンプルな■アイコンが表示される  <br>🟦はスクリーンセーバーが有効で安全  <br>🟥はスクリーンセーバーが無効で危険  <br>というイメージ
- [[環境情報]] — Python3.10環境でPyinstallerによる実行ファイル作成もできた際のWhereコマンド結果一覧  <br>  <br>D:\Python>where python  <br>C:\Users\takah\AppData\Local\Programs\Python\Python310\python.exe  <br>C:\Users\takah\AppData\Local\Microsoft\WindowsApps\python.exe  <br>  <br>D:\Python>where pip  <br>C:\Users\takah\AppData\Local\Programs\Python\Python310\Scripts\pip.exe  <br>C:\Users\takah\AppData\Local\Microsoft\WindowsApps\pip.exe  <br>  <br>D:\Python>where pyinstaller  <br>C:\Users\takah\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\pyinstaller.exe
