---
notion-id: 5b48ff3047ea48728ca5e824e6635041
URL: https://atmarkit.itmedia.co.jp/ait/articles/2206/27/news035.html
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - 知識
  - 記事
---
# **パスワードを忘れたWindows 11にサインインする方法（UbuntuのインストールUSBメモリ編）**_**Tech TIPS**_

## スタッフの急な退社などでパスワードの分からないPCがある場合、どうしているだろうか。初期化しても問題ないPCならいいが、大事なデータが入っているような場合など、パスワードを再設定して使い続けたいということもあるだろう。そのような場合にパスワードを再設定する方法を紹介する。

2022年06月27日 05時00分 公開

[[小林章彦](https://www.itmedia.co.jp/author/194032/)，**デジタルアドバンテージ**]

|   |   |   |   |   |   |
|---|---|---|---|---|---|
|[印刷](https://id.itmedia.co.jp/isentry/contents?sc=0c1c43111448b131d65b3b380041de26f2edd6264ee1c371184f54d26ab53365&lc=7d7179c146d0d6af4ebd304ab799a718fe949a8dcd660cd6d12fb97915f9ab0a&return_url=https://ids.itmedia.co.jp/print/ait/articles/2206/27/news035.html&encoding=shift_jis&ac=e8cb9106baa7e37eb9feb877b9f0a27ddaf48b95ba02da49cbb3a8247ee7fec4&cr=e9fd42802bc22856808963077023568339063544b05e5a8646e62c02a898e0fd)|通知|[見る](https://twitter.com/search?q=https://atmarkit.itmedia.co.jp/ait/articles/2206/27/news035.html)|Share|[13](http://b.hatena.ne.jp/entry/https%3A%2F%2Fatmarkit.itmedia.co.jp%2Fait%2Farticles%2F2206%2F27%2Fnews035.html)||

この記事は会員限定です。**会員登録（無料）**すると全てご覧いただけます。

[![](https://image.itmedia.co.jp/ait/files/20010101/backn2.gif)](https://image.itmedia.co.jp/ait/files/20010101/backn2.gif)

[連載目次](https://atmarkit.itmedia.co.jp/ait/series/1751/index.html)

**対象：**Windows 11

**パスワードを忘れたWindows 11にサインインするには**PINやパスワードが分からないWindows 11。PCを再利用するのであれば、Windows 11を再インストールするのが無難だが、大事なデータやアクティベーションを解除しなければならないアプリがある場合は困る。そんな場合でも、ちょっとした裏技を使うと、パスワードの再設定が行えて、Windows 11にサインインできるようになる。その方法を解説しよう。

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword01.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword01.png)

「Windows 11」でパスワードやPINが分からなくなってサインインできなくなった、ということはないだろうか。

Microsoftアカウントでサインインしている場合、Microsoftアカウントの［パスワードのリセット］ページを開き、指示に従ってMicrosoftアカウント名やCAPTCHAを入力すると、パスワードリセット用のリンクがアカウント作成時に指定したメールアドレスに送られてくるので、メールに記載されたリンクを開き、新しいパスワードを設定すればよい。

- [パスワードのリセット](https://account.live.com/password/reset)（Microsoft）

また、ローカルアカウントでサインインしている場合は、インストール時に設定した秘密の質問でパスワードがリセットできる。

**秘密の質問の回答が分かればパスワードのリセットも可能**ローカルアカウントでサインインしている場合、インストール時などに設定した秘密の質問に回答できればパスワードがリセットできる。

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword02.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword02.png)

ところが、退社した人のPCなどは、Microsoftアカウントの［パスワードのリセット］ページや秘密の質問ではパスワードがリセットできない。そのため、Windows OSを初期化しなければならなくなったということもあるだろう。

ただ、初期化には時間がかかるし、ローカルストレージ上のデータや設定が失われてしまう危険性もある。また、アプリケーションによっては、アクティベーションを解除しないとライセンスが無駄になってしまう、といったケースもあるだろう。

[**製造業で進むデータ活用　必要なのは堅牢で俊敏な基盤構築**](https://dlv.itmedia.jp/rd/v1/j/on/c/chsm=90,785eec7d/2075501498/ISALM/408358/301031189.510389340.620304743/730393069/109634/2075501497:ISALM:*/l/sp=0;/g/B:aHR0cHM6Ly93d3cuaXRtZWRpYS5jby5qcC9lbnRlcnByaXNlL2FydGljbGVzLzIzMDkvMjIvbmV3czAwNC5odG1s)

[![](https://img.itmedia.jp/so/images/sa/b/287/293975/301031189/et230804_1_240.jpg)](https://img.itmedia.jp/so/images/sa/b/287/293975/301031189/et230804_1_240.jpg)

実は、パスワードやPINが分からなくなっても、ちょっとした操作でパスワードの再設定が可能だ。ただし、他人のPCに対して許可なく、サインインすると犯罪になるので、悪用は厳禁である。なお、BitLockerなどでストレージが暗号化されている場合は、この方法ではパスワードの解除はできないので注意してほしい。

### Windows 11のパスワードをリセットする手順

サインイン画面にある［コンピューターの簡単操作］アイコンをクリックするとコマンドプロンプトが開くように細工することで、パスワードの再設定を実現可能にする。

コマンドプロンプトを開くようにするには、［コンピューターの簡単操作］アイコンをクリックして実行される「utilman.exe（［コンピューターの簡単操作］の実行ファイル）」を、「cmd.exe（コマンドプロンプト）」に置き換える必要がある。ただ「utilman.exe」は、システムフォルダ（C:\windows\system32）にあるため、Windows 11が起動した状態では保護されており、置き換えができない。

また、以前のWindows OSと異なり、Windows OSのインストールメディア（インストールUSBメモリ）で起動してコマンドプロンプトを開いても、Windows 11のシステムドライブは見えないことがあり、単純にファイルの置き換えが行えない（Windows OSのインストールメディアを利用する場合は、Tech TIPS「[【Windows 10対応】パスワードを忘れたWindows OSにログオン（サインイン）する](https://atmarkit.itmedia.co.jp/ait/articles/1312/06/news055.html)」を参照してほしい）。

システムドライブが見えない場合、diskpartコマンドを使って、システムボリュームにドライブレターを割り当てる必要がある。ただ、diskpartコマンドは使い方を誤ると、データが失われてしまう危険性があるので慎重に操作してほしい（diskpartコマンドの使い方は、Tech TIPS「[Windowsのdiskpartコマンドでディスクのパーティションを操作する](https://atmarkit.itmedia.co.jp/ait/articles/0812/26/news119.html)」を参照してほしい）。

**Windows 11はWindows OSのインストールUSBメモリでは裏技が使えない？**Windows 10までは、ここでD:ドライブを開けば、［Windows］フォルダが見えたのだが……。Windows 11の場合、従来のWindows OSのインストールUSBメモリを使う方法では、システムドライブが見えず、ファイルの置き換えが行えない場合がある。この場合、diskpartコマンドを使って、システムボリュームにドライブレターを割り当てる必要がある。

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword03.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword03.png)

そこで、本稿ではWindows OSのインストールメディアではなく、Linuxのインストールディスクで起動して、「utilman.exe」を「cmd.exe」に置き換える操作を行う方法を紹介する。

### Ubuntuのインストールメディアを作成する

Linuxのディストリビューションは何でもいいが、ここではUbuntuを利用することにする。まずUbuntuのインストールメディアを作成しよう。

以下のWebページを開き、「Ubuntu Desktop **＜バージョン＞**」欄にある［ダウンロード］ボタンをクリックする。

- [Ubuntuを入手する](https://jp.ubuntu.com/download)（Canonical）

自動的にISOファイルのダウンロードが開始される。これを[Rufus](https://rufus.ie/ja/)などを使って、容量4GB以上のUSBメモリに書き込めば、UbuntuのインストールUSBメモリが作成できる（Rufusの使い方は、Tech TIPS「[Windows OSのインストールUSBメモリを作る（Rufus編）](https://atmarkit.itmedia.co.jp/ait/articles/1801/17/news021.html)」を参照してほしい）。Windows 11のインストールUSBメモリを作成するには容量8GB以上のUSBメモリが必要になるので、この点でもUbuntuを利用するメリットがある。

DVDドライブがあるようならば、ISOファイルをDVD-Rに書き込んでインストールDVDを作成してもよい。

**UbuntuのインストールUSBメモリを作成する（1）**

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword04.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword04.png)

▼

**UbuntuのインストールUSBメモリを作成する（2）**Rufusを使って、UbuntuのISOファイルをUSBメモリに書き込む。

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword05.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword05.png)

▼

**UbuntuのインストールUSBメモリを作成する（3）**

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword06.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword06.png)

### パスワードを忘れたPCをUbuntuのインストールUSBメモリで起動する

次に作成したUbuntuのインストールUSBメモリ／インストールDVDを使って、パスワードを忘れたPCを起動する。

Ubuntuの起動方法の選択画面が表示されたら、一番上の［Try or Install Ubuntu］が選択された状態で［Enter］キーを押す。［Install］画面が表示されたら、左側の言語リストで［日本語］を選択し、右側の［Ubuntuを試す］ボタンをクリックする。これでUbuntuをローカルストレージにインストールせずに実行することができる。この機能を利用して、Windows 11のシステムフォルダにアクセスする。

Ubuntuが起動したら、デスクトップの左側にある［Files］アイコンをクリックし、Windows OSのエクスプローラーに相当する「ファイル」アプリ（Nautilus）を起動する。単にファイルを救いたいだけならば、ここでUSBメモリなどにコピーすればよいが、ここではWindows 11にサインインして操作可能にすることを目的に話を進める。

「ファイル」アプリの左ペインで一番下にある［Other Locations］を選択すると、右ペインに「**＜ディスク容量＞** Volume」としてWindows 11のシステムドライブが見える。このフォルダを開けば、Windows 11のシステムドライブの中にアクセスできるので、「Windows」「System32」とフォルダを開いていく。

「utilman.exe」をバックアップ（「@utilman.exe」などの名前に変更）し、「cmd.exe（［コマンドプロンプト］の実行ファイル）」をデスクトップなどにドラッグ＆ドロップでコピーし、utilman.exeという名前に変更してから、「System32」フォルダにコピー（移動）するとよい。

**「utilman.exe」を「cmd.exe」に置き換える（1）**UbuntuのインストールUSBメモリから起動すると、この画面が表示される。ここでは［Try or Install Ubuntu］を選択する。

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword07.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword07.png)

▼

**「utilman.exe」を「cmd.exe」に置き換える（2）**

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword08.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword08.png)

▼

**「utilman.exe」を「cmd.exe」に置き換える（3）**Ubuntuのデスクトップが表示されたら、左側のバー（Ubuntu Dock）にある［Files］アイコンをクリックし、「ファイル」アプリを起動する。

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword09.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword09.png)

▼

**「utilman.exe」を「cmd.exe」に置き換える（4）**「ファイル」アプリの左ペインにある［Other Locations］を選択する。右ペインに「**＜ディスク容量＞** Volume」としてWindows 11のシステムドライブが見える。

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword10.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword10.png)

▼

**「utilman.exe」を「cmd.exe」に置き換える（5）**「Windows」「System32」と順番に開く。Windows 11の「Windows\System32」フォルダの中が見える。

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword11.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword11.png)

▼

**「utilman.exe」を「cmd.exe」に置き換える（6）**アドレスバーに「ut」と入力すると、フィルタリングされて、フォルダ内の「ut」という文字列が含まれるファイルが表示される。「utilman.exe」を見つけて、右クリックして、表示されたメニューの［Rename］を選択する。［Rename File］ダイアログが表示されるので、「utilman.exe」のファイル名を「@utilman.exe」などに変更する。

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword12.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword12.png)

▼

**「utilman.exe」を「cmd.exe」に置き換える（7）**同様にアドレスバーに「cmd」と入力して、「cmd.exe」を探し、これをデスクトップにドラッグ＆ドロップでコピーする。

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword13.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword13.png)

▼

**「utilman.exe」を「cmd.exe」に置き換える（8）**デスクトップ上で、「cmd.exe」のファイル名を「utilman.exe」に変更し、これを「System32」フォルダにドラッグ＆ドロップでコピーする。

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword14.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword14.png)

