---
notion-id: 1c137ce6287180a78017d53e5457399f
更新されました: Invalid date
作成日時: Invalid date
---
Stable Diffusion WebUIをAMD Ryzen 9 6900HXのRadeon Graphicsで利用する際、DirectMLを使用することでGPUアクセラレーションが可能です。以下に設定手順を説明します。

1. **Pythonのインストール**:  
	Stable Diffusion WebUIはPython 3.10.6を推奨しています。既にインストール済みの場合は、このステップをスキップしてください。インストール後、環境変数`PATH`にPythonのパスが追加されていることを確認してください。
2. **Gitのインストール**:  
	Stable Diffusion WebUIのセットアップや更新にはGitが必要です。公式サイトからGitをダウンロードし、インストールしてください。インストール後、コマンドプロンプトやPowerShellで`git --version`と入力し、バージョン情報が表示されることを確認してください。
3. **Stable Diffusion WebUIの取得**:  
	コマンドプロンプトやPowerShellを開き、以下のコマンドを実行して、Stable Diffusion WebUIをダウンロードします。
    
	```bash
	git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
	```
    



1. **DirectML対応のための設定**:  
	ダウンロードしたディレクトリに移動し、以下のコマンドを実行して、DirectML対応のリポジトリをクローンします。
    
	```bash
	git clone https://github.com/lshqqytiger/stable-diffusion-webui-directml.git
	```
    



次に、`stable-diffusion-webui-directml`ディレクトリ内のファイルを`stable-diffusion-webui`ディレクトリに上書きコピーします。

1. **必要なライブラリのインストール**:  
	仮想環境を作成し、必要なライブラリをインストールします。
    
	```bash
	cd stable-diffusion-webui
	python -m venv venv
	venv\Scripts\activate
	pip install -r requirements.txt
	pip install torch-directml
	```
    



1. **起動スクリプトの設定**:  
	`webui-user.bat`ファイルをテキストエディタで開き、以下の行を追加または編集します。
    
	```bash
	set COMMANDLINE_ARGS=--skip-torch-cuda-test --use-directml --precision full --no-half
	```
    



1. **WebUIの起動**:  
	設定が完了したら、`webui-user.bat`を実行してWebUIを起動します。初回起動時にはモデルのダウンロードなどが行われるため、時間がかかる場合があります。

**注意点**:

- `torch-directml`のインストール時にタイムアウトエラーが発生する場合、ネットワーク環境を確認し、再試行してください。
- `git`コマンドが認識されない場合、Gitが正しくインストールされ、環境変数`PATH`に追加されていることを確認してください。
- `-use-directml`オプションが認識されない場合、DirectML対応のリポジトリが正しく適用されているか確認してください。

これらの手順を踏むことで、AMD Ryzen 9 6900HXのRadeon Graphicsを利用してStable Diffusion WebUIを動作させることが可能となります。