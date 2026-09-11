---
notion-id: f715f78197fe4e6a8bb3889215b46610
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - 知識
---
# **FXS / FXOとは何か？**

**FXS**と**FXO**はアナログ電話回線（POTS‐Plain Old Telephone Serviceとも呼ばれる）に使用されるポートの名称です。

**FXS** ― **F**oreign e**X**change **S**ubscriberインターフェースとは、受信契約者にアナログ回線を配信するポートです。つまり、ダイアルトーン、バッテリ電流、呼出信号電圧を伝播する壁の差し込み口です。

**FXO** ― **F**oreign e**X**change **O**fficeインターフェースとは、アナログ回線を受信するポートで、電話やFAX、又はアナログ電話システムに備わっている差し込み口を指し、電話の接続状態を示します（ループ閉鎖）。FAXや電話機のような機器には、FXOポートが備わっているため、「FXOデバイス」とも呼ばれます。

FXOとFXSは、雌雄組み合わせ型のプラグのように常に対になっています。PBXが無い場合、電話会社によって供給されたFXSポートに電話機を直接接続します。

![[fxs-fxo-without-pbx-200x93.png]]

PBXを使用する場合、電話会社から供給された回線と電話をPBXに接続します。そのため、PBXには電話会社が供給するFXSに接続するためのFXOポートと、電話機やFAXに接続するためのFXSポートの両方が必要です。

![[fxs-fxo-with-pbx-200x93.png]]

## FXS / FXO / VoIP

アナログ電話回線やアナログ電話機を[VoIPシステム](https://www.3cx.jp/ip-pbx/)に接続する機器や、PBXをVoIPサービスプロバイダに接続したりPBX同士を接続する機器を購入する際、FXSとFXOの二つの用語はおそらく耳にするでしょう。

**FXOゲートウェイ**

アナログ電話回線をIP-PBXに接続するためには、FXOゲートウェイが必要です。 ゲートウェイのFXOポートとFXSポートを繋ぐことにより、アナログ電話回線がVoIP信号に変換されます。[VoIPゲートウェイの製造を](https://www.3cx.com/voip-gateways/)。

![[fxo-gateway-200x114.png]]

**FXSゲートウェイ**

FXSゲートウェイは従来型のPBXを通して1本または複数の回線をVoIPシステムやプロバイダに接続する際に使用します。FXSゲートウェイを使用すると、通常は電話会社に接続されるFXOポートを通してインターネットやVoIPシステムに接続することが可能になります。

![[fxs-gateway-200x93.png]]

**FXSアダプタ(ATAアダプタ)**

FXSアダプタはアナログ電話機やFAXをVoIPシステム又はVoIPプロバイダに接続する際に使用します。電話機又はFAXのFXOポートとアダプタを繋いで使用します。

![[fxs-adapter-200x141.png]]

**続きを読む**

- [_**ボイスオーバーIPとは**_](https://www.3cx.jp/voip-sip/voice-over-ip/)
    
- [_**PBX電話システムとは**_](https://www.3cx.jp/voip-sip/pbx-phone-system/)
- [_**VoIPゲートウェイとは何か？**_](https://www.3cx.jp/voip-sip/voip-gateway/)