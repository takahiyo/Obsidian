---
notion-id: 88a8973007e64c268f98b564c55f55a1
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - 仕事
  - 知識
---
【概要】

パブリックとプライベートを変更したい

【手法1　Windows10等】

「ネットワークとインターネット」から「状態」「プロパティ」で変更できる

【手法2　1が使えなかった場合】

1. PowerShellを管理者権限で起動する
2. Get-NetConnectionProfile　を実行する
3. 結果の内、「InterfaceIndex」の数字を控える
4. Set-NetConnectionProfile -InterfaceIndex InterfaceIndexの番号 -NetworkCategory Private　を実行する
5. 手法1のプロパティで変更されたことを確認する