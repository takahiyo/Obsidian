---
notion-id: 15311ca292064922ae574cb8fc6bd4e7
URL: https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - セキュリティ
  - 仕事
  - 記事
---
# [**フレッツIPv6はファイアウォール無効?**](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)

[小生の家は、フレッツ光とプロバイダのフレッツv6オプションでIPv6(IPoE)を使っている。](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)[  
](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)[  
ファイアウォールはホームゲートウェイ(HGW)の標準設定のまま、特にいじっていなかった。](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)[  
](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)[  
ある日ネットを見ていたら、これではマズいということらしいので、慌てて設定変更したので、その備忘としてこの記事を投稿した。](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)

## [**HGWのIPv6パケットフィルタ**](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)

[HGWの設定画面では以下のような記載がある。](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)[IPv6ファイアウォール機能が「有効」でかつ、セキュリティレベルが「標準」の場合、NTT東日本・NTT西日本のフレッツ光ネクスト網内で折り返す通信（NTT東日本・NTT西日本との契約により可能となるもの）は許容し、その他のIPv6通信を使用したインターネット側からの通信を拒否します。](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)[  
](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)[  
※セキュリティレベルが「高度」の場合は、NTT東日本・NTT西日本のフレッツ光ネクスト網内で折り返す通信（NTT東日本・NTT西日本との契約により可能となるもの）を拒否します。](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)

[**フレッツ光ネクスト網内で折り返す通信**](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)[を許容するということは、厳密な説明は割愛するが、IPv6のインターネットへ接続はプロバイダのゲートウェイを通らなければならないが、下図のように、NGN網内同士は通信ができるということである。(下図)](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)

