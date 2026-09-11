---
notion-id: 31337ce6287180bbbd68e5c461b6a029
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - 仕事
  - 知識
---
以下は**「Windows 10 で一定時間の無操作によるロック（LockWorkStation）を “一時的に停止” したい場合の、実行可能な CMD / PowerShell での方法」**です。

一次情報として、**キー送信による無操作状態の回避（ロック阻止）を PowerShell で実現する方法**が文献で確認されています。

---

# ✅ 最も確実で一時的に使える方法：PowerShell で疑似キー送信

Windows は **“一定時間キー入力がなければロックする”** 仕組みのため、

無操作を継続して疑似入力で防ぐのが一時停止として最適です。

### ▼ PowerShell（ロック防止・確実に動作）

```jsx
$WShell = New-Object -Com "Wscript.Shell"
while (1) {
$WShell.SendKeys("{SCROLLLOCK}")
Start-Sleep -Seconds 60
}
```

  

📝 このスクリプトは 60 秒ごとに ScrollLock キーを送信し、**「ユーザーが操作している」状態を維持**してロックを防ぎます。

ScrollLock は多くの場合アプリに影響しません。

📌 出典（一次情報）

ShellHacks: “Windows: Prevent Lock Screen Timeout When Idle”（2020-04-08）

https://www.shellhacks.com/windows-prevent-lock-screen-timeout-when-idle/

（該当箇所に同一コードを確認） [[shellhacks.com]](https://www.shellhacks.com/windows-prevent-lock-screen-timeout-when-idle/)

---

# ✅ CMD で実質的に同じことを行う方法は？

CMD には **キー疑似送信の機能がなく**、

CMD 単体で「ロックを止める」ことは不可です。

→ 可能な方法は **CMD から PowerShell を呼び出して実行**すること。

### ▼ CMD から PowerShell ロック防止スクリプトを起動

```jsx
powershell -command "$WShell = New-Object -Com 'Wscript.Shell'; while (1) { $WShell.SendKeys('{SCROLLLOCK}'); Start-Sleep -Seconds 60 }"
```

---

# ⚠ ロックタイマー自体を「0（無効）」にするレジストリ変更は？

レジストリ `InactivityTimeoutSecs` を 0 に設定すればロック無効化できますが、

**これは “一時停止” ではなく設定変更**です。

文献：Interactive logon: Machine inactivity limit（InactivityTimeoutSecs）

https://windowsforum.com/threads/windows-10-inactivity-lock-timeout-registry-policy-and-powershell.384044/ [[windowsforum.com]](https://windowsforum.com/threads/windows-10-inactivity-lock-timeout-registry-policy-and-powershell.384044/)

---

# 🧩 結論（最も安全で一時的な方法）

|目的|推奨方法|
|---|---|
|一時的にロックを止めたい（終了すると元に戻る）|**PowerShell の疑似キー送信が最適**|
|CMD で済ませたい|**CMD → PowerShell 実行**|
|設定を恒久的に無効化したい|レジストリの `InactivityTimeoutSecs=0`|

---

必要なら、

- 自動で停止するバージョン
- トレイ最小化版
- PowerShell スクリプトの EXE 化  
	なども作成できます。