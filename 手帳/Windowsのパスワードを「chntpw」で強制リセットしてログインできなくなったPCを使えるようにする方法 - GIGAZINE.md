---
notion-id: 8da25340b2a84785b630e62bf641c719
URL: https://gigazine.net/news/20200314-chntpw/
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - 知識
  - 記事
---
# **Windowsのパスワードを「chntpw」で強制リセットしてログインできなくなったPCを使えるようにする方法**

[![](https://i.gzn.jp/img/2020/03/14/chntpw/00_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/00_m.png)

コンピューターにパスワードを設定することは、セキュリティの観点から非常に大切なことですが、そのパスワードを失念してしまったり、前の持ち主からパスワードを聞きそびれてしまったりした場合、コンピューター内のデータにアクセスできなくなってしまう事態に陥ってしまいます。「chntpw」はWindowsのパスワードを強制リセットし、そうした事態を回避することができるコマンドです。

**chntpw | Remove, bypass, unlock and reset forgotten Windows password**

[**http://www.chntpw.com/**](http://www.chntpw.com/)

Windowsのパスワードを忘れてしまい、誤ったパスワードを入力すると、画像のように「パスワードが正しくありません。入力し直してください。」と表示され、ログインができなくなってしまいます。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/005_m.jpg)](https://i.gzn.jp/img/2020/03/14/chntpw/005_m.jpg)

chntpwはLinux上で動作するコマンド。今回はUbuntu 18.04を用いてchntpwを使ってみます。まずは下記サイトにアクセスしてOSをダウンロード。

**Ubuntuを入手する | Ubuntu | Ubuntu**

[**https://jp.ubuntu.com/download**](https://jp.ubuntu.com/download)

赤枠の「ダウンロード」をクリックすると、ファイルをダウンロードできます。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/010_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/010_m.png)

続いて、OS起動用のUSBメモリーを作成するための「**Rufus**」を下記からダウンロード。

**Rufus - 起動可能なUSBドライブを簡単に作成できます**

[**https://rufus.ie/ja_JP.html**](https://rufus.ie/ja_JP.html)

「ダウンロード」下の赤枠部分をクリックして実行ファイルをダウンロードします。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/040_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/040_m.png)

ダウンロードした実行ファイルを起動すると、Rufusが起動します。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/050_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/050_m.png)

USBメモリーをPCに挿入。使用するUSBメモリーの容量は4GBあれば十分です。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/060_m.jpg)](https://i.gzn.jp/img/2020/03/14/chntpw/060_m.jpg)

挿入したUSBメモリーがRufusに認識されたことを確認したら、「選択」をクリックして……

[![](https://i.gzn.jp/img/2020/03/14/chntpw/070_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/070_m.png)

先ほどダウンロードした拡張子が「iso」のファイルを選択し「開く」へ進みます。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/080_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/080_m.png)

選択したファイル名が表示されていることを確認したら、「スタート」をクリック。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/090_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/090_m.png)

モードの確認画面が表示されますが、そのままの設定で「OK」をクリックします。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/100_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/100_m.png)

USBメモリーの内容が消去される旨の注意画面が表示されるので、「OK」で先へ進むと……

[![](https://i.gzn.jp/img/2020/03/14/chntpw/110_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/110_m.png)

USBメモリーへISOファイルの内容がインストールされ始めます。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/120_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/120_m.png)

進捗を表す緑色のバーに「準備完了」と表示されたら、USBメモリーを取り外します。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/130_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/130_m.png)

作成したUSBメモリーをパスワードをリセットしたいPCに挿入します。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/135_m.jpg)](https://i.gzn.jp/img/2020/03/14/chntpw/135_m.jpg)

PCを再起動し、[**BIOS**](https://ja.wikipedia.org/wiki/Basic_Input/Output_System)画面を表示。BIOS画面の表示方法はPCによって異なります。「終了」タブで先ほど挿入したUSBメモリーを選択すると……

[![](https://i.gzn.jp/img/2020/03/14/chntpw/140_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/140_m.png)

USBメモリーにインストールしたUbuntuが起動します。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/150_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/150_m.png)

Ubuntuが起動したら、左のリストから「日本語」を選択して「Ubuntuを試す」をクリック。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/160_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/160_m.png)

デスクトップが表示されたら、左下のボタンをクリックします。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/165_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/165_m.png)

検索窓で「Update」と検索すると表示される赤枠のソフトを起動。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/170_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/170_m.png)