以上の操作が完了したら、Ubuntuの右上端の［電源］アイコンをクリックし、メニューの［Power Off/Log Off］を展開し、その中にある［Power Off］を選択して電源をオフにする。画面に「Please remove the installation medium, then press ENTER:」と表示されたら、USBメモリなどを抜き、［Enter］キーを押して、Ubuntuを完全に終了させてから、PCの電源をオフにする。

**Ubuntuの電源をオフにする（1）**デスクトップの右上にある［電源］アイコンをクリックし、メニューを表示、［Power Off/Log Off］を展開して、その中にある［Power Off］を選択する。確認ダイアログが表示されるので、［Power Off］ボタンをクリックする。

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword15.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword15.png)

▼

**Ubuntuの電源をオフにする（2）**このメッセージが表示されたら、USBメモリなどを抜き、［Enter］キーを押すと、電源がオフになる。

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword16.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword16.png)

### Windows 11のパスワードを変更する

PCの電源を入れてWindows 11が起動し、サインイン画面が表示されたら、右下の［コンピューターの簡単操作］アイコンをクリックする。すると、［コンピューターの簡単操作］ダイアログではなく、「utilman.exe」としてコピーした「cmd.exe（コマンドプロンプト）」が実行される。

ここで以下のコマンドを実行して、Administratorや既存のユーザーアカウントに対して新しいパスワードを設定する。この際、設定済みのパスワードの確認は行われないので、パスワードを忘れてしまったユーザーに対しても、新しいパスワードが設定できる。これで、新しいパスワードでサインインできるようになるので、コマンドプロンプトを閉じて再起動した後、設定したアカウントとパスワードでサインインするとよい。

