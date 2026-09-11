---
notion-id: 04ec5ee18c204215b2e473f9705de45a
コマンド例: robocopy 元 先 /mir /dt /r:3 /w:5
解説: よく使う基本的な構文元から先へとにかくファイルをミラー複写、属性無し、リトライ3ウェイト5
---
【基本的な構成】

robocopy コピー元 コピー先 [ファイル[ファイル]...] [オプション]

※ファイル名にはワイルドカードも使える

# よく使うオプション

- /l　プレビューモード。実際のファイル情報を触らずに、実行した結果を表示する
- /s　サブディレクトリコピー時、空のディレクトリは無視
- /purge　コピー元に無いファイルやディレクトリをコピー先から削除
- /mir　コピー元に合わせてコピー先をミラーリング
- /move　コピー元からは削除
- /mot:m　コピー元を監視。m分後に変更があればコピーされる
	- コマンドプロンプトは閉じず、常時稼働する
	- /mir等と併用しないと、ファイル名変更等で増える一方なので注意
- /max:n　nバイトより大きいファイルは除外
- /min:n　nバイトより小さいファイルは除外
- /maxage:n　n日より古いファイルは除外
- /minage:n　n日より新しいファイルは除外
- /maxlad:n　n日以降アクセスしていないファイルを除外
- /minlad:n　n日以降アクセスしたファイルを除外
- /copy:フラグ　既定値はDAT
	- D=データ (代替データストリームを含む)
	- A=属性
	- T=タイムスタンプ
	- X=代替データストリームをコピーしない
	- S=セキュリティ情報=アクセス権情報(NTFS ACL)
	- O=所有者情報
	- U=監査情報
- /timfix　タイムスタンプを更新する
- /E　空のディレクトリを含むサブディレクトリをコピーする
- /nocopy　フォルダ構造だけをコピーする※上記/Eと併用する

---

## 知っておくべきRobocopyの基本動作

### **Robocopyのデフォルト動作の主なポイント**

Robocopy はフォルダ・ファイルをコピーするツールですが、コピー先に既に同じファイルが存在する場合はコピーをせず、必要なファイルだけをコピーするため、非常に効率よく短時間でコピーを行うことができ、とても便利です。

意外とあまり説明されていませんが、Robocopyのデフォルトの動作は、以下のようになります。主なポイントを記載します。

