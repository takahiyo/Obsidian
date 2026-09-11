---
notion-id: 542adf0d7b164486857f4f03dfad14fa
URL: https://yne.network.yamaha.com/view/post/0/849012
更新されました: Invalid date
作成日時: Invalid date
---
[![](https://storage.googleapis.com/users-cuuf/env/production/brandId/88/977b7700-350e-11ef-8fc7-d5799d9dbcde.png)](https://storage.googleapis.com/users-cuuf/env/production/brandId/88/977b7700-350e-11ef-8fc7-d5799d9dbcde.png)

# ==テクニカルノーツ==

==投稿を作成==

[![](https://commmune.imgix.net/env/production/brandId/88/fdc0b3e0-b40a-11ec-9b88-ebc8a9c2a303.png?auto=format&fit=crop&ixlib=react-9.0.3&h=44&w=44)](https://commmune.imgix.net/env/production/brandId/88/fdc0b3e0-b40a-11ec-9b88-ebc8a9c2a303.png?auto=format&fit=crop&ixlib=react-9.0.3&h=44&w=44)

==[ヤマハテクニカルノーツ担当](https://yne.network.yamaha.com/view/mypage/167224)==

==@tech_notes2==

==2024年6月28日 11:17==

# ==LANマップ：他社製UTMが入った時の管理方法と表示==

==「ヤマハルーターとヤマハLAN機器の間にUTMを導入した場合にLANマップは使えるの？」という問合せもよくいただきます。==

==ヤマハのUTMアプライアンス"[UTX100](https://network.yamaha.com/products/firewalls/utx100/index)/[UTX200](https://network.yamaha.com/products/firewalls/utx200/index)"であればもちろん使用可能ですし、ヤマハLAN機器だけでなくUTX100/UTX200自身をLANマップに表示させることも可能です。==

==そのため、基本的にはUTX100/UTX200の導入をおすすめしておりますが、諸般の事情により、他社製UTMを使用されるケースも少なくありません。==

==他社製UTMを使用する場合は、==

==１．「他社UTMでL2MSフレームを透過して、ルーターのLANマップを利用する」==

==もしくは==

==２．「他社UTM配下にインテリL2スイッチまたはL3スイッチを設置して、スイッチのLANマップを利用する」==

==のいずれかの対処を行っていただくことで、LANマップを使用することができます。==

==※ どちらの場合も他社製UTMはLANマップで表示されません。==

==今回は １．「他社UTMでL2MSフレームを透過して、ルーターのLANマップを利用する」 の方法を紹介します。==

[![](https://commmune.imgix.net/env/production/brandId/88/977b7700-350e-11ef-8fc7-d5799d9dbcde.png?fromServer=1&auto=format&q=50&fit=max)](https://commmune.imgix.net/env/production/brandId/88/977b7700-350e-11ef-8fc7-d5799d9dbcde.png?fromServer=1&auto=format&q=50&fit=max)

==LANマップはL2MSという独自プロトコルで情報をやり取りしていますので、UTMではブロックされてしまうため、ルーターとスイッチの間に他社製UTMがある場合はUTMの設定変更が必要になります。==

==詳しくはこちらの技術資料をご確認ください。==

==[https://www.rtpro.yamaha.co.jp/RT/docs/swctl/index.html#L2MS_protocol](https://www.rtpro.yamaha.co.jp/RT/docs/swctl/index.html)==

==下記はFortigate社製UTMをブリッジモードで使用した場合の設定例です。==

==ーーーーー==

==１．Internal1 ⇔ WAN1 でL2フレームの通信を許可。==

==# config system interface==

==# edit internal1==

==# set l2forward enable==

==# end==

==# config system interface==

==# edit wan1==

==# set l2forward enable==

==# end==

==２．LANマップ経由でエージェント機器のGUIを開くため、ルーターからエージェント機器宛のHTTP通信を許可。==

==※FortiOS v6.0.6 build6414 (GA)で確認==

==ーーーーー== 

==上記の設定をすることで、ルーターとスイッチの間に他社製UTMがある場合でも、ルーターから配下のスイッチが見えるようになります。==

[![](https://commmune.imgix.net/env/production/brandId/88/7cfc7880-34f4-11ef-8fc7-d5799d9dbcde.png?fromServer=1&auto=format&q=50&fit=max)](https://commmune.imgix.net/env/production/brandId/88/7cfc7880-34f4-11ef-8fc7-d5799d9dbcde.png?fromServer=1&auto=format&q=50&fit=max)

==UTMはLANマップ上では表示されませんが、ルーターGUIから配下のスイッチを表示/管理することが可能になります。==

==このように、他社製UTMを使用している環境であっても、LANマップで使用する通信を透過させることでLANマップをご活用いただけます。==

==とはいえ、ヤマハのUTMアプライアンス"UTX100/UTX200"をご使用いただければ、通信を透過する設定も不要で、以下の画像のようにLANマップ上にUTMを表示させることも可能です。==

==UTM導入の際は、LANマップとの組み合わせに便利なヤマハUTMアプライアンス"UTX100/UTX200"をぜひご検討ください！==

[![](https://commmune.imgix.net/env/production/brandId/88/70b2b800-34f4-11ef-8fc7-d5799d9dbcde.png?fromServer=1&auto=format&q=50&fit=max)](https://commmune.imgix.net/env/production/brandId/88/70b2b800-34f4-11ef-8fc7-d5799d9dbcde.png?fromServer=1&auto=format&q=50&fit=max)

==@テクニカルノーツ==

==(編集済み)==

==ソフトウェア／サービス==