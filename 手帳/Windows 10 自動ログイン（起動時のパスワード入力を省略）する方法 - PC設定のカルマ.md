---
notion-id: d36d7838d0524fcc882a7da92b68962d
URL: https://pc-karuma.net/windows10-disable-password-login/
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - 知識
---
**Windows 10 自動ログイン（起動時のパスワード入力を省略）する方法**

[![](https://pc-karuma.net/wp-content/uploads/2021/05/windows-10-user-auto-login.png)](https://pc-karuma.net/wp-content/uploads/2021/05/windows-10-user-auto-login.png)

**Windows 10 で、起動時のパスワード入力を省略し、自動ログイン（サインイン）する方法を紹介します。**  
**パソコンを起動するたびにパスワードを入力するのはめんどくさい！ という方はパスワードの入力を省略し、自動ログインを設定しましょう。**  
**ここでは「netplwiz」というコマンドを使って、パスワードの入力を省略する方法をみていきます。また自動ログインできない場合の対処方法も合わせてみていきます。**  
**目次**  
**•** [**自動ログイン**](https://pc-karuma.net/windows10-disable-password-login/#%E8%87%AA%E5%8B%95%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3)  
**◦** [**検索ボックスに**](https://pc-karuma.net/windows10-disable-password-login/#%E6%A4%9C%E7%B4%A2%E3%83%9C%E3%83%83%E3%82%AF%E3%82%B9%E3%81%AB)  
**◦** [**「netplwiz」を入力**](https://pc-karuma.net/windows10-disable-password-login/#%E3%80%8Cnetplwiz%E3%80%8D%E3%82%92%E5%85%A5%E5%8A%9B)  
**◦** [**「netplwiz」の起動**](https://pc-karuma.net/windows10-disable-password-login/#%E3%80%8Cnetplwiz%E3%80%8D%E3%81%AE%E8%B5%B7%E5%8B%95)  
**◦** [**ユーザーアカウントの設定**](https://pc-karuma.net/windows10-disable-password-login/#%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%AE%E8%A8%AD%E5%AE%9A)  
**◦** [**自動ログインの設定**](https://pc-karuma.net/windows10-disable-password-login/#%E8%87%AA%E5%8B%95%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E3%81%AE%E8%A8%AD%E5%AE%9A)  
**◦** [**自動ログインできるかどうかを確認**](https://pc-karuma.net/windows10-disable-password-login/#%E8%87%AA%E5%8B%95%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E3%81%A7%E3%81%8D%E3%82%8B%E3%81%8B%E3%81%A9%E3%81%86%E3%81%8B%E3%82%92%E7%A2%BA%E8%AA%8D)  
**•** [**自動ログインできない場合の対処**](https://pc-karuma.net/windows10-disable-password-login/#%E8%87%AA%E5%8B%95%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84%E5%A0%B4%E5%90%88%E3%81%AE%E5%AF%BE%E5%87%A6)  
**◦** [**レジストリのバックアップ**](https://pc-karuma.net/windows10-disable-password-login/#%E3%83%AC%E3%82%B8%E3%82%B9%E3%83%88%E3%83%AA%E3%81%AE%E3%83%90%E3%83%83%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97)  
**◦** [**ファイル名を指定して実行**](https://pc-karuma.net/windows10-disable-password-login/#%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%90%8D%E3%82%92%E6%8C%87%E5%AE%9A%E3%81%97%E3%81%A6%E5%AE%9F%E8%A1%8C)  
**◦** [**レジストリエディターの起動**](https://pc-karuma.net/windows10-disable-password-login/#%E3%83%AC%E3%82%B8%E3%82%B9%E3%83%88%E3%83%AA%E3%82%A8%E3%83%87%E3%82%A3%E3%82%BF%E3%83%BC%E3%81%AE%E8%B5%B7%E5%8B%95)  
**◦** [**レジストリの修正**](https://pc-karuma.net/windows10-disable-password-login/#%E3%83%AC%E3%82%B8%E3%82%B9%E3%83%88%E3%83%AA%E3%81%AE%E4%BF%AE%E6%AD%A3)  
**◦** [**netplwizの起動**](https://pc-karuma.net/windows10-disable-password-login/#netplwiz%E3%81%AE%E8%B5%B7%E5%8B%95)  
**•** [**自動ログインの解除**](https://pc-karuma.net/windows10-disable-password-login/#%E8%87%AA%E5%8B%95%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E3%81%AE%E8%A7%A3%E9%99%A4)  
**•** [**パスワードなしユーザーの作成**](https://pc-karuma.net/windows10-disable-password-login/#%E3%83%91%E3%82%B9%E3%83%AF%E3%83%BC%E3%83%89%E3%81%AA%E3%81%97%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E3%81%AE%E4%BD%9C%E6%88%90)  
**•** [**Windows Hello（顔認証）の設定**](https://pc-karuma.net/windows10-disable-password-login/#Windows_Hello%EF%BC%88%E9%A1%94%E8%AA%8D%E8%A8%BC%EF%BC%89%E3%81%AE%E8%A8%AD%E5%AE%9A)  
**•** [**パスワードの変更**](https://pc-karuma.net/windows10-disable-password-login/#%E3%83%91%E3%82%B9%E3%83%AF%E3%83%BC%E3%83%89%E3%81%AE%E5%A4%89%E6%9B%B4)  
**•** [**Windows10の使い方や設定**](https://pc-karuma.net/windows10-disable-password-login/#Windows10%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9%E3%82%84%E8%A8%AD%E5%AE%9A)  
**自動ログイン**  
**それでは実際にパスワード入力を省略してみましょう。**  
**検索ボックスに**  
**デスクトップの左下にあるフォーム（検索ボックス）に**  
**「netplwiz」を入力**  
**「netplwiz」を入力しましょう。**  
**「netplwiz」の起動**  
**「netplwiz」を起動します。**  
**ユーザーアカウントの設定**  
**「ユーザーアカウント」の設定です。「ユーザーがこのコンピューターを使うには、ユーザー名とパスワードの入力が必要」からチェックをはずしましょう。**  
**チェックする項目がない場合は「**[**自動ログインできない場合**](https://pc-karuma.net/windows10-disable-password-login/#cannotset)**」をご覧ください。**  
**チェックがはずれていること確認し、「OK」をクリックします。**  
**自動ログインの設定**  
**すると、「自動サインイン」ウィンドウが表示されます。「ユーザー名」「パスワード」を入力し「OK」をクリックしましょう。**  
**自動サインイン**  
**ユーザーがサインインするときに、ユーザー名とパスワードを入力する必要がないようにコンピューターをセットアップできます。自動でサインインするユーザーを指定してください。**  
**自動ログインできるかどうかを確認**  
**これでパスワード入力の省略（自動サインイン）の設定は完了です。実際に自動サインインできるかどうかを確認してみましょう。**  
**スタートボタンをクリックし**  
**スタートメニューから Windows を再起動しましょう。**  
**再起動後、このようにパスワードの入力画面はスキップされ**  
**このようにデスクトップが表示されます。これで自動サインインの設定は完了です。**  
**自動ログインできない場合の対処**  
**「netplwizコマンド」を実行した場合に**  
**ここに「ユーザーがこのコンピューターを使うには、ユーザー名とパスワードの入力が必要」という設定項目ない場合があります。**  
[**Windows 10 ver.2004以降をクリーンインストール**](https://pc-karuma.net/windows-10-clean-install/)**した場合、上記のように自動サインインの設定ができない場合があります。**  
  
**上記の場合に自動サインインの設定ができるようにする方法をみていきます。**  
**レジストリのバックアップ**  
**※ 設定するにはレジストリを編集する必要があるので、**[**Windows 10 レジストリをエクスポート（バックアップ）する方法**](https://pc-karuma.net/windows-10-export-registry-file/)**を参考に念のためにバックアップをとっておきましょう。**  
**それでは実際に設定してみましょう。**  
**スタートボタンにマウスカーソルをもっていき、右クリックすると**  
**ファイル名を指定して実行**  
**このようにメニューが表示されるので「ファイル名を指定して実行」をクリックします。**  
**すると、「**[**ファイル名を指定して実行**](https://pc-karuma.net/windows-10-open-run-dialog/)**」ウインドウが表示されます。**  
**レジストリエディターの起動**  
**ファイル名を指定して実行に「regedit」と入力し、「OK」をクリックします。**  
**ユーザーアカウント制御です。「はい」をクリックしましょう。**  
**レジストリエディターです。**  
**レジストリの修正**  
**「HKEY_LOCAL_MACHINE」から以下のようにたどります……ちょっと長いです。**  
**HKEY_LOCAL_MACHINE**  
**→ SOFTWARE**  
**→ Microsoft**  
**→ Windows NT**  
**→ CurrentVersion**  
**→ PasswordLess**  
**→ Device**  
**「DevicePasswordLessBuildVersion」を選択し、右クリックすると**  
**このようにメニューが表示されるので、「修正」をクリックします。**  
**値のデータが「2」になっているので**  
**「0」に変更し、「OK」をクリックします。**  
**これでOKです。**  
**スタートメニューから**  
**Windows を再起動しましょう。**  
**再起動後、タスクバーの「フォーム」に**  
**netplwizの起動**  
**「netplwiz」と入力し**  
**「netplwiz」を起動しましょう。**  
**すると、このように自動ログインの設定ができるようになります。これで準備完了です。**  
**「**[**自動ログイン**](https://pc-karuma.net/windows10-disable-password-login/#netpl)**」から続きを設定しましょう。**  
**自動ログインの解除**  
**自動ログインが不要になった場合は解除しておきましょう。**  
**①タスクバーのフォーム（検索ボックス）に「netplwiz」と入力し、②「netplwiz」を起動します。**  
**①「ユーザーがこのコンピューターを使うには、ユーザー名とパスワードの入力が必要に」にチェックを入れ、②「OK」をクリックします。**  
**これで自動ログインは解除されます。**

[![](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-disable-password-login-c01-640x480.png)](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-disable-password-login-c01-640x480.png)

[![](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-disable-password-login-c02-640x401.png)](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-disable-password-login-c02-640x401.png)

[![](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-disable-password-login-c07-640x401.png)](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-disable-password-login-c07-640x401.png)

[![](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-disable-password-login-c08-640x501.png)](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-disable-password-login-c08-640x501.png)

[![](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-disable-password-login-c09-640x480.png)](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-disable-password-login-c09-640x480.png)

[![](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-settings-netplwiz-08-640x440.png)](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-settings-netplwiz-08-640x440.png)

[![](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-settings-netplwiz-09-640x440.png)](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-settings-netplwiz-09-640x440.png)

[![](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-settings-netplwiz-10-320x188.png)](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-settings-netplwiz-10-320x188.png)

[![](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-settings-netplwiz-19-1-480x534.png)](https://pc-karuma.net/wp-content/uploads/2020/08/windows10-settings-netplwiz-19-1-480x534.png)

[![](https://pc-karuma.net/wp-content/uploads/2021/05/windows10-disable-password-login-01-620x669.jpg)](https://pc-karuma.net/wp-content/uploads/2021/05/windows10-disable-password-login-01-620x669.jpg)

[![](https://pc-karuma.net/wp-content/uploads/2021/05/windows10-disable-password-login-02-480x537.jpg)](https://pc-karuma.net/wp-content/uploads/2021/05/windows10-disable-password-login-02-480x537.jpg)

![[windows-10-user-auto-login.png]]

Windows 10 で、起動時のパスワード入力を省略し、自動ログイン（サインイン）する方法を紹介します。

![[windows10-disable-password-login-c01-2048x1537.png]]

パソコンを起動するたびにパスワードを入力するのはめんどくさい！ という方はパスワードの入力を省略し、自動ログインを設定しましょう。

ここでは「netplwiz」というコマンドを使って、パスワードの入力を省略する方法をみていきます。また自動ログインできない場合の対処方法も合わせてみていきます。

## 自動ログイン

それでは実際にパスワード入力を省略してみましょう。

### 検索ボックスに

デスクトップの左下にあるフォーム（検索ボックス）に

### 「netplwiz」を入力

「netplwiz」を入力しましょう。

### 「netplwiz」の起動

「netplwiz」を起動します。

### ユーザーアカウントの設定

「ユーザーアカウント」の設定です。「ユーザーがこのコンピューターを使うには、ユーザー名とパスワードの入力が必要」からチェックをはずしましょう。

チェックする項目がない場合は「[自動ログインできない場合](https://pc-karuma.net/windows10-disable-password-login/#cannotset)」をご覧ください。

チェックがはずれていること確認し、「OK」をクリックします。

### 自動ログインの設定

すると、「自動サインイン」ウィンドウが表示されます。「ユーザー名」「パスワード」を入力し「OK」をクリックしましょう。

自動サインイン

ユーザーがサインインするときに、ユーザー名とパスワードを入力する必要がないようにコンピューターをセットアップできます。自動でサインインするユーザーを指定してください。

### 自動ログインできるかどうかを確認

これでパスワード入力の省略（自動サインイン）の設定は完了です。実際に自動サインインできるかどうかを確認してみましょう。

## 自動ログインできない場合の対処

「netplwizコマンド」を実行した場合に

ここに「ユーザーがこのコンピューターを使うには、ユーザー名とパスワードの入力が必要」という設定項目ない場合があります。

[Windows 10 ver.2004以降をクリーンインストール](https://pc-karuma.net/windows-10-clean-install/)した場合、上記のように自動サインインの設定ができない場合があります。

上記の場合に自動サインインの設定ができるようにする方法をみていきます。

### レジストリのバックアップ

※ 設定するにはレジストリを編集する必要があるので、[Windows 10 レジストリをエクスポート（バックアップ）する方法](https://pc-karuma.net/windows-10-export-registry-file/)を参考に念のためにバックアップをとっておきましょう。

それでは実際に設定してみましょう。

スタートボタンにマウスカーソルをもっていき、**右クリック**すると

### ファイル名を指定して実行

すると、「[ファイル名を指定して実行](https://pc-karuma.net/windows-10-open-run-dialog/)」ウインドウが表示されます。

### レジストリエディターの起動

### レジストリの修正

「HKEY_LOCAL_MACHINE」から以下のようにたどります……ちょっと長いです。

HKEY_LOCAL_MACHINE

→ SOFTWARE

→ Microsoft

→ Windows NT

→ CurrentVersion

→ PasswordLess

→ Device

再起動後、タスクバーの「フォーム」に

### netplwizの起動

すると、このように自動ログインの設定ができるようになります。これで準備完了です。

「[自動ログイン](https://pc-karuma.net/windows10-disable-password-login/#netpl)」から続きを設定しましょう。

## 自動ログインの解除

自動ログインが不要になった場合は解除しておきましょう。

①タスクバーのフォーム（検索ボックス）に「netplwiz」と入力し、②「netplwiz」を起動します。

①「ユーザーがこのコンピューターを使うには、ユーザー名とパスワードの入力が必要に」にチェックを入れ、②「OK」をクリックします。

これで自動ログインは解除されます。

## パスワードなしユーザーの作成

※ パスワードなしのユーザーを作成し、ログイン画面をスキップすることもできます。合わせてご覧ください。

[Windows 10 パスワードなしのユーザーアカウントを作成する方法](https://pc-karuma.net/windows10-create-passwordless-user-account/)

## Windows Hello（顔認証）の設定

※ Windows Hello（顔認証）を利用して、ログインする方法はこちらをご覧ください。

[Windows 10 – Windows Hello（顔認証）を設定・登録する](https://pc-karuma.net/windows-10-enable-windows-hello/)

## パスワードの変更

Windows10のログイン・パスワードを変更する場合はこちらをご覧ください。

- [Windows 10 – ローカルアカウントのパスワードを変更する](https://pc-karuma.net/windows-10-change-local-account-password/)
- [Windows 10 – Microsoftアカウントのパスワードを変更する](https://pc-karuma.net/windows-10-change-microsoft-account-password/)

## Windows10の使い方や設定

※ Windows10 の使い方や設定はこちらをご覧ください。

[Windows 10 の設定と使い方まとめ](https://pc-karuma.net/windows10/)