赤枠にチェックを入れて「Close」と進みます。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/180_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/180_m.png)

パッケージ情報のアップデートを促されるので「Reload」をクリック。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/190_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/190_m.png)

情報のアップデートが行われます。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/200_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/200_m.png)

続いて先ほどの検索窓で「Terminal」と検索。ターミナルを起動します。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/210_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/210_m.png)

下記コマンドを入力して、chntpwをインストールします。

> sudo apt install chntpw

ターミナルに入力するとこんな感じ。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/220_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/220_m.png)

「Enter」キーを押すとインストールが始まります。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/230_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/230_m.png)

インストールが完了したらファイラーを起動します。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/240_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/240_m.png)

「Other Location」へと進み、Windowsがインストールされているディスクを選択します。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/250_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/250_m.png)

WindowsのCドライブのディレクトリが表示されるので、「Windows」をクリック。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/260_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/260_m.png)

次は「System32」をクリックします。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/270_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/270_m.png)

「config」フォルダを見つけたら、右クリックして「Open in Terminal」をクリック。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/280_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/280_m.png)

ターミナルが起動したら下記コマンドを入力。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/290_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/290_m.png)

> sudo chntpw -u パスワードをリセットしたいユーザー名 SAM

ユーザー名が「admin」の場合はこんな感じ。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/300_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/300_m.png)

コマンドを実行すると、モードを選択する画面が表示されます。この時点でエラーが生じた場合は、一度Windowsを起動した上で、再起動するとうまくいく場合があります。今回はパスワードをリセットするため「1」を入力して「Enter」キーを押します。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/320_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/320_m.png)

実行に成功するとすぐにパスワードがリセットされるので、続いて「q」を入力して「Enter」キー。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/330_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/330_m.png)

ファイルへ情報を書き込むかどうか尋ねられるので「y」を入力して「Enter」キーを押します。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/340_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/340_m.png)

Windowsを起動するため、Ubuntuを終了します。右上のメニューをクリックし、電源ボタンをクリック。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/350_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/350_m.png)

「Shutdown」をクリックしていったんPCの電源をオフにします。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/360_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/360_m.png)

PCからUSBメモリーを取り外し、再度PCを起動すると、Windowsが起動します。パスワードが設定されている場合はパスワードの入力が求められますが……

