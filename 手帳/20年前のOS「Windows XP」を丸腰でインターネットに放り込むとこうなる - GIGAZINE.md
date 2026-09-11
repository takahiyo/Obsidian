---
notion-id: ca7c0dfb44e44de89833501349d62502
URL: https://gigazine.net/news/20240523-windows-xp-connect-internet-malware/
更新されました: Invalid date
作成日時: Invalid date
---
[![](https://i.gzn.jp/img/2024/05/23/windows-xp-connect-internet-malware/00_m.png)](https://i.gzn.jp/img/2024/05/23/windows-xp-connect-internet-malware/00_m.png)

2001年にリリースされたWindows XPは、2014年4月に延長サポートが打ち切られてから記事作成時点で10年が経過していますが、要求スペックの低さや安定性などから根強く支持されており、2022年に公開されたレポートではWindows 11に匹敵するシェア率だったと[**報告**](https://gigazine.net/news/20211026-windows-xp-20th-anniversary/)されています。そんなWindows XPをファイアウォールを切った状態でインターネットに接続した動画をYouTuberのエリック・パーカー氏が公開したところ、投稿から約10日で45万回も再生されました。

[**What happens if you connect Windows XP to the Internet in 2024? - YouTube**](https://www.youtube.com/watch?v=6uSVVCmOH5w)

[![](https://i.gzn.jp/img/2024/05/23/windows-xp-connect-internet-malware/a00001_m.png)](https://i.gzn.jp/img/2024/05/23/windows-xp-connect-internet-malware/a00001_m.png)

今回使用するWindows XP環境は、仮想化プラットフォームの[**Proxmox VE**](https://www.proxmox.com/en/)のサーバー上に構築された仮想マシンを[**VNC**](https://e-words.jp/w/VNC.html)でリモート操作するという形で実行されています。

[![](https://i.gzn.jp/img/2024/05/23/windows-xp-connect-internet-malware/a00002_m.png)](https://i.gzn.jp/img/2024/05/23/windows-xp-connect-internet-malware/a00002_m.png)

わずか数クリックでセットアップが完了しました。「昔のセットアップ画面は今よりずっとシンプルでいいですね。これが今では、いろいろなボタンをクリックしないとあなたのデータがMicrosoftのものになると脅してきます」とパーカー氏。

[![](https://i.gzn.jp/img/2024/05/23/windows-xp-connect-internet-malware/a00003_m.png)](https://i.gzn.jp/img/2024/05/23/windows-xp-connect-internet-malware/a00003_m.png)

ファイアウォールとセキュリティを解除してインターネット接続の設定を済ませます。もちろん、アンチウイルスソフトも入っていません。

[![](https://i.gzn.jp/img/2024/05/23/windows-xp-connect-internet-malware/a00004_m.png)](https://i.gzn.jp/img/2024/05/23/windows-xp-connect-internet-malware/a00004_m.png)

ブラウザのInternet Explorerを開いて放置してからわずか数分で、PCが感染した最初の兆候が現れます。

タスクマネージャーを開くと、「conhoz.exe」というという見慣れない実行ファイルがありますが、これは有害なウイルスとのこと。

さらにその直後、アカウントを確認すると「admina」という管理者権限のアカウントを作成していました。パーカー氏は、このアカウントがFTPファイルサーバーをホストしていることから、ハッカーがボットネットを構築しているかスパムメールでも送ろうとしているのではないかと推測しています。

先ほどのconhoz.exeの通信履歴をたどってみると、1994年にロシアで登録されてから2024年4月まで使われ続けているドメインが引っかかりました。つまり、2024年になってもまだWindows XPを標的にしたマルウェアの運用が続けられているということです。

ウイルスをスキャンするMalwarebytesを使ってみると、8つのマルウェアが検出されました。マシンにはもっと多くのウイルスが存在していましたが、無料版のMalwarebytesではこれが限界でした。

Malwarebytesでマルウェアを駆除してからWindows XPを再起動したところ、conhoz.exeはまだデバイス上に存在していましたが、自動起動はしなかったので、首尾よく無効化に成功した……かのように思われました。

しかし、再びMalwarebytesでスキャンをしつつファイアウォールを起動させようとした瞬間、Malwarebytesが自動的に閉じられてしまい、実行ファイルも復活しました。無料版とはいえ、アンチウイルスソフトがマルウェアによって強制終了されてしまったことから、パーカー氏は「これはマルウェアに一本取られたと言っていいでしょう」と述べました。

パーカー氏はその後Windows 2000でも同じ事をやってみました。

[**What happens if you connect Windows 2000 to the Internet in 2024? - YouTube**](https://www.youtube.com/watch?v=Mmp-P24QJjQ)

怪しい実行ファイルをオンラインスキャンにかけると、無数のマルウェアがヒットしました。

パーカー氏は、Windows 7で同様にファイアウォールを切って数時間インターネットにつなぎっぱなしにしてみましたが、このような事態には陥らなかったとのこと。

一連の実験結果からパーカー氏は「Windows XPのようなシステムがマルウェアに非常に感染しやすく、いかに脆弱(ぜいじゃく)かがわかりました。もしこういう状態になったらインターネット接続を切断してシステムを再インストールすることを強くお勧めします」と述べました。

**◆フォーラム開設中**

本記事に関連するフォーラムを[**GIGAZINE公式Discordサーバー**](https://gigazine.net/news/20221117-gigazine-discord/)に設置しました。誰でも自由に書き込めるので、どしどしコメントしてください！Discordアカウントを持っていない場合は、[**アカウント作成手順解説記事**](https://gigazine.net/news/20221117-gigazine-discord/)を参考にアカウントを作成してみてください！

- **Discord | "古めのOSでウイルスに感染したことある？" | GIGAZINE(ギガジン)**

[**https://discord.com/channels/1037961069903216680/1243132971632824381**](https://discord.com/channels/1037961069903216680/1243132971632824381)