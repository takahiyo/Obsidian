---
notion-id: 13037ce6287180b4ab3afbcd38dd85f8
Pythonコード:
  - "[[ScreenOff_Stopper.pyw]]"
解説: 実行するとタスクトレイにシンプルな■アイコンが表示される🟦はスクリーンセーバーが有効で安全🟥はスクリーンセーバーが無効で危険というイメージ
---
# 余談

- Pythonインタプリタ上で実行するだけのシンプルなコードが下記
    
	```jsx
	import ctypes
	
	# モニターオフとスクリーンセーバーを防止
	ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
	
	# 入力待ち
	input('何かキーを押すと終了します...')
	
	# 通常の動作に戻す
	ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
	```