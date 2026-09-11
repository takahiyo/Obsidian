---
notion-id: 766f13157cc84cb3932f1a95fc3acb0a
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - 知識
  - 記事
---
**環境**

- Windows10
- Apache2.4

**手順**

- Apache2.4のインストール後、フォルダを開く
	- 以降、特に指定しない限りフォルダはApacheインストールフォルダ内を基準とする
- 「conf」フォルダ内の「hppd.conf」ファイルを複写バックアップしておく
- hppd.confをメモ帳等で開き、Apacheのインストールフォルダを指定

```
Define SRVROOT "c:\Apache24"
```

- Apacheのアクセスポートを指定

```
Listen 80
```

- WebDAC関連のモジュールから\#を外して有効化する

```
LoadModule dav_module modules/mod_dav.so
LoadModule dav_fs_module modules/mod_dav_fs.so
LoadModule dav_lock_module modules/mod_dav_lock.so
```

- hppd.confの最下行に以下を追加する

```
# WebDAV
Alias /local_storage "C:\Local_Storage"
<Directory "C:\Local_Storage">
	Dav On
	Options Indexes MultiViews
	AllowOverride None
	Require all granted
</Directory>
```

※2行目、3行目の「c:\local_storage」は公開したいフォルダを指定する

- 「bin」フォルダ内の「hppd.exe」を実行する
	- この時点でコマンドプロンプトが立ち上がり、サーバーが起動する
	- 上記例なら、[127.0.0.1](http://127.0.0.1/)で「htdocs」内の「index.html」が開き、[127.0.0.1/local_storage](http://127.0.0.1/local_storage)で「c:\local_storage」内のファイル一覧がWebDAV表示される
	- 127.0.0.1をグローバルアドレスやDDNSに変えてもアクセスできるはず