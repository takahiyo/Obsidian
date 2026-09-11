---
notion-id: 12a37ce62871806a90fbeed1e4ad2068
URL: https://learn.microsoft.com/ja-jp/windows-server/storage/file-server/best-practices-analyzer/smb-open-file-sharing-ports
更新されました: Invalid date
作成日時: Invalid date
---
# 概要

- Windows11では別セグメントとの共有フォルダ設定が面倒になっている

# 解決策

1. 共有フォルダを設定しているPCのWindowsDefenderファイアウォールの詳細設定を開く
2. ’ローカルコンピュータのセキュリティ’
3. 受信の規則
4. 設定を変更したいプロファイルの’ファイルとプリンターの共有（NBセッション受信）’を開く
	1. ’スコープ’タブを開く
	2. リモートIPアドレスの’追加’
	3. 複合機のIPアドレスを追加
5. 設定を変更したいプロファイルの’ファイルとプリンターの共有（SMB受信）’を開く
	1. ’スコープ’タブを開く
	2. リモートIPアドレスの’追加’
	3. 複合機のIPアドレスを追加

解決策2

上記でも駄目だった場合に、SMB用のポート自体を通す設定が有効だった例がある

https://zapping.beccou.com/2023/08/08/windows-shared-folders-cannot-be-accessed-between-different-segments/

# 補足

- アクセス権限に'guest’を’読み書き可’で追加すると、複合機側のアクセス情報が'guest’じゃなくても送信できたが、理由がわからない