- デフォルトでは、コピー元フォルダ直下のファイル（フォルダは含みません）をコピーします。サブフォルダ配下もコピーする場合、/S, /E, /MIRなどを指定する必要があります。
- 既にコピー先にファイルが存在する場合、コピー元ファイルとコピー先ファイルを比較し、タイムスタンプとファイルサイズが同じであればコピーは行わない。
- コピー先のほうがタイムスタンプが新しくても上書きされる。
- ファイル属性については比較しないので、ファイル属性が更新されていてもコピーされない。
- ファイルコピー時のクラスの分類と、コピー処理をまとめると、以下の表ようになります。(セキュリティ情報をコピーする場合の動作については**、**[**こちら**](https://n-archives.net/software/robosync/articles/robocopy-security-information)の記事をご覧ください)

ファイル・フォルダ コピー時ののクラス分類とコピー動作

|   |   |   |
|---|---|---|
|クラス|クラス条件|コピー動作|
|コピー元|コピー先|更新時刻|
|Lonely|ある|ない|
|Tweaked|ある|ある|
|Same|ある|ある|
|Changed|ある|ある|
|Newer|ある|ある|
|Older|ある|ある|
|Extra|ない|ある|
|Mismatched|ある*1|ある*1|

- 1: コピー元がファイルでコピー先がフォルダ、またはその逆
- 2: 「元＞先」はコピー元ファイルの方が新しい、「元＜先」はコピー先ファイルの方が新しい
- 3: /PURGEまたは/MIR指定時コピー先を削除
- ファイルのコピーは、ファイルのデータ(代替データストリームも含む)、タイムスタンプ、ファイル属性がコピーされる。（アクセス権情報(NTFS ACL)、所有者情報、監査情報はコピーされません。）
- フォルダのコピーは、フォルダの属性、および、代替データストリームがコピーされる。フォルダのタイムスタンプはコピー元を引き継がない。（空のフォルダはコピー元のタイムスタンプとなるが、それ以外のフォルダはコピー実行時のタイムスタンプになる。）
- シンボリックリンクやジャンクションポイントは、通常のフォルダとして扱われ、配下の対象ファイル・フォルダをコピーする。（予想外のデータ量になる可能性がある）
- コピーに失敗した場合、30秒間隔で、最大百万回リトライを行う。

### **全般ルール**

- ファイル名、パス名に空白文字を含む場合""で囲む必要があります。

## Robocopyコマンド説明

### **Syntax**

```
robocopy <コピー元フォルダ> <コピー先フォルダ> [<ファイル>[ ...]] [<オプション>]
```

### **パラメータ**

|   |   |
|---|---|
|コピー元フォルダ|コピー元フォルダを指定します。  <br>• 通常のパス形式（絶対パス、相対パス。例 N:\folder\subfolder）、または、UNCパス形式（例 \\server\share\path）で指定します。  <br>• ファイル名、パス名に空白文字を含む場合""で囲む必要があります。|
|コピー先フォルダ|コピー先フォルダを指定します。  <br>• 通常のパス形式（絶対パス、相対パス。例 N:\folder\subfolder）、または、UNCパス形式（例 \\server\share\path）で指定します。  <br>• ファイル名、パス名に空白文字を含む場合""で囲む必要があります。|
|ファイル|コピーの対象とするファイル名を指定します。  <br>• ワイルドカード（* と ? のみ）を使うことができます。  <br>• 省略時の規定値は *.* (すべてのファイルを対象)とみなされます。  <br>• ファイル名に空白文字を含む場合""で囲む必要があります。  <br>• 複数のファイル名を列挙して指定できます。空白で区切ります。  <br>• パス（\を含む文字列）は指定できません。  <br>• あくまでもファイル名を指定するためのものであり、フォルダ名は制限を受けない。|
|オプション|オプションを指定します。|

## Robocopyのオプション

### **コピーオプション**

|   |   |
|---|---|
|/S|サブディレクトリをコピーしますが、空のディレクトリはコピーしません。**関連記事：「**[**RoboSync設定事例：増分バックアップ(直近20回,14日以内保存)**](https://n-archives.net/software/robosync/articles/incremental-backup-example)」|
|/E|空のディレクトリを含むサブディレクトリをコピーします。**関連記事：「**[**RoboSync設定事例：個人PCのバックアップ設定例**](https://n-archives.net/software/robosync/articles/personal-pc-backup-example)**」関連記事：「**[**Robocopy /MIRオプションの動作と注意点**](https://n-archives.net/software/robosync/articles/robocopy-mir-option)**」**|
|/LEV:n|コピー元ディレクトリ ツリーの上位 n レベルのみをコピーします。|
|/Z|再起動可能モードでファイルをコピーします。  <br>• オーバーヘッドが大きいため再起動可能モードを必要としない場合は使用すべきでない**関連記事：「**[**Robocopy /Zオプションの再起動可能モードとは**](https://n-archives.net/software/robosync/articles/robocopy-z-option-restartable-mode)**」**|
|/B|バックアップ モードでファイルをコピーします。  <br>• ファイル、フォルダのアクセス権限情報(ACL)を上書きします。|
|/ZB|再起動可能モードを使用します。アクセスが拒否された場合、バックアップ モードを使用します。|
|/J|バッファーなし I/O を使用してコピーします (大きなファイルで推奨)。|
|/EFSRAW|暗号化されたすべてのファイルを EFS RAW モードでコピーします。|
|/COPY:コピーフラグ|ファイルにコピーする情報を指定します。(既定値は /COPY:DAT)  <br>• コピーフラグ:D=データ  (代替データストリームを含む)A=属性T=タイムスタンプX=代替データストリームをコピーしないS=セキュリティ情報=アクセス権情報(NTFS ACL)O=所有者情報U=監査情報**関連記事：「**[**Robocopyでセキュリティ情報を正しくコピーする方法と注意点**](https://n-archives.net/software/robosync/articles/robocopy-security-information)**」**|
|/SEC|セキュリティと共にファイルをコピーします (/COPY:DATS と同等)。**関連記事：「**[**Robocopyでセキュリティ情報を正しくコピーする方法と注意点**](https://n-archives.net/software/robosync/articles/robocopy-security-information)**」**|
|/COPYALL|ファイル情報をすべてコピーします (/COPY:DATSOU と同等)。**関連記事：「**[**Robocopyでセキュリティ情報を正しくコピーする方法と注意点**](https://n-archives.net/software/robosync/articles/robocopy-security-information)**」**|
|/NOCOPY|ファイル情報をコピーしません (/PURGE と共に使用すると便利)。**関連記事：「**[**Robocopy コピー元に存在しないファイルをコピー先から削除する**](https://n-archives.net/software/robosync/articles/robocopy-purge-nocopy)**」関連記事：「**[**Robocopy フォルダツリーのみをコピーする方法**](https://n-archives.net/software/robosync/articles/robocopy-how-to-copy-folder-tree-only)**」**|
|/SECFIX|スキップしたファイルも含むすべてのファイルのファイルセキュリティを修正します。  <br>• /SECFIXを使用する場合は、/COPYALL /COPY:O /COPY:S /COPY:U /SECのいずれかを設定し、どの情報をコピーするかを指定する。**関連記事：「**[**Robocopyでセキュリティ情報を正しくコピーする方法と注意点**](https://n-archives.net/software/robosync/articles/robocopy-security-information)**」**|
|/TIMFIX|スキップしたファイルも含むすべてのファイルのファイル時刻を修正します。|
|/PURGE|コピー元に存在しないコピー先のファイル・フォルダを削除します。**関連記事：「**[**Robocopy /MIRオプションの動作と注意点**](https://n-archives.net/software/robosync/articles/robocopy-mir-option)**」**|
|/MIR|ディレクトリ ツリーをミラー化します (/E /PURGE と同等)。  <br>• /MIR は /E /PURGEと同等ですが、次の点のみ異なります。 コピー先にフォルダが存在する場合、/MIRはセキュリティ設定をコピーしますが、/E /PURGEはコピーしません。**関連記事：「**[**Robocopy /MIRオプションの動作と注意点**](https://n-archives.net/software/robosync/articles/robocopy-mir-option)**」関連記事：「**[**Robocopyでセキュリティ情報を正しくコピーする方法と注意点**](https://n-archives.net/software/robosync/articles/robocopy-security-information)**」関連記事：「**[**RoboSync設定事例：フルバックアップ3世代**](https://n-archives.net/software/robosync/articles/full-backup-example)**」関連記事：「**[**RoboSync設定事例：個人PCのバックアップ設定例**](https://n-archives.net/software/robosync/articles/personal-pc-backup-example)**」**|
|/MOV|ファイルを移動します (コピー後にコピー元から削除)。|
|/MOVE|ファイルとディレクトリを移動します (コピー後にコピー元から削除)。|
|/A+:[RASHCNET]|コピーされたファイルに指定の属性を追加します。|
|/A-:[RASHCNET]|コピーされたファイルから指定の属性を削除します。|
|/CREATE|ディレクトリ ツリーと長さ 0 のファイルのみを作成します。**関連記事：「**[**Robocopy /CREATEオプションの目的と使い方**](https://n-archives.net/software/robosync/articles/robocopy-create-option)**」**|
|/FAT|8.3 FAT ファイル名のみを使用してコピー先ファイルを作成します。|
|/256|256 文字を超える非常に長いパスのサポートをオフにします。|
|/MON:n|コピー元を監視し、n 回以上の変更があった場合に再度実行します。**関連記事：「**[**Robocopy /MON /MOT を使ってフォルダ更新を監視する**](https://n-archives.net/software/robosync/articles/robocopy-mon-mot-option)**」**|
|/MOT:m|コピー元を監視し、m 分後に変更があった場合に再度実行します。**関連記事：「**[**Robocopy /MON /MOT を使ってフォルダ更新を監視する**](https://n-archives.net/software/robosync/articles/robocopy-mon-mot-option)**」**|
|/RH:hhmm-hhmm|実行時間 - 新しいコピーを開始できる時刻を設定します。|
|/PF|実行時間をファイルごと (パスごとではない) に確認します。|
|/IPG:n|低速回線で帯域幅を解放するため、1パケット(64KB)送信ごとにnミリ秒待機する。|
|/SJ|ジャンクション配下のファイルやフォルダを追跡コピーするのではなく、ジャンクションを作成します。  <br>• /SJを指定していないデフォルトの動作は、ジャンクション配下のファイルまたはフォルダを追跡しコピーします。  <br>• /SJを指定した場合、ジャンクションは、ジャンクションとしてコピーされます。ジャンクション配下のファイルまたはフォルダはコピーされません。|
|/SL|シンボリックリンクのリンク先の対象をコピーするのではなく、シンボリックリンクを作成します。  <br>• /SLを指定していないデフォルトの動作は、シンボリックリンクのリンク先のファイルまたはフォルダを追跡しコピーします。  <br>• /SLを指定した場合、シンボリックリンクは、シンボリックリンクとしてコピーされます。リンク先のファイルまたはフォルダはコピーされません。|
|/MT[:n]|n 個のスレッドのマルチスレッド コピーを実行します(既定値 8)。 n は 1 から 128 までの値である必要があります。 このオプションは、/IPG および /EFSRAW オプションと互換性がありません。 パフォーマンスの向上のため、/LOG オプションを使用して出力をリダイレクトします。|
|/DCOPY:コピーフラグ|ディレクトリにコピーする情報 (既定値は /DCOPY:DA)。  <br>• コピーフラグ:D= データ   (代替データストリーム)A= 属性   (拡張ファイル属性)T= タイムスタンプE=拡張属性X=代替データストリームをコピーしない**関連記事：「**[**Robocopy: /DCOPY:DATのすすめ**](https://n-archives.net/software/robosync/articles/dcopy-dat)**」**|
|/NODCOPY|ディレクトリ情報をコピーしません (既定では /DCOPY:DA が実行されます)。**関連記事：「**[**Robocopy: /DCOPY:DATのすすめ**](https://n-archives.net/software/robosync/articles/dcopy-dat)」|
|/NOOFFLOAD|Windows のオフロードをコピーするメカニズムを使用せずにファイルをコピーします。|
|/COMPRESS|SMB圧縮機能を利用してネットワーク転送時にファイル圧縮を行う。**関連記事：「**[**Robocopy /COMPRESS を使ってNW経由のコピーを高速化する**](https://n-archives.net/software/robosync/articles/robocopy-compress-option)**」関連記事：「**[**SMB圧縮を利用してNW経由コピーを高速化する**](https://n-archives.net/software/robosync/articles/robocopy-smb-compression)**」**|

### **ファイル選択オプション**

|   |   |
|---|---|
|/A|アーカイブ属性が設定されているファイルのみをコピーします。**関連記事：「**[**RoboSyncを使って差分・増分バックアップを設定してみる**](https://n-archives.net/software/robosync/articles/incremental-differential-backup)」**関連記事：「**[**RoboSync設定事例：増分バックアップ(直近20回,14日以内保存)**](https://n-archives.net/software/robosync/articles/incremental-backup-example)」|
|/M|アーカイブ属性のあるファイルのみをコピーし、リセットします。**関連記事：「**[**RoboSyncを使って差分・増分バックアップを設定してみる**](https://n-archives.net/software/robosync/articles/incremental-differential-backup)」**関連記事：「**[**RoboSync設定事例：増分バックアップ(直近20回,14日以内保存)**](https://n-archives.net/software/robosync/articles/incremental-backup-example)」|
|/IA:[RASHCNETO]|指定されたいずれかの属性が設定されているファイルのみを含みます。|
|/XA:[RASHCNETO]|指定されたいずれかの属性が設定されているファイルを除外します。|
|/XF files...|指定された名前/パス/ワイルドカードに一致するファイルを除外します。  <br>• 複数のファイル名を列挙できます。空白で区切ります。  <br>• ワイルドカードが使用できますが、* と ? のみが使用可能です。  <br>• ファイル名だけでなくフルパス名(例 N:\folder\filename.txt)も指定可能ですが、相対パスでの指定はできないようです。  <br>• ファイル名、パス名に空白文字を含む場合""で囲む必要があります。**関連記事：「**[**Robocopy /MIRオプションの動作と注意点**](https://n-archives.net/software/robosync/articles/robocopy-mir-option)**」**|
|/XD dirs...|指定された名前/パス/ワイルドカードに一致するフォルダ(ディレクトリ)を除外します。  <br>• 複数のフォルダ(ディレクトリ)名を列挙できます。空白で区切ります。  <br>• ワイルドカードが使用できますが、* と ? のみが使用可能です。  <br>• フォルダ名だけでなくフルパス名(例 N:\folder\subfolder)も指定可能ですが、相対パスでの指定はできないようです。  <br>• ファイル名、パス名に空白文字を含む場合""で囲む必要があります。**関連記事：「**[**Robocopy /MIRオプションの動作と注意点**](https://n-archives.net/software/robosync/articles/robocopy-mir-option)**」**|
|/XC|変更された(Changed)ファイルを除外します。|
|/XN|新しい(Newer)ファイルを除外します。|
|/XO|古い(Older)ファイルを除外します。|
|/XX|コピー先にだけ存在するファイルとディレクトリ(eXtra)を除外します。|
|/XL|コピー元にだけ存在するファイルとディレクトリ(Lonely)を除外します。|
|/IS|タイムスタンプとファイルサイズが同一なファイル(Same)を含みます。|
|/IT|ファイル属性だけが異なるファイル(Tweaked)を含めます。|
|/MAX:n|最大ファイル サイズ - n バイトより大きいファイルを除外します。**関連記事：「**[**Robocopy /Zオプションの再起動可能モードとは**](https://n-archives.net/software/robosync/articles/robocopy-z-option-restartable-mode)」|
|/MIN:n|最小ファイル サイズ - n バイトより小さいファイルを除外します。**関連記事：「**[**Robocopy /Zオプションの再起動可能モードとは**](https://n-archives.net/software/robosync/articles/robocopy-z-option-restartable-mode)」|
|/MAXAGE:n|更新日時が指定した日時より古いファイルを除外する。  <br>• n < 1900の場合 n日前、または nはYYYYMMDDの日付です**関連記事：「**[**Robocopy の MAXAGE MINAGE MAXLAD MINLADオプション**](https://n-archives.net/software/robosync/articles/robocopy-maxage-minage-maxlad-minlad)」|
|/MINAGE:n|更新日時が指定した日時より新しいファイルを除外する。  <br>• n < 1900の場合 n日前、または nはYYYYMMDDの日付です**関連記事：「**[**Robocopy の MAXAGE MINAGE MAXLAD MINLADオプション**](https://n-archives.net/software/robosync/articles/robocopy-maxage-minage-maxlad-minlad)」|
|/MAXLAD:n|最終アクセス日時が指定した日時より前のファイルを除外する。  <br>• n < 1900の場合 n日前、または nはYYYYMMDDの日付です**関連記事：「**[**Robocopy の MAXAGE MINAGE MAXLAD MINLADオプション**](https://n-archives.net/software/robosync/articles/robocopy-maxage-minage-maxlad-minlad)」|
|/MINLAD:n|最終アクセス日時が指定した日時より後のファイルを除外する。  <br>• n < 1900の場合 n日前、または nはYYYYMMDDの日付です**関連記事：「**[**Robocopy の MAXAGE MINAGE MAXLAD MINLADオプション**](https://n-archives.net/software/robosync/articles/robocopy-maxage-minage-maxlad-minlad)」|
|/FFT|FAT ファイル時間 (2 秒の粒度) を仮定します。|
|/DST|1 時間の DST 時間差を補正します。|
|/XJ|ジャンクションポイントとシンボリックリンクを除外します。 (デフォルト動作では含まれます)  <br>• /XJを指定しないデフォルト動作は、ジャンクションポイント(ボリュームマウントポイント)とシンボリックリンクは通常のディレクトリとしてその配下の対象をコピーする。そのため、予想以上のデータ量になる可能性がある。  <br>• /XJを指定することで。ジャンクションポイントとシンボリックリンク配下をスキップする。|
|/XJD|ディレクトリのジャンクションポイントとシンボリックリンクを除外します。|
|/XJF|ファイルのシンボリックリンクを除外します。|
|/IM|Modifiedクラスを含めます**関連記事：「**[**Robocopyでセキュリティ情報を正しくコピーする方法と注意点**](https://n-archives.net/software/robosync/articles/robocopy-security-information)**」**|

### **再試行オプション**

|   |   |
|---|---|
|/R:n|失敗したコピーに対する再試行数: 既定値は 1,000,000。|
|/W:n|再試行と再試行の間の待機時間: 既定値は、30 秒です。|
|/REG|既定の設定としてレジストリに /R:n と /W:n を保存します。  <br>• レジストリ保存先は、HKCU\Software\Microsoft\ResKit\Robocopy|
|/TBD|共有名が定義されるのを待ちます (再試行エラー 67)。|
|/LFSM|空き領域不足モードで動作します。コピー実行中に、コピー先ボリュームの空き容量がボリューム全体の10%以下になる場合、コピーを一時停止し、空き容量ができるのを待ちます。|
|/LFSM:n[KMG]|空き領域不足モードで動作します。コピー実行中に、コピー先ボリュームの空き容量が、n [K:kilo,M:mega,G:giga] バイト以下になる場合、コピーを一時停止し、空き容量ができるのを待ちます。|

### **ログオプション**

|   |   |
|---|---|
|/L|処理内容の表示のみを行いコピー先フォルダに変更を加えません。コピー、削除、タイムスタンプの追加などを行いません。**関連記事：「**[**RoboSync TIPS: /Lオプションをつけて実行結果をプレビューする**](https://n-archives.net/software/robosync/articles/robosync-tips-option-l)」|
|/X|選択されたファイルのみではなく、余分なファイルをすべて報告します。|
|/V|スキップされたファイルの情報も表示します。|
|/TS|コピー元ファイルのタイムスタンプを表示します。|
|/FP|ファイルの完全なパス名を表示します。|
|/BYTES|ファイルサイズをバイトで表示します。|
|/NS|ファイルサイズをログに表示しません。|
|/NC|ファイルクラスをログに表示しません。|
|/NFL|ファイル名をログに表示しません。|
|/NDL|ディレクトリ名をログに表示しません。|
|/NP|コピーの完了率を表示しません。|
|/ETA|コピーするファイルの推定完了時刻を表示します。|
|/LOG:ファイル|ログファイルに出力します (既存のログファイルを上書きします)。  <br>• ログファイルの保存先のフォルダは存在している必要があります。  <br>• ファイル名、パス名に空白文字を含む場合""で囲む必要があります。**関連記事：「**[**Robocopyのログ出力の文字コードについて調べてみた**](https://n-archives.net/software/robosync/articles/robocopy-unicode-unilog-log)」|
|/LOG+:ファイル|ログファイルに出力します (既存のログファイルに追加します)。  <br>• ログファイルの保存先のフォルダは存在している必要があります。  <br>• ファイル名、パス名に空白文字を含む場合""で囲む必要があります。**関連記事：「**[**Robocopyのログ出力の文字コードについて調べてみた**](https://n-archives.net/software/robosync/articles/robocopy-unicode-unilog-log)」|
|/UNILOG:ファイル|ログファイルに UNICODE で出力します (既存のログファイルを上書きします)。  <br>• ログファイルの保存先のフォルダは存在している必要があります。  <br>• ファイル名、パス名に空白文字を含む場合""で囲む必要があります。**関連記事：「**[**Robocopyのログ出力の文字コードについて調べてみた**](https://n-archives.net/software/robosync/articles/robocopy-unicode-unilog-log)」**関連記事：「**[**Robocopyを英語表示にしてログ表示の桁ずれをなくす**](https://n-archives.net/software/robosync/articles/robocopy-english-mode)」|
|/UNILOG+:ファイル|ログファイルに UNICODE で出力します (既存のログファイルに追加します)。  <br>• ログファイルの保存先のフォルダは存在している必要があります。  <br>• ファイル名、パス名に空白文字を含む場合""で囲む必要があります。  <br>• このオプションはUNICODEを出力しないので使い物になりません(個人調べ)**関連記事：「**[**Robocopyのログ出力の文字コードについて調べてみた**](https://n-archives.net/software/robosync/articles/robocopy-unicode-unilog-log)」|
|/TEE|ログファイル出力時、コンソールウィンドウにも出力します。**関連記事：「**[**Robocopyを英語表示にしてログ表示の桁ずれをなくす**](https://n-archives.net/software/robosync/articles/robocopy-english-mode)」|
|/NJH|ジョブヘッダーを表示しません。|
|/NJS|ジョブサマリを表示しません。|
|/UNICODE|状態を UNICODE で出力します。  <br>• このオプションは出力が異常なため使い物になりません(個人調べ)**関連記事：「**[**Robocopyのログ出力の文字コードについて調べてみた**](https://n-archives.net/software/robosync/articles/robocopy-unicode-unilog-log)」|

### **ジョブオプション**

|   |   |
|---|---|
|/JOB:ジョブ名|ジョブ名で指定されたジョブファイルからパラメーターを取得します。|
|/SAVE:ジョブ名|ジョブ名で指定されたジョブファイルにパラメーターを保存します。|
|/QUIT|コマンドラインパラメータの解釈のみ行います。パラメータ表示後終了します。**関連記事：「**[**RoboSync TIPS: /Lオプションをつけて実行結果をプレビューする**](https://n-archives.net/software/robosync/articles/robosync-tips-option-l)」|
|/NOSD|コピー元フォルダを指定しません。|
|/NODD|コピー先フォルダを指定しません。|
|/IF files...|コピーの対象とするファイル名を指定します  <br>• ファイル名の指定方法は、コマンドパラメータの「ファイル」と同じ。  <br>• /IFはジョブファイルで使用することを想定しているが、通常のコマンドでも使用できる。|

## Robocopyの戻り値

戻り値一覧(Microsoftドキュメントより)

|   |   |
|---|---|
|戻り値|説明|
|0|コピーは行われませんでした。処理は正常に終了ました。ミスマッチ(Mismatched)も見つかりませんでした。全てのファイルはコピー先に存在しています。|
|1|ファイルのコピーが行われました。|
|2|コピー先にのみ存在するファイルが見つかりました。コピーされたファイルはありませんでした。|
|3|ファイルのコピーが行われました。コピー先にのみ存在するファイルが見つかりました。処理は正常に終了しました。|
|5|ファイルのコピーが行われました。ミスマッチ(Mismatched)が見つかりました。処理は正常に終了しました。|
|6|コピー先にのみ存在するファイルが見つかりました。ミスマッチ(Mismatched)が見つかりました。コピーされたファイルはありませんでした。処理は正常に終了しました。全てのファイルはコピー先に存在しています。|
|7|ファイルのコピーが行われました。ミスマッチ(Mismatched)が見つかりました。コピー先にのみ存在するファイルが見つかりました。|
|8|コピーできなかったファイルがあります。|
|8以上|何らかの異常が発生しました。|

戻り値の算出方法ですが、各ファイルの処理結果が下表の結果種別ごとにカウントされ、該当するものがあった結果種別のビット値が合計され、戻り値として算出されます。

結果種別（ビット値）

|   |   |
|---|---|
|結果種別(ビット値)|説明|
|0|コピーする必要がないため、何も実施しなかったログの「スキップ(Skipped)」としてカウント|
|1|ファイルのコピーが成功した (フォルダーのコピーは含まれません)ログの「コピー済み(Copied)」としてカウント|
|2|コピー先にのみ存在するファイル/フォルダが確認されたログの「Extras」としてカウント|
|4|同じ名前で別の種類のファイルが存在した(Mismatched)ログの「不一致(Mismatch)」としてカウント|
|8|コピーに失敗したログの「失敗(FAILED)」としてカウント|
|16|致命的エラー。全く処理できなかったなど。|

戻り値の参照方法は、robocopy実行後に、以下のようなスクリプトで判定可能です。

```
if %errorlevel% == 0 echo no error
```

## ファイル属性

/A+, /A-, /IA, /XA オプションで指定するファイル属性は以下の通り。

|   |   |
|---|---|
|属性名|意味|
|R|読み取りのみ属性 (Read only)|
|A|アーカイブ属性 (Archive)|
|S|システム属性 (System)|
|H|隠し属性 (Hidden)|
|C|圧縮属性 (Compressed)|
|N|インデックス抑止属性 (Not content indexed)|
|E|暗号化属性 (Encrypted)|
|T|一時ファイル属性 (Temporary)|
|O|オフライン属性 (Offline)|

---

以下は社内業務がタブレット運用だった際のメモ

構成主旨

- 運用時のToolsフォルダは常にローカルPCがメインであり、robocopyではバックアップしか取らない
    
	日常業務用に「タブレットLAN」にコピーするが、そこから戻さない為、更新はローカルPC上で行う
    
- 「全体共有」は「SEフォルダ」に1次バックアップ、「SEフォルダ」ごと「Gドライブ」に2次バックアップする
- 「SEフォルダ」は「Gドライブ」への1次バックアップのみ
- 「顧客管理」は多重バックアップを取っているが、原本は「全体共有\お客様情報\顧客管理」とする

業務開始時

1. 「全体共有\お客様情報」　→　「タブレットLAN\お客様情報」
    
	前日業務終了時「3.」をタブレットLANで運用する為。ミラーリング
    
	「顧客管理」原本から運用フォルダへのコピーと考える
    
2. 「ローカルPC\マイドキュメント\Tools」　→　「タブレットLAN\お客様以外\Tools」
    
	主にCLCLを運用し、J-thomas等のパスワード変更に対応する為。ミラーリング
    

業務終了時

1. 「ローカルPC\マイドキュメント\Tools」　→　「SEフォルダ\お客様以外\Tools」
    
	主にCLCLとバックアップ用バッチファイルのバックアップを取るため。ミラーリング
    
2. 「タブレットLAN\お客様情報\顧客管理」　→　「SEフォルダ\お客様情報\顧客管理」
    
	顧客管理の多重バックアップの為　１つ目
    
3. 「タブレットLAN\お客様情報」　→　「全体共有\お客様情報」
    
	日常業務運用ファイル戻し用。「顧客管理」はこれを以て運用フォルダから原本更新と考える
    
4. 「全体共有\お客様情報」　→　「SEフォルダ\お客様情報\BACKUP」
    
	顧客管理の多重バックアップを兼ねて　２つ目
    
5. 「全体共有\お客様情報以外」　→　「SEフォルダ\お客様情報以外\BACKUP」
    
	全体共有フォルダ毎SEフォルダにバックアップ
    
6. 「SEフォルダ」　→　「G:\」
    
	上記までのバックアップ自体を「SEフォルダ」ごとGドライブにバックアップ
    
	顧客管理の多重バックアップ　３つ目、４つ目