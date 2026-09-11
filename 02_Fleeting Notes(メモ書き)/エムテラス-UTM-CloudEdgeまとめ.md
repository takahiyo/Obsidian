# 税理士法人エムテラス UTM / CloudEdgeまとめ

出力日: 2026-09-08 / 出力先: Vaultルート
対象: 金山本社 + 岡崎拠点

## 1. 結論（現状）
- 金山のUTMは `TrendMicro CloudEdge50`（納品2020-10-22、資産名 `CloudEdge50 2`）
- 金山ルータは `YAMAHA NVR510 x2`（ISP用 + VPN用、納品2021-06-29）
  - `NVR510 3` = ISP用 / `NVR510 7` = VPN用
- 岡崎ルータは `YAMAHA NVR510`（資産名 `NVR510`）
- 2024-09-11版（プライオ導入）が最新図面。VPNプライオ用 `CISCO C1111-8P` が金山・岡崎に追加

## 2. 拠点別構成（図面からの読取り）

### 金山（192.168.1.0/24）
- ONU（フレッツ光ネクスト FSHS隼）→ ISP NVR510 → CloudEdge50（DHCP有効、.254）→ L2SW → 端末群
- VPN系: NVR510ローカル（192.168.1.253、DHCP無効期あり）→ VoIP OG420Xa → CPE C1111-8P（10.0.1.1）
- 端末例: NAS OSpro4 192.168.1.103、Atlas720（Win2019、RDPで会計ソフト）、他社AP、PC多数
- 主装置: NTT αA1Std

### 岡崎（192.168.2.0/24）
- ONU → NVR510（WAN 10.0.2.254 / LAN 192.168.2.253、DHCP有効）→ CPE C1111-8P（10.0.2.1）
- 旧構成（2021/2024-06）: NVR510 user02@cvn、192.168.101.2経由で金山と拠点間VPN

### 変遷
- 2021-06-24: 金山 CloudEdge50 192.168.1.254 + 岡崎 NVR510 user02、FWVで拠点間VPN
- 2024-06-03: 同上維持（FSHS隼表記）
- 2024-07-01: プライオ準備 — 金山CPE 10.0.1.1 / 岡崎CPE 10.0.2.1、NVR WANを10.0.x.254化
- 2024-09-11: プライオ導入 — 10.0.0.0/16管理（.254）、金山10.0.1.0/24 / 岡崎10.0.2.0/24

## 3. CloudEdge50 一般情報（Web補完・要公式確認）
- TrendMicro UTM。入口対策（標的型メール3段フィルタ、Webレピュテーション）+ 出口対策（C&Cブロック）+ 侵入検知/防御、ウイルス/SPAM、P2P/BOT制御
- 管理はクラウドコンソール（CECC）+ オンプレコンソール。リモート設定・ログ・日本語レポート可
- バイパス機能で故障/電源断時も通信継続（機種依存あり）
- ライセンス切れ後は30日Grace（全機能動作）、以後はセキュリティ機能ほぼ無効・コンソール情報は残る（KA-0013403、2026-01-30更新）
- 現行はG3世代（50G3/100G3/SB-S G3）。50は50名規模向け・ファンレス。エムテラス納品は2020年の無印50のため、EOS/ライセンス更新要確認
- 問合せ先（Vault内）: NTT西日本セキュリティおまかせサポートセンター（商材別一覧参照）

参考:
- https://www.otsuka-shokai.co.jp/products/security/internet/firewall-utm/cloudedge.html
- https://success.trendmicro.com/ja-JP/solution/KA-0013403
- https://docs.trendmicro.com/ja-jp/documentation/cloud-edge/

## 4. Vault内ソース
- 顧客: `Notion/顧客情報/顧客管理/税理士法人エムテラス（金山）/税理士法人エムテラス（金山）.md`
- 顧客: `Notion/顧客情報/顧客管理/税理士法人エムテラス（岡崎）/税理士法人エムテラス（岡崎）.md`
- 資産: `Notion/顧客情報/顧客資産管理/CloudEdge50 2.md`（2020-10-22納品）
- 資産: `Notion/顧客情報/顧客資産管理/NVR510 3.md`（ISP用・PPPoE情報あり）
- 資産: `Notion/顧客情報/顧客資産管理/NVR510 7.md`（VPN用）
- 資産: `Notion/顧客情報/顧客資産管理/NVR510.md`（岡崎）
- 資産: `Notion/顧客情報/顧客資産管理/VPNプライオ.md`、`VPNワイド管理者 1.md`
- 図面: `Notion/Attachments/_Shared/【吉田CA 峯沢（エムテラス）】NW構成図_20210624.pdf`
- 図面: `Notion/Attachments/_Shared/20240603_配線イメージ図_税理士法人エムテラス_01_-配線接続図.drawio.pdf`
- 図面: `Notion/Attachments/_Shared/20240701_配線イメージ図_税理士法人エムテラス_02_アドレス設計変更-配線接続図.drawio.pdf`
- 図面: `Notion/Attachments/_Shared/20240911_配線イメージ図_税理士法人エムテラス_03_プライオ導入-配線接続図.drawio.pdf`

## 5. 要確認（次アクション）
- CloudEdge50（2020納品）のライセンス/保守・後継G3要否
- 岡崎現行がプライオ構成か旧FWV構成か（最新現地確認）
- NVR510 3のPPPoE詳細は資産ファイルにあり（本書では転記せず原典参照）
- 他顧客のコンソール情報は混入させていないこと
