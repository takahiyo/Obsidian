---
notion-id: 811b85a332f4447993c0d1e9c830910b
URL: https://www.fujifilm.com/fb/support/callcenter/faq/ccfaq0037
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - 仕事
  - 知識
---
[[Windows共有フォルダMac接続トラブルシューティング]]

  

# 2024/12/17時点での成功情報

## Mac側の設定

> [!info] MacでSMBファイル共有を設定する  
> MacでSMBファイル共有をオンにできます。  
> https://support.apple.com/ja-jp/guide/mac-help/mh14107/mac  

上記リンクに従って共有設定を行う

- 「オプション」の’Windowsファイル共有’でアカウントのチェックは必須

## ゼロックス複合機側のSMB設定

- サーバーは固定したIPアドレスを入力する
	- 192.168.100.201
	- Mac上で共有表示される共有ホスト名は通らない
- 共有名は、共有対象にしたフォルダ名「だけ」を入力する
	- Web上などで、Macの共有フォルダの「場所」が「Macintosh HD→ユーザ→HirahaeTakahiro→デスクトップ→Scan」だとしたら、デスクトップ以降を入力とあったりする
- 保存場所は入力しない
	- これも、Web上では入力する様に指示されていることがある
- ユーザー名、パスワード
	- Macのログインアカウントを使用してもらう
	- everyoneは上手く通らない

  

# 基本情報

> [!info] WindowsユーザとMacファイルを共有する  
> お使いのMacにWindowsコンピュータからユーザが接続できるようにするには、ファイル共有をオンにして、SMB共有を有効にします。  
> https://support.apple.com/ja-jp/guide/mac-help/mchlp1657/mac  

> [!info] MacでスキャナーPC保存（SMB）の設定をしたい  
> [ 富士フイルムビジネスイノベーション ] サポート – [ 複合機 ][ プリンター ][ 複合機やプリンターのよくあるお問い合わせ ][ CCFAQ ][ コンテンツID:0037 ][ MacでスキャナーPC保存（SMB）の設定をしたい ][ Apeos 7580 / 6580 / 5580 ][ Apeos C4030 / C3530 ][ Apeos 5330 ][ Revoria Press SC180 / SC170 ][ Apeos C3067 / C3061 / C2561 / C2061 ][ Apeos C7071 / C6571 / C5571 / C4571 / C3571 / C2571 ]  
> https://www.fujifilm.com/fb/support/callcenter/faq/ccfaq0037  

1. 共有したいフォルダを作る
	- 例）desktop\scan
2. システム環境設定　→　共有　→　ファイル共有　と移動し、チェックを入れて有効にする
3. オプション　を開き、
	1. [SMBを使用してファイルやフォルダを共有]　にチェックを入れる
	2. 対象アカウントにチェックを入れる（パスワードを求められる）
4. 「共有フォルダ」下の［+］を押す
5. [1]で作成したフォルダを指定して[追加]を押す
6. このフォルダーにアクセスするユーザーの権限が「読み/書き」に設定されていることを確認する
7. [このMacについて]から[詳しい情報]　→　[システムレポート]　を開く

![[08_Storage/Attachments/MacOSと共有フォルダ/Untitled.png|Untitled.png]]

ユーザー名で使用するのは（）内で、ここでしか表示されないので留意すること

8. パソコンのIPアドレスを確認する