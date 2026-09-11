---
notion-id: 1d137ce628718180bf7bde3021db22b7
URL: https://getnavi.jp/digital/1031482/
更新されました: Invalid date
作成日時: Invalid date
---
マイクロソフトは最近、Windows 11のセットアップ時にインターネット接続と「Microsoftアカウント」（以下、MSアカウント）へのサインインを回避できる抜け道をふさぎました。これまで利用可能だった[「bypassnro」コマンド](https://www.windowscentral.com/how-set-windows-11-without-microsoft-account)が削除されたという流れです。

[![](https://getnavi.jp/wps/wp-content/uploads/2025/04/AdobeStock_761499113_Editorial_Use_Only.jpeg.webp)](https://getnavi.jp/wps/wp-content/uploads/2025/04/AdobeStock_761499113_Editorial_Use_Only.jpeg.webp)

[![](https://getnavi.jp/wps/wp-content/uploads/2025/04/AdobeStock_761499113_Editorial_Use_Only.jpeg)](https://getnavi.jp/wps/wp-content/uploads/2025/04/AdobeStock_761499113_Editorial_Use_Only.jpeg)

↑rvlsoft/Adobe Stockより。現在のWindows 11は基本的にネット環境がない状態ではセットアップできず、状況によっては非常に不便なのですが……。

しかし、新たな回避方法が発見されたと報じられています。

X（旧Twitter）のユーザー @witherornot1337 氏が、その具体的な手順を紹介しています。

1. Windows 11のセットアップ中に、Shift + F10キーを押してコマンドプロンプトを起動します
2. コマンドプロンプトに start ms-cxh:localonly と入力し、Enterキーを押します
3. ローカルアカウントの作成画面が表示されるので、ユーザー名とパスワードを設定します
4. 設定が完了すると、プライバシー設定の画面に進みます

MSアカウントへのサインインが好まれない理由はいくつかあります。ひとつは、認証にインターネット接続が必要なため、出張先やオフライン環境ではセットアップができないことです。また、別のPCと同じMSアカウントを使うと、設定やカスタマイズが勝手に引き継がれてしまう場合があり、それを不快に感じるユーザーもいます。さらに、MSアカウントのパスワードを忘れてしまうと、PCにログインできなくなるリスクもあります。

なお、マイクロソフトはbypassnroコマンドの削除について、「セキュリティとユーザー体験を強化するため」と公式に[説明しています](https://techcommunity.microsoft.com/discussions/windowsinsiderprogram/bypassnro-removal/4398756)。そのため、今後のアップデートで今回の回避方法も使えなくなる可能性がありますが、現時点では問題なく機能しているようです。

Source: [@witherornot1337(X)](https://x.com/witherornot1337/status/1906050664741937328)

via:[Wccftech](https://wccftech.com/you-can-still-setup-windows-11-without-logging-into-a-microsoft-account/)