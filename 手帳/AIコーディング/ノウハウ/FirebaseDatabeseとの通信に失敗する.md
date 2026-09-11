---
notion-id: 2ec37ce6287180c093befb30fbaf2706
テキスト: 基本的にFirestoreSDKでの通信を指せるのがアクセス数を抑える意味でも効果的但し、社内ネットワークやファイアウォール等、通信制限がかかる環境だと高確率で通信エラーになりがちでもある。そこで、FirestoreSDKでの通信に失敗した時はCloudFlareWorkersを通した通信を行うという設計にすることで、大抵の場合に通用する※こういう構成をGraceful Degradationと呼ぶ※但し、書き込みについては常にWorkers経由にした方がデータ整合性に寄与するらしい
選択:
  - CloudFlareWorkers
  - FirebaseDatabese
  - Firestore
---