net user **＜ユーザー名＞** **＜新しいパスワード＞**

**パスワードを再設定するためのコマンド**

なお、Microsoftアカウントでサインインしている場合は、以下のコマンドでAdministratorアカウントを有効化し、パスワードを設定すれよい。再起動後、サインイン画面の左下でAdministratorアカウントが選択可能になるので、これを選択し、設定したパスワードでサインインすればよい。

net user Administrator /active:yes

net user Administrator **＜パスワード＞**

**Administratorアカウントを有効にしてパスワードを設定するコマンド**

**Windows 11のパスワードを変更する（1）**

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword17.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword17.png)

▼

**Windows 11のパスワードを変更する（2）**これまでの操作により、［コンピューターの簡単操作］アイコンをクリックすると、このようにコマンドプロンプトが起動するようになる。ここで、上記のコマンドを入力して、既存のアカウントのパスワードを変更したり、Administratorアカウントを有効化してパスワードを設定したりする。パスワードは、Windows 11にサインイン後、［設定］アプリで変更すればいいので、短い適当なものを設定しておけばよい。

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword18.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword18.png)

▼

**Windows 11のパスワードを変更する（3）**Windows 11を再起動すると、有効化したAdministratorアカウントが選択できるようになる。［Administrator］を選択してサインインアカウントを切り替えて、有効化の際に設定したパスワードを入力すれば、Administratorアカウントでサインインできる。

