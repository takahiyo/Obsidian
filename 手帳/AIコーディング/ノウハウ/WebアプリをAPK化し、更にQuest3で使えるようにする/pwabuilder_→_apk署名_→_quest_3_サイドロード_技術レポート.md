---
notion-id: 2ef37ce6287181609af7f4880338cef8
---
# PWABuilder → APK署名 → Meta Quest 3 サイドロード 技術レポート

> 本ドキュメントは Markdown（GitHub互換） 形式で記載しています。

## 1. 目的

本レポートは、**PWABuilder を用いて PWA を Android APK 化し、**  
**独自署名（JKS + apksigner）を行ったうえで Meta Quest 3 にサイドロードするまでの一連の手順**を、  
次回以降の作業に再利用できるよう整理した技術記録である。

対象PWA：BookReader（epubreader-7w6.pages.dev）

---

## 2. 全体フロー概要

1. PWABuilder に PWA URL を投入し Android パッケージを生成
2. 生成された **署名前 APK（unsigned）** を取得
3. `keytool` で JKS（署名鍵）を作成
4. `apksigner` を用いて **v1 + v2 署名付き APK** を生成
5. 署名検証
6. Meta Quest 3 へ `adb install` でサイドロード

---

## 3. PWABuilder による APK 生成

### 3.1 使用URL

```
https://www.pwabuilder.com
```

トップページの **“Ship your PWA to app stores”** に以下を入力：

```
https://epubreader-7w6.pages.dev
```

### 3.2 Android パッケージ生成

- Report Card 画面 → **Package for stores**
- Android を選択
- 設定は原則デフォルト
- Download package により ZIP を取得

ZIP 内には以下が含まれる：

- `-unsigned.apk`（署名前 APK）
- `.aab`（Play Store 用）
- `Next-steps.md`
- TWA ソース一式

---

## 4. 署名鍵（JKS）の作成

### 4.1 使用コマンド（Windows）

```bash
keytool -genkeypair -v -keystore BookReader.jks -alias BookReaderKey -keyalg RSA -keysize 2048 -validity 10000
```

### 4.2 パスワードの整理

|種別|内容|
|---|---|
|ストアパス|JKS ファイル全体のパスワード|
|キーパス|alias（秘密鍵）専用のパスワード|

※ 今回は **Enter を押して両者を同一** にした

---

## 5. apksigner による APK 署名

### 5.1 apksigner の実体パス

```
C:\Users\takah\AppData\Local\Android\Sdk\build-tools\36.1.0\apksigner.bat
```

### 5.2 PowerShell 実行時の注意点

- フルパス実行時は **呼び出し演算子** `**&**` **が必須**
- 行継続は `^` ではなく **バッククォート `**
- バッククォートの後ろに空白があると失敗

### 5.3 実行コマンド（確定版）

```powershell
& "C:\Users\takah\AppData\Local\Android\Sdk\build-tools\36.1.0\apksigner.bat" sign `
  --ks "C:\Users\takah\OneDrive\Documents\BookReader.jks" `
  --ks-key-alias BookReaderKey `
  --ks-pass pass:v7xTcuHflt `
  --key-pass pass:v7xTcuHflt `
  --v1-signing-enabled true `
  --v2-signing-enabled true `
  --out "D:\Download\BookReader - Google Play package (2)\BookReader.apk" `
  "D:\Download\BookReader - Google Play package (2)\BookReader-unsigned.apk"
```

---

## 6. 署名検証

```powershell
& "C:\Users\takah\AppData\Local\Android\Sdk\build-tools\36.1.0\apksigner.bat" verify --verbose `
  "E:\Local_Storage\Tools\Flateight\BookReader-signed.apk"
```

成功時の期待ログ：

```
Verified using v1 scheme (JAR signing): true
Verified using v2 scheme (APK Signature Scheme v2): true
```

---

## 7. Meta Quest 3 へのインストール

```powershell
adb install "E:\Local_Storage\Tools\Flateight\BookReader-signed.apk"
```

- Quest 3 は事前に **開発者モード** を有効化
- 「不明な提供元」アプリとして表示される

---

## 8. よくある詰まりポイント（再発防止）

|症状|原因|対策|
|---|---|---|
|`apksigner が認識されない`|PATH 未設定|フルパス実行|
|`UnexpectedToken sign`|PowerShell の `&` 忘れ|`& "apksigner.bat"`|
|v1 / v2 検証失敗|署名オプション不足|`--v1 --v2` 明示|
|APK インストール不可|未署名 / v2不足|再署名|

---

## 9. 結論

- PWABuilder で生成される APK は **そのままでは Quest 3 に不適合**
- **独自 JKS + apksigner（v1 + v2）署名が必須**
- PowerShell 特有の構文（`&`, `）が最大の落とし穴

本手順を踏襲すれば、**任意の PWA を Quest 3 用 Android アプリとして再現可能**である。

---

（本レポートは再利用・横展開前提の技術覚書として作成）