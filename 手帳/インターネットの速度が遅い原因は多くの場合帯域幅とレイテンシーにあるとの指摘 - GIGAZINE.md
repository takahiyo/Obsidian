---
notion-id: 11b37ce62871815fa3f5e46f85bf3649
URL: https://gigazine.net/news/20241010-internet-bandwidth/
更新されました: Invalid date
作成日時: Invalid date
---
[![](https://i.gzn.jp/img/2024/10/10/internet-bandwidth/00_m.jpg)](https://i.gzn.jp/img/2024/10/10/internet-bandwidth/00_m.jpg)

インターネットを快適に楽しむためには、適切なデバイスの購入のほかに、**[帯域幅](https://ja.wikipedia.org/wiki/%E5%B8%AF%E5%9F%9F%E5%B9%85)**や**[レイテンシー](https://ja.wikipedia.org/wiki/%E3%83%AC%E3%82%A4%E3%83%86%E3%83%B3%E3%82%B7)**が重要になります。「帯域幅」や「レイテンシー」について、学術雑誌「**[Communications of the ACM](https://cacm.acm.org/)**」が解説しています。

**You Don’t Know Jack about Bandwidth – Communications of the ACM**

**https://cacm.acm.org/practice/you-dont-know-jack-about-bandwidth/**

[![](https://i.gzn.jp/img/2024/10/10/internet-bandwidth/01_m.png)](https://i.gzn.jp/img/2024/10/10/internet-bandwidth/01_m.png)

Communications of the ACMは帯域幅とレイテンシーをインターネットというパイプに例えて説明しています。インターネット接続を介して一度に送信できるデータ量を指す帯域幅は「パイプの直径」であり、「パイプが太いほど、より多くのデータを一度に送信できる一方、パイプが狭いほどデータ送信に時間がかかり、インターネット速度が遅くなる」「特に、大きなファイルをダウンロードしたり、高解像度の動画をストリーミングしたりする場合に顕著になる」というわけです。

[![](https://i.gzn.jp/img/2024/10/10/internet-bandwidth/02_m.jpg)](https://i.gzn.jp/img/2024/10/10/internet-bandwidth/02_m.jpg)

また、データが送信元から宛先に到達するまでの時間を指すレイテンシーは「パイプの長さ」に相当し、「パイプが長いほどデータが宛先に到達するまでに時間がかかります。レイテンシーが高いと、ウェブページの読み込みやオンラインゲーム、ビデオ通話などが遅延し、スムーズに動作しなくなります」とCommunications of the ACMは説明しています。

Communications of the ACMによると、インターネット速度が遅い場合、多くのユーザーは帯域幅を増やすことを考えるものの、実際にはレイテンシーが問題になる場合が多いとのこと。特に、小さなデータパケットを頻繁に送信するビデオ通話などではレイテンシーが接続の問題につながりやすいとされています。Communications of the ACMは「あなたが自宅でビデオ通話をしている時に接続の問題が発生した場合、家族の誰かが映画をストリーミングしているか、スマートフォンから写真をアップロードしている可能性があります。これらの行為はビデオ通話が送信する一連のデータパケットとストリーミングなどによるパケットがインターネットの間で競合してしまうことにつながります」と語りました。

[![](https://i.gzn.jp/img/2024/10/10/internet-bandwidth/03_m.png)](https://i.gzn.jp/img/2024/10/10/internet-bandwidth/03_m.png)

これらの問題は、家庭用ルーターやプロバイダのルーターに古いソフトウェアが使用されていることが原因とされています。これらのソフトウェアには「**[Bufferbloat](https://queue.acm.org/detail.cfm?id=2071893)**」と呼ばれるバグが存在しており、これはソフトウェア側が大量のデータのバッファリングを優先する結果、ビデオ通話などの小さなデータパケットの送信が後回しになるというものです。この結果、**[ビデオ通話などで遅延や中断が発生する](https://cacm.acm.org/research/buffer-bloated-router-how-to-prevent-it-and-improve-performance/)**とされています。

「Bufferbloat」の解決策としてCommunications of the ACMは「**[fq_codel](https://wiki.archlinux.jp/index.php/%E9%AB%98%E5%BA%A6%E3%81%AA%E3%83%88%E3%83%A9%E3%83%95%E3%82%A3%E3%83%83%E3%82%AF%E5%88%B6%E5%BE%A1)**」や「**[Cake](https://www.bufferbloat.net/projects/codel/wiki/Cake/)**」などの最新のソフトウェアを導入することを推奨しています。しかし、ルーターのメーカーが古いソフトウェアを使用している場合、更新が困難な場合があります。そこでCommunications of the ACMは、家庭用ルーターとプロバイダが提供するモデムやルーター、Wi-Fiボックスの間に、より新しいルーターを設置することで、Bufferbloatを回避できると述べています。こうしたスマートルーターは、パイプの許容範囲内でできるだけ高速にデータを長し続け、ホームネットワーク内のデバイスが過剰にデータを送信すると、古いソフトウェアに対し適切に「競合が発生しています」という信号を送信してくれるそうです。

[![](https://i.gzn.jp/img/2024/10/10/internet-bandwidth/04_m.jpg)](https://i.gzn.jp/img/2024/10/10/internet-bandwidth/04_m.jpg)

しかし、すべての家庭や企業が新しいルーターを導入できるとは限りません。そこで、インターネット側から問題を捉え、帯域幅を簡単に増やすことができないプロバイダや企業が、既存の帯域幅をより有効に活用できるようにすることを目指したソフトウェアソリューション「**[LibreQoS](https://libreqos.io/)**」が開発されています。

LibreQoSはIPネットワーキングに「**[重み付き公平キューイング](https://ja.wikipedia.org/wiki/%E9%87%8D%E3%81%BF%E4%BB%98%E3%81%8D%E5%85%AC%E5%B9%B3%E3%82%AD%E3%83%A5%E3%83%BC%E3%82%A4%E3%83%B3%E3%82%B0)**」「**[トラフィックシェーピング](https://ja.wikipedia.org/wiki/%E3%83%88%E3%83%A9%E3%83%95%E3%82%A3%E3%83%83%E3%82%AF%E3%82%B7%E3%82%A7%E3%83%BC%E3%83%94%E3%83%B3%E3%82%B0)**」「**[アクティブキュー管理](https://en.wikipedia.org/wiki/Active_queue_management)**」などの包括的な修正を適用することで、システムの最も遅い部分に過負荷をかけない最高の速度を見つけるとのこと。つまり、家庭内で画像のアップロードが完了するまでビデオ通話のパケットが送信を待つように、パケットがキューにとどまる必要がなくなるとされています。

実際にLibreQoSを導入すると、100Mbpsの帯域幅で「**[ディアブロII](https://ja.wikipedia.org/wiki/%E3%83%87%E3%82%A3%E3%82%A2%E3%83%96%E3%83%ADII)**」と「**[ディアブロIV](https://ja.wikipedia.org/wiki/%E3%83%87%E3%82%A3%E3%82%A2%E3%83%96%E3%83%ADIV)**」を同時にダウンロードしながらZoomでビデオ通話を実施しても遅延に気付かないレベルでの会話が可能とのことです。