[![](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword19.png)](https://image.itmedia.co.jp/ait/articles/2206/27/wi-win11forgotpassword19.png)

後は、必要なファイルをコピーしたり、アカウントの再設定を行ったりすればよい。

### 置き換えた「utilman.exe」を元に戻す

上記の操作で変更したパスワードでサインインできるのを確認したら、置き換えた「utilman.exe」を元に戻そう。再びUbuntuのインストールUSBメモリで起動して、置き換えた「utilman.exe」を削除、バックアップしておいた「@utilman.exe」のファイル名を変更して元に戻せばよい。

### パスワードの再設定やAdministratorアカウントの無効化をする

PCの復旧が完了したら、前述のnetコマンドで設定した簡単なパスワードを、長くて安全なパスワードに変更する。それには、［設定］アプリの［アカウント］－［サインインオプション］－「サインインする方法」欄－［パスワード］－［変更］ボタンとクリックすれば変更できる。

無効になっていたAdministratorアカウントを有効化した場合は、無効化しておこう。それには、[管理者権限でコマンドプロンプトを起動](https://atmarkit.itmedia.co.jp/ait/articles/1806/14/news017.html)してから以下のコマンドラインを実行すればよい。

net user Administrator /active:no

**Administratorアカウントを無効化するコマンド**

---

このようにパスワードが分からなくても、Windows 11にサインインしてローカルストレージに保存されているデータなどを取り出すことが可能だ。退社したスタッフや急病になってしまった人のPCから必要なデータを取り出す際などには有効だろう。もちろん、その際はPCの所有者（利用者）の同意を得ること。

また、このようにパスワードが分からなくてもサインインが可能になってしまうので、簡単に盗まれたり、忘れたりしてしまうようなノートPCなどは、BitLockerで暗号化しておくなど、セキュリティを高める工夫をした方がよいだろう（BitLockerについては、超入門BitLocker：「[BitLockerとは](https://atmarkit.itmedia.co.jp/ait/articles/1702/28/news040.html)」参照のこと）。