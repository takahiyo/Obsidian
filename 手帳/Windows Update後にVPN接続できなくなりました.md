---
notion-id: 6b3fdc4852724d7f88549eb11d20a464
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - 仕事
  - 記事
---
## **よくあるお問い合わせ**

**質問**

Windows Update後にVPN接続できなくなりました(Windows10)

**お問い合わせ分類**

マニュアル・設定

**対象のサービス**

マイIPセカイVPNグループ専用VPN

## **答え**

2022年1月22日に配信されたWindows Update（KB5009543またはKB5009566）後に、L2TP接続ができなくなった場合は、[こちら](https://faq.interlink.or.jp/faq2/View/wcDisplayContent.aspx?id=879)をご覧ください。

---

Windows10をご利用でWindows Update後にVPN接続ができなくなった場合は、以下の手順で対処してください。

**1**.画面左下のWindowsマークをクリックし、歯車マークをクリックします。

[![](https://faq.interlink.or.jp/faq2/FileStore/images/787/01.jpg)](https://faq.interlink.or.jp/faq2/FileStore/images/787/01.jpg)

**2**.「Windowsの設定」より「ネットワークとインターネット」をクリックします。

[![](https://faq.interlink.or.jp/faq2/FileStore/images/787/02.jpg)](https://faq.interlink.or.jp/faq2/FileStore/images/787/02.jpg)

**3**.「アダプターのオプションを変更する」をクリックします。

[![](https://faq.interlink.or.jp/faq2/FileStore/images/787/03.jpg)](https://faq.interlink.or.jp/faq2/FileStore/images/787/03.jpg)

**4**.アダプター一覧画面が表示されますので、既存のVPN接続設定を全て削除します。

[![](https://faq.interlink.or.jp/faq2/FileStore/images/787/04.jpg)](https://faq.interlink.or.jp/faq2/FileStore/images/787/04.jpg)

**5**.画面左下のWindowsマークを右クリックして、「デバイスマネージャー」をクリックします。

[![](https://faq.interlink.or.jp/faq2/FileStore/images/787/05.jpg)](https://faq.interlink.or.jp/faq2/FileStore/images/787/05.jpg)

**6**.ネットワークアダプターを展開して、赤枠のアダプターを全て右クリックして削除します。

[![](https://faq.interlink.or.jp/faq2/FileStore/images/787/06.jpg)](https://faq.interlink.or.jp/faq2/FileStore/images/787/06.jpg)

**7**.Windows10を再起動します。

**8**.ご契約サービスの設定マニュアルをご覧いただき、VPN設定を新規に行います。

[＞＞セカイVPNの設定マニュアル](https://faq.interlink.or.jp/faq2/View/wcDisplayContent.aspx?id=1077)

[＞＞マイIPの設定マニュアル](https://faq.interlink.or.jp/faq2/View/wcDisplayContent.aspx?id=663)

**9**.VPN設定後、デバイスマネージャーの操作メニューより「ハードウェア変更のスキャン」をクリックします。

[![](https://faq.interlink.or.jp/faq2/FileStore/images/787/07.jpg)](https://faq.interlink.or.jp/faq2/FileStore/images/787/07.jpg)

**10**.スキャン完了後、VPN接続を開始してください。

以上で完了です。