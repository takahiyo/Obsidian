# Remotely Save 設定画面 完全日本語訳＆PROプラン徹底解説ガイド

Obsidianの人気同期プラグイン「Remotely Save」の設定画面（全項目）の日本語訳と、有料版「PROプラン」の機能・料金・導入手順をまとめた総合ガイドです。

## 1. Choose A Remote Service（リモートサービスの選択）

### Choose A Remote Service（リモートサービスの選択）

- **原文**: Start here. What service are you connecting to? S3, Dropbox, Webdav, OneDrive for personal, or Webdis?
    
- **和訳**: ここから開始します。どのサービスに接続しますか？（S3、Dropbox、WebDAV、個人用OneDrive、Webdisなど）
    

### Google Drive (PRO) (beta) に関する注意文

- **免責事項 1**: 本アプリはGoogle公式製品ではありません。Google Driveの公開APIを使用しているだけです。
    
- **免責事項 2**: 認証情報は端末ローカルに保存されます。悪意のあるプラグインや不具合のあるプラグインがこの情報を読み取る危険性があります。意図しないアクセスを発見した場合は、直ちに [Googleアカウントの権限設定](https://myaccount.google.com/permissions "null") から本アプリの連携を解除してください。
    
- **保存場所の注意**: Google Drive上に自動生成される「Obsidian_Vault」フォルダ内に同期されます。**このフォルダを手動で事前に作成しないでください。**
    
- **PRO（有料）機能の警告**: これはRemotely Saveの有料（PRO）機能です。利用にはRemotely Saveオンラインアカウントが必要です。
    
- **Google Drive Settings Not Available（設定不可）**: PRO機能に加入していないため、Google Driveの設定は利用できません。［View PRO Settings］
    

> 💡 **補足**: Google Drive同期は現在「有料プラン（PRO Connect）限定」です。**完全無料で同期したい場合は、選択肢を「Dropbox」「OneDrive」「WebDAV」「S3」などに変更**してください。

## 2. Basic Settings（基本設定）

|

| **項目名** | **原文の説明** | **日本語訳・解説** | **初期値** |

| **Encryption Password** （暗号化パスワード） | Password for E2E encryption. Empty for no password. You need to click "Confirm"... | エンドツーエンド（E2E）暗号化用のパスワード。空欄なら暗号化なし。入力後は「Confirm」をクリック。パスワード変更時は、クラウド側の全ファイルを手動削除して再同期する必要があります。 | 空欄（未設定） |

| **Schedule For Auto Run** （自動実行スケジュール） | The plugin tries to schedule the running after every interval. Battery may be impacted. | 指定した間隔ごとに自動で同期を試みます（バッテリー消費に影響する場合があります）。 | `every 1 minute` （1分ごと） |

| **Run Once On Start Up Automatically** （起動時の自動同期） | This setting causes the sync to run once automatically at startup... | Obsidian起動時に自動で1回同期を実行します（変更は次回の起動時から有効）。 | `sync once after 1 second of start up` （起動1秒後に同期） |

| **Sync On Save (experimental)** （保存時に同期［実験的］） | If you change your file, the plugin tries to trigger a sync. | ノートを変更・保存したタイミングで自動的に同期を開始します。 | `Disable` （無効） |

| **Skip Large Files** （大容量ファイルのスキップ） | Skip files with sizes larger than the threshold. Here $1\text{ MB} = 10^6\text{ bytes}$. | 指定した容量を超える大きなファイルを同期対象から除外します。 | `(not set)` （未設定） |

| **Show Last Successful Sync In Status Bar** （ステータスバー表示） | Show the time of the last successful sync in the status bar. | 画面右下のステータスバーに「最後に同期が成功した時刻」を表示します。 | `ON`（有効） |

| **Reset Last Successful Sync Time** （最終同期日時のリセット） | Reset last successful sync time. | 記録されている最終同期成功日時をリセットします。［Reset］ボタン | - |

| **Regex Of Paths To Ignore** （除外パスの正規表現） | Regex of paths of folders or files to ignore. One regex per line... | 同期から除外したいフォルダやファイルを正規表現で指定します（1行に1パターン）。先頭のスラッシュを除いた保管庫ルートからの相対パスで記述します。 | 空欄 |

| **Regex Of Paths To Allow** （許可パスの正規表現） | Regex of paths of folders or files to allow to sync. One regex per line... | 同期を許可するフォルダやファイルを指定します。**ここに入力した場合、設定フォルダ（.obsidian）などを含め、同期したい全パスを明示的に記述する必要があります。** | 空欄 |

## 3. Advanced Settings（詳細設定）

| **項目名** | **原文の説明** | **日本語訳・解説** | **初期値** |

| **Concurrency** （同時並行処理数） | How many files do you want to download or upload in parallel at most?... | 同時にダウンロード/アップロードする最大ファイル数。APIのレート制限（制限エラー）等が発生した場合は数値を下げてください。 | `5 (default)` |

| **Sync _ Files Or Folders** （アンダースコア付きの同期） | Sync files or folders starting with _ ("underscore") or not | アンダースコア（`_`）で始まるファイルやフォルダを同期するかどうか。 | `Disable` （同期しない） |

| **Sync Config Dir (experimental)** （設定フォルダの同期［実験的］） | Sync config dir .obsidian or not (inner folder .git and node_modules would be ignored)... | `.obsidian` 設定フォルダを同期するかどうか。全プラグインや設定に影響し、同期後にObsidianの再起動が必要になる場合があります。自己責任で有効化してください。 | `Disable` （同期しない） |

| **Sync Bookmarks (experimental)** （ブックマークの同期［実験的］） | Sync .obsidian/bookmarks.json or not... | ブックマーク（bookmarks.json）を同期するかどうか。上記の設定フォルダ同期を有効にしている場合は自動的に有効扱いになります。 | `Disable` |

| **Deletion Destination** （削除ファイルの移動先） | Which trash should the plugin put the files into while deleting? | 同期処理でファイルを削除する際、どこへ送るか。 | `system trash (default)` （OSのゴミ箱） |

| **Action For Conflict** （ファイル競合時の動作） | If a file is created or modified on both side since last update, it's a conflict event... | 前回同期以降に双方向で同じファイルが編集されていた場合の処理方針。※PRO版ではSmart Conflictが選べます。 | `newer version survives (default)` （新しい方を残す） |

| **Clear Duplicated Files By Smart Conflict** （重複ファイルの削除） | If you have ever used Smart Conflict (PRO) feature... | スマート競合解決（PRO機能）で生成された重複ファイルをローカルから一括削除します。※不要と確信できる場合のみ実行。［Start Scanning］ | - |

| **Abort Sync If Modification Above Percentage** （大量変更時の同期中断） | Abort the sync if more than n% of the files are going to be deleted / modified... | 変更または削除されるファイルが全体の $n\%$ を超えた場合に同期を中断し、意図せぬ大量消失事故を防ぎます（100で保護無効、0で常に中断）。 | `50 (default)` （50%） |

| **Sync Direction (experimental)** （同期の方向［実験的］） | Which direction should the plugin sync to?... | 同期の方向性を指定します（更新日時とサイズを基準に変更分のみ処理）。 | `Bidirectional (default)` （双方向同期） |

### ※ 同期方向（Sync Direction）の選択肢一覧

1. **Bidirectional（双方向）**: 両側の変更を相互に同期（通常はこれ）。
    
2. **Incremental Push（増分プッシュ）**: ローカルで変更・作成されたファイルのみをクラウドへ送信。
    
3. **Incremental Pull（増分プル）**: クラウド側で変更・作成されたファイルのみをローカルへ受信。
    
4. **Incremental Push And Delete（増分プッシュ＋削除）**: ローカルの変更と「削除」をクラウド側に反映。
    
5. **Incremental Pull And Delete（増分プル＋削除）**: クラウドの変更と「削除」をローカル側に反映。
    

## 4. Import and Export Partial Settings（設定の移行）

- **Export（エクスポート）**:
    
    - 設定内容をQRコードやURIとして書き出します。別の端末（スマホなど）へ設定を素早く引き継ぐ際に使用します。
        
    - `Export Basic And Advanced Part`（基本・詳細設定）や各サービス（S3、Dropbox、OneDriveなど）ごとの接続情報ボタンがあります。
        
- **Import（インポート）**:
    
    - エクスポートされたURIを貼り付けて［Confirm］を押すか、カメラでQRコードを読み取ることで設定を一括反映できます。
        

## 5. Account (for PRO features)（有料アカウント設定）

- **説明文**:
    
    - Remotely Saveの基本機能は「無料（FREE）」**であり、アカウント登録は**「不要（do NOT need）」です。
        
    - ただし、「Google Drive同期」や「スマート競合解決」などのPRO機能を使う場合のみ、オンラインアカウントを作成して認証を行う必要があります。
        
    - 利用する場合は [remotelysave.com](https://remotelysave.com/ "null") でサインアップし、下の「Connect」ボタンで端末と連携してください。（※Obsidian公式のアカウントとは無関係の独立したサービスです）
        
- **Remotely Save Online Account**: ［Sign Up / Sign In］（公式サイトを開く）
    
- **Connect**: ［Connect］（ログイン後にローカル端末と接続する）
    

## 6. Remotely Save「PROプラン」徹底解説（機能・料金・比較）

Remotely Saveには、完全無料の基本プランと、高度な機能が解放される「PROプラン」が存在します。

### ① 無料版 vs PRO版 機能比較表

| **機能・項目** | **Basic（無料版）** | **PRO Connect** | **PRO Merge（Smart Conflict）** |

| **S3 / S3互換（Cloudflare R2, MinIO等）** | ◯ | ◯ | ◯ |

| **Dropbox** | ◯ | ◯ | ◯ |

| **OneDrive for personal (App Folder)** | ◯ （`/Apps/remotely-save`限定） | ◯ | ◯ |

| **WebDAV（InfiniCloud, Nextcloud等）** | ◯ | ◯ | ◯ |

| **Webdis** | ◯ | ◯ | ◯ |

| **Google Drive 同期** | ×（利用不可） | **◯ 利用可能** | **◯ 利用可能** |

| **OneDrive for personal (Full / ルート指定)** | × | **◯ 利用可能** | **◯ 利用可能** |

| **Box / pCloud（ネイティブAPI） / Koofr** | × | **◯ 利用可能** | **◯ 利用可能** |

| **Azure Blob Storage / Yandex Disk** | × | **◯ 利用可能** | **◯ 利用可能** |

| **競合解決：Newer survives（新しい方を残す）** | ◯ | ◯ | ◯ |

| **競合解決：Smart Conflict（自動マージ/重複退避）** | × | × | **◯ 利用可能** |

| **アカウント登録** | **不要** | 必要 | 必要 |

| **料金** | **永久無料（FREE forever!）** | ベータ期間中無料提供枠あり （将来的な価格設定） | ベータ期間中無料提供枠あり （将来的な価格設定） |

### ② PROプランの2大特典とメリット

#### 1. PRO Connect：対応クラウドサービスの拡充

- **Google Driveへの対応**:
    
    個人ユーザーの利用率が最も高いGoogle Driveに直接同期できます（自動作成される `Obsidian_Vault` フォルダを使用）。
    
- **OneDrive (Full access)**:
    
    無料版では `/Apps/remotely-save` という固定サブフォルダにしか同期できませんが、PRO版ではOneDriveのルート直下や自由なフォルダパスを指定して保管庫を同期できます。
    
- **追加ストレージのネイティブ接続**:
    
    Box、pCloud、Koofr、Azure Blob Storage等にWebDAVを経由せず直接高速アクセスできます。
    

#### 2. PRO Merge（Smart Conflict）：ノート消失を防ぐ競合自動解決

- **無料版のリスク**:
    
    PCとスマホの両方でオフライン編集した場合などに競合が発生すると、無料版では「新しい方を残す（newer version survives）」しか選べません。この場合、**古い方の端末で追記したメモが上書きされて消滅する**危険性があります。
    
- **Smart Conflictの挙動**:
    
    - **小さなMarkdownファイル**: 内容を自動解析し、両方の差分を統合して「自動マージ」します。
        
    - **大きなMarkdownファイルや画像・添付ファイル**: 勝手に上書きせず、ファイル名を変更して「複製（Duplicate）」して両方を保持します。手動で後から見比べて安全に統合できます。
        

### ③ PRO機能の導入・連携手順

1. **アカウント作成**: ブラウザで [remotelysave.com](https://remotelysave.com/ "null") を開き、アカウントを作成（Sign Up）します。
    
2. **プランの確認・有効化**:
    
    ログイン後のダッシュボードで、利用したいPRO機能（PRO connect / PRO merge）を有効化します。
    
3. **Obsidianとの接続**:
    
    Obsidianの「Remotely Save」設定画面を開き、**「5. Account (for PRO features)」** までスクロールします。
    
    - ［Sign Up / Sign In］を押してログイン状態にする。
        
    - ［Connect］ボタンをクリックして、現在の端末（Vault）とアカウントを紐付ける。
        
4. **機能の反映**:
    
    設定画面上部の「Choose A Remote Service」で「Google Drive」が選べるようになっているか、あるいは「Action For Conflict」でSmart Conflictが有効になっているかを確認します。
    

### ④ あなたはPROに加入すべきか？（判断フロー）

- **PROプランを検討すべき人**:
    
    - すでにGoogle Drive（Google One）に課金しており、**どうしてもGoogle Drive上にノートを一本化したい**人。
        
    - PCとスマホで日常的に激しくメモを更新しており、**競合によるテキスト消失を絶対に避けたい**人（Smart Conflict目的）。
        
    - 会社のBoxやAzure Blob Storageなどを同期先に指定したい人。
        
- **無料版のままで全く問題ない人**:
    
    - **Dropbox**（無料2GB〜）、**OneDrive**（無料5GB〜）、または **Cloudflare R2（S3互換・無料枠10GB）** を使って同期できる人。
        
    - 同期を「1分ごと」や「起動時」に設定し、1人で1台ずつ順序よく作業するため、ファイルの激しい衝突が起こりにくい人。
        
    - E2E暗号化パスワードを設定して、一般的なクラウドで安全に同期できれば十分な人。
        

## 7. Debug（デバッグ・開発者向け設定）

日常的な使用では基本的に変更不要な高度な設定・トラブルシューティング項目です。

- **Alter Notice Level（通知レベル変更）**:
    
    - 同期時のポップアップ通知の詳細度。通常は `info`、エラー調査時は `debug` に切り替えます。
        
- **Output Current Settings From Disk To Console（設定のコンソール出力）**:
    
    - 保存されている暗号化/エンコード設定をコンソールに出力して確認します。
        
- **Obfuscate The Setting File Or Not（設定ファイルの難読化）**:
    
    - `data.json` 内の機密情報を保護するため難読化（暗号化に似た処理）を施すか。通常は `Enable`（有効）のままにします。
        
- **View Console Log（ログの確認方法）**:
    
    - PCは `Ctrl + Shift + I`（Macは `Cmd + Option + I`）の開発者ツールでログを確認。モバイルは「Logstravaganza」プラグインを推奨。
        
- **Export Sync Plans（同期計画のエクスポート）**:
    
    - 同期実行直前に作られる内部処理計画（どのファイルが追加・削除されるか）のログを書き出します。
        
- **Delete Sync Plans History In DB（同期計画履歴の削除）**:
    
    - データベース内の同期計画ログを消去します。
        
- **Delete Prev Sync Details In DB（前回同期詳細の削除）**:
    
    - データベース内の「前回の同期成功履歴」を消去し、全ファイルを新規ファイルとして再判定させます。
        
- **Export Profiler Results / Enable Profiler 系（プロファイラー）**:
    
    - 同期処理の各工程にかかった時間やサイズを計測し、同期が遅い原因を突き止める開発者向け機能です（通常は `Disable`）。
        
- **Output Vault Base Path And Randomly Assigned ID**:
    
    - 保管庫のパスとランダムIDをコンソールに出力します。
        
- **Reset Local Internal Cache/Databases（キャッシュ/DBのリセット）**:
    
    - 同期の不整合が直らない場合にローカルDBを初期化します（※保存済みの接続パスワード等は消去されません）。