[![](https://i.gzn.jp/img/2020/03/14/chntpw/370_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/370_m.png)

パスワードが未設定の状態にリセットされているので、パスワードを入力することなくWindowsにログインすることができました。

[![](https://i.gzn.jp/img/2020/03/14/chntpw/380_m.png)](https://i.gzn.jp/img/2020/03/14/chntpw/380_m.png)

![[00_m.png]]

コンピューターにパスワードを設定することは、セキュリティの観点から非常に大切なことですが、そのパスワードを失念してしまったり、前の持ち主からパスワードを聞きそびれてしまったりした場合、コンピューター内のデータにアクセスできなくなってしまう事態に陥ってしまいます。「chntpw」はWindowsのパスワードを強制リセットし、そうした事態を回避することができるコマンドです。

**chntpw | Remove, bypass, unlock and reset forgotten Windows password**

[**http://www.chntpw.com/**](http://www.chntpw.com/)

Windowsのパスワードを忘れてしまい、誤ったパスワードを入力すると、画像のように「パスワードが正しくありません。入力し直してください。」と表示され、ログインができなくなってしまいます。

![[005_m.jpg]]

chntpwはLinux上で動作するコマンド。今回はUbuntu 18.04を用いてchntpwを使ってみます。まずは下記サイトにアクセスしてOSをダウンロード。

**Ubuntuを入手する | Ubuntu | Ubuntu**

[**https://jp.ubuntu.com/download**](https://jp.ubuntu.com/download)

赤枠の「ダウンロード」をクリックすると、ファイルをダウンロードできます。

![[010_m.png]]

続いて、OS起動用のUSBメモリーを作成するための「**Rufus**」を下記からダウンロード。

**Rufus - 起動可能なUSBドライブを簡単に作成できます**

[**https://rufus.ie/ja_JP.html**](https://rufus.ie/ja_JP.html)

「ダウンロード」下の赤枠部分をクリックして実行ファイルをダウンロードします。

![[040_m.png]]

ダウンロードした実行ファイルを起動すると、Rufusが起動します。

![[050_m.png]]

USBメモリーをPCに挿入。使用するUSBメモリーの容量は4GBあれば十分です。

![[060_m.jpg]]

挿入したUSBメモリーがRufusに認識されたことを確認したら、「選択」をクリックして……

![[070_m.png]]

先ほどダウンロードした拡張子が「iso」のファイルを選択し「開く」へ進みます。

![[080_m.png]]

選択したファイル名が表示されていることを確認したら、「スタート」をクリック。

![[090_m.png]]

モードの確認画面が表示されますが、そのままの設定で「OK」をクリックします。

USBメモリーの内容が消去される旨の注意画面が表示されるので、「OK」で先へ進むと……

USBメモリーへISOファイルの内容がインストールされ始めます。

進捗を表す緑色のバーに「準備完了」と表示されたら、USBメモリーを取り外します。

作成したUSBメモリーをパスワードをリセットしたいPCに挿入します。

![[135_m.jpg]]

PCを再起動し、[**BIOS**](https://ja.wikipedia.org/wiki/Basic_Input/Output_System)画面を表示。BIOS画面の表示方法はPCによって異なります。「終了」タブで先ほど挿入したUSBメモリーを選択すると……

USBメモリーにインストールしたUbuntuが起動します。

Ubuntuが起動したら、左のリストから「日本語」を選択して「Ubuntuを試す」をクリック。

デスクトップが表示されたら、左下のボタンをクリックします。

検索窓で「Update」と検索すると表示される赤枠のソフトを起動。

赤枠にチェックを入れて「Close」と進みます。

パッケージ情報のアップデートを促されるので「Reload」をクリック。

情報のアップデートが行われます。

続いて先ほどの検索窓で「Terminal」と検索。ターミナルを起動します。

下記コマンドを入力して、chntpwをインストールします。

> sudo apt install chntpw

ターミナルに入力するとこんな感じ。

「Enter」キーを押すとインストールが始まります。

インストールが完了したらファイラーを起動します。

「Other Location」へと進み、Windowsがインストールされているディスクを選択します。

WindowsのCドライブのディレクトリが表示されるので、「Windows」をクリック。

次は「System32」をクリックします。

「config」フォルダを見つけたら、右クリックして「Open in Terminal」をクリック。

ターミナルが起動したら下記コマンドを入力。

> sudo chntpw -u パスワードをリセットしたいユーザー名 SAM

ユーザー名が「admin」の場合はこんな感じ。

コマンドを実行すると、モードを選択する画面が表示されます。この時点でエラーが生じた場合は、一度Windowsを起動した上で、再起動するとうまくいく場合があります。今回はパスワードをリセットするため「1」を入力して「Enter」キーを押します。

実行に成功するとすぐにパスワードがリセットされるので、続いて「q」を入力して「Enter」キー。

ファイルへ情報を書き込むかどうか尋ねられるので「y」を入力して「Enter」キーを押します。

Windowsを起動するため、Ubuntuを終了します。右上のメニューをクリックし、電源ボタンをクリック。

「Shutdown」をクリックしていったんPCの電源をオフにします。

PCからUSBメモリーを取り外し、再度PCを起動すると、Windowsが起動します。パスワードが設定されている場合はパスワードの入力が求められますが……

パスワードが未設定の状態にリセットされているので、パスワードを入力することなくWindowsにログインすることができました。