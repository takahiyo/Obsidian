---
notion-id: ce6d8b0ad1b4429287d93d6e3ccc82b1
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - セキュリティ
  - 仕事
  - 知識
---
# 概要

暗号化アルゴリズムと暗号鍵は、予め手動で設定しておくか、通信相手との事前折衝の段階で決定・交換が行われる

お互いの間で得られた暗号化アルゴリズムと暗号化鍵に関する合意をSA(Security Association)と呼ぶ

このSAの確定と同時にSAと関連付けされたSPI(Security Pointer Index)と呼ばれる32bitの整数値が割り当てられる

# 中核を成す3つのプロトコル

IKE(Internet Key Exchange)

鍵交換使われるプロトコル

メインモードとアグレッシブモードという2つのモードが有り、

メインモードは両拠点のIPアドレスが固定の時に用いられ、安全性が高い

アグレッシブモードは片方の拠点のIPアドレスが不定の場合に用いられ、メインモードに比べてパケットの交換が少ない

ESP(Encapsulating Security Payload)

データの転送に利用するプロトコル

トランスポートモードではIPパケットで運ぶデータ部分のみ暗号化し、IPヘッダの後ろにESPヘッダを挿入する

トンネルモードではIPヘッダとデータ部分を合わせたものをまとめて暗号化した上で、新たにIPヘッダをつけて送信を行う

AH(Authentication Header)

完全性と認証のためのプロトコル

AHではデータの暗号化は行わず、SPI、シーケンス番号、認証データのみをパックして通常のIPパケットの中、IPヘッダの直後に加えるようになっている

# 関連するポート番号

TCP/UDP　500：ISAKMP(Internet Security Association and Key Management Protocol)

TCP/UDP　50：ESP