[![](https://qiita-user-contents.imgix.net/https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/577966/f68322ab-9eeb-cacf-c467-b46d8809b63a.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=ec8411491b889544792f4b6205efd48f)](https://qiita-user-contents.imgix.net/https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/577966/f68322ab-9eeb-cacf-c467-b46d8809b63a.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=ec8411491b889544792f4b6205efd48f)

出典: [http://www.geekpage.jp/blog/?id=2013/1/11/1](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)

## [**HGWのセキュリティレベルの設定**](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)

[ここで問題となるが上述の設定画面の「セキュリティレベル」ということになるのだが、「標準」というのは、](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)[**HGWがNGN網内のIPv6通信を全て通過させる**](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)[ということなのである。これは非常にマズく、NASやファイル共有設定を有効にすると誰からでも見えてしまうという状況なのである。](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)[  
当然ここは、設定を「](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)[**高度**](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)[」に変えよう。](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)[  
変更してもIPv6通信ができなくなるわけではない。](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)

[![](https://qiita-user-contents.imgix.net/https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/577966/2c0ac8de-ba1d-1200-f538-e216d6233c34.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=385db2dc98ea46cd8aed54aff5b34a07)](https://qiita-user-contents.imgix.net/https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/577966/2c0ac8de-ba1d-1200-f538-e216d6233c34.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=385db2dc98ea46cd8aed54aff5b34a07)

図：HGWのIPv6(IPoE)のセキュリティレベル設定は「高度」に！

なお、「標準」でもNGN網の外からのアクセスは遮断されるようだ(HGWまではアクセスできるようだが、パケットフィルタで遮断される）。

NGN網の中の人たちはよほど信頼できるということなのだろうか(笑)。

IPv4だと、ルータがプライベートアドレス(192.168.x.xなど)を割り振るため、わざわざ設定しない限りはLANの外にいきなりPCがさらされることはないのだが、IPv6ではHGWの設定一つで丸裸になってしまうのである。

## [**まとめ**](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)

[フレッツのHGWのセキュリティレベルはデフォルトの「標準」ではかなり危険だ。](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)[  
特に理由がある場合を除き、少なくとも「高度」に変えておこう。](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)[  
それでも設定一つで丸裸になることには変わりが無いので、もう少しセキュリティのレベルを上げることを](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)[その2](https://qiita.com/maron2000/items/c857d01e8a4d2e62c9d5undefined)で、紹介する。

  

![[a8586d6d87b8f234a576262a66b04135]]

[**@maron2000**](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)

投稿日 2020年02月02日

# **フレッツ IPv6(IPoE)のセキュリティに関する考察　その2**

[IPv6,フレッツ,ファイアウォール,IPoE,NGN](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)

# [**はじめに**](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)

[フレッツ IPv6(IPoE)のセキュリティに関する考察　その1](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)では、とりあえずホームゲートウェイ(HGW)の**IPv6のセキュリティレベルを「高度」**にするということを紹介した。

一方で、設定を試しに、もしくは誤って「標準」にした場合にはいきなり丸裸に逆戻りになってしまう。

そこで、いわゆるバカよけ(フールプルーフ)のため、パケットフィルタも設定しておくことにした。

## [**HGWのIPv6(IPoE)パケットフィルタの設定**](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)

[HGWのトップページ＞詳細設定＞セキュリティ設定＞IPv6パケットフィルタ設定(IPoE)から設定する。  
  
とりあえず設定した順番で優先順位も設定しているが、本当は精査をした方が良いかもしれない。](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)

### [**1.全ての外部からのアクセスは遮断**](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)

[通信方向: IPoE→LAN  
プロトコル:TCP,UDP  
ポート：any(全ポート)  
フィルタ：拒否](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)

[![](https://qiita-user-contents.imgix.net/https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/577966/16da4f32-46aa-5cb7-0988-c1e70be5be29.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=5f1559d1ed4945ef09d394f5a1812416)](https://qiita-user-contents.imgix.net/https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/577966/16da4f32-46aa-5cb7-0988-c1e70be5be29.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=5f1559d1ed4945ef09d394f5a1812416)

### [**2.ファイル共有関係(1.とも重複するが、念のため)**](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)

[通信方向：両方向  
プロトコル:TCP, UDP  
ポート: 137-139, 445  
フィルタ:拒否](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)

[![](https://qiita-user-contents.imgix.net/https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/577966/f42e867e-aef7-8585-97a5-81a3a32a31bf.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=669e1e0bcbac0fc30ca83b2c341c1afc)](https://qiita-user-contents.imgix.net/https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/577966/f42e867e-aef7-8585-97a5-81a3a32a31bf.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=669e1e0bcbac0fc30ca83b2c341c1afc)

※念のため、LAN→IPoE方向で137-139, 445の送信も遮断

### [**3.IPv6近隣要請**](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)

[プロトコル: ICMPv6  
通信方向：IPoE→LAN タイプ135  
　　　　　　　LAN→IPoE タイプ136  
フィルタ：拒否](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)

[![](https://qiita-user-contents.imgix.net/https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/577966/72de5a5e-32c8-925e-294a-74a6d90ad88b.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=2b66ef3dcb1487ed021a96c691dbce6e)](https://qiita-user-contents.imgix.net/https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/577966/72de5a5e-32c8-925e-294a-74a6d90ad88b.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=2b66ef3dcb1487ed021a96c691dbce6e)

### [**4.ノード情報問い合わせ等**](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)

[RFC4890 4.3.5 で遮断が推奨されている  
プロトコル: ICMPv6  
タイプ: 138-140  
通信方向：下図の通りだが、両方向でも良いかもしれない。  
フィルタ：拒否](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)

[![](https://qiita-user-contents.imgix.net/https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/577966/2bbd0b65-86a2-85b6-1108-65ab6637e897.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=6832b7d9a78a7dbd6aa6eda7f433060a)](https://qiita-user-contents.imgix.net/https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/577966/2bbd0b65-86a2-85b6-1108-65ab6637e897.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=6832b7d9a78a7dbd6aa6eda7f433060a)

## [**まとめ**](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)

[実験的に設定を変えてしまっても、いきなり丸裸にならないようにパケットフィルタを設定しておくことをお薦めする。  
  
ただし、ファイアウォール機能自体をを無効にするという設定には無意味なので、結局は気休めかもしれない。](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)

[](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)

[**ユーザー登録して、Qiitaをもっと便利に使ってみませんか。**](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)  
**1.** [**あなたにマッチした記事をお届けしますユーザーやタグをフォローすることで、あなたが興味を持つ技術分野の情報をまとめてキャッチアップできます便利な情報をあとで効率的に読み返せます気に入った記事を「ストック」することで、あとからすぐに検索できます**](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)[_****_](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)[**より詳しく**](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)[ユーザー登録ログイン](https://qiita.com/maron2000/items/f3765a517a4616bdc395undefined)