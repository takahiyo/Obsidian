---
notion-id: 11690faec94941d7b536d2eb626463fb
URL: https://webnation.co.jp/10%E5%88%86%E3%81%A7%E3%81%A7%E3%81%8D%E3%82%8Bsteabledeffusionwebui%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89-windows11/?utm_source=chatgpt.com#1_Python
更新されました: Invalid date
作成日時: Invalid date
---
[![](https://webnation.co.jp/wp-content/uploads/2023/09/%E5%90%8D%E7%A7%B0%E6%9C%AA%E8%A8%AD%E5%AE%9A-1_03-1.png)](https://webnation.co.jp/wp-content/uploads/2023/09/%E5%90%8D%E7%A7%B0%E6%9C%AA%E8%A8%AD%E5%AE%9A-1_03-1.png)

==こんにちは、ウェブネーションの山下です。==  
==AIの技術革新が目覚ましい昨今、ChatGPT（AIチャットボット）やStableDeffusion（画像生成AI）等のアプリケーションによってAIが一般層にも身近なものになっていますね。==  
==私もAIチャットは日々の業務でも日常的に利用していますし、画像生成AIから画像素材を生成して業務に役立てれないかと調査研究をしています。==

==しかしStableDeffusionによる画像生成AIの環境を作ることがPC上で作業環境を作ることのなじみのないかだと少しハードルを高く感じてしまうのでは？と思い今回の表題にある通り簡単な環境構築の方法をまとめました。==

==※StableDeffusionでの画像生成はNVIDIA製のグラフィックボードが搭載されたPCで行ってください。==

==目次==

- ==[ステップ1: Pythonのインストール](https://webnation.co.jp/10%E5%88%86%E3%81%A7%E3%81%A7%E3%81%8D%E3%82%8Bsteabledeffusionwebui%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89-windows11/#1_Python)==
- ==[ステップ2: Gitのインストール](https://webnation.co.jp/10%E5%88%86%E3%81%A7%E3%81%A7%E3%81%8D%E3%82%8Bsteabledeffusionwebui%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89-windows11/#2_Git)==
- ==[ステップ3: Stable Diffusion Web UIの取得](https://webnation.co.jp/10%E5%88%86%E3%81%A7%E3%81%A7%E3%81%8D%E3%82%8Bsteabledeffusionwebui%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89-windows11/#3_Stable_Diffusion_Web_UI)==
- ==[ステップ4: 実行方法](https://webnation.co.jp/10%E5%88%86%E3%81%A7%E3%81%A7%E3%81%8D%E3%82%8Bsteabledeffusionwebui%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89-windows11/#4)==
- ==[ステップ6: 学習済みモデルのダウンロード](https://webnation.co.jp/10%E5%88%86%E3%81%A7%E3%81%A7%E3%81%8D%E3%82%8Bsteabledeffusionwebui%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89-windows11/#6)==
- ==[ステップ7: プロンプト（呪文）を入力して生成](https://webnation.co.jp/10%E5%88%86%E3%81%A7%E3%81%A7%E3%81%8D%E3%82%8Bsteabledeffusionwebui%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89-windows11/#7)==

## ==**ステップ1: Pythonのインストール**==

==PythonはStable Diffusion Web UIの動作に必要です。Python 3.10.6以上をインストールしましょう。==

1. ==[Python 公式ウェブサイト](https://www.python.org/downloads/) から最新バージョンのPythonをダウンロードします。==
2. ==ダウンロードしたインストーラーを実行し、指示に従ってPythonをインストールします。[追加オプション] のセクションで、”Add Python to PATH” オプションにチェックを入れてください。==

==Windows11ではコマンドプロンプトからpythonと入力するとWindows Storeが表示され最新のpythonをインストールしてくれるようなので既存でpythonがインストールされていない方はWindowsStoreからで大丈夫かと思います（**私の環境だと3.11.5**がインストールされました）==

## ==**ステップ2: Gitのインストール**==

==Stable Diffusion Web UIのソースコードを取得するためにGitが必要です。以下の手順でGitをインストールします。==

1. ==[Git 公式ウェブサイト](https://git-scm.com/downloads) からWindows用のGitをダウンロードします。==
2. ==ダウンロードしたインストーラーを実行し、指示に従ってGitをインストールします。すべてデフォルトの設定を使用してください。==

[![](https://webnation.co.jp/wp-content/uploads/2023/09/image-3.png)](https://webnation.co.jp/wp-content/uploads/2023/09/image-3.png)

==Gitとは分散型バージョン管理システムで、ソフトウェア開発者がプロジェクトの変更履歴を追跡し、複数の人が協力してコードを管理できるツールです。ファイルの変更、コミット、ブランチの作成、マージなどをサポートし、プロジェクトの履歴と安定性を保つのに役立ちます。==

## ==**ステップ3: Stable Diffusion Web UIの取得**==

==Stable Diffusion Web UIのソースコードを取得しましょう。==

1. ==デスクトップに作業フォルダを追加する場合デスクトップ上で右クリックからターミナルで開くを押します。==
2. ==コマンドプロンプトを開き、以下のコマンドを実行して**Stable Diffusion Web UI**のソースコードを取得します。==
    
	==git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git==
    

## ==**ステップ4: 実行方法**==

==ダウンロードが完了したら、Stable Diffusion Web UIを実行してみましょう。==  
==開いているコマンドプロンプトに、以下のコマンドを実行します。==

```
cd stable-diffusion-webui
.\webui-user.bat
```

==またはダウンロードしたフォルダから、`webui-user.bat` ファイルをダブルクリックして実行することもできます。==  
==PCのスペックにもよるかと思いますが数分でウェブブラウザ上に以下のような画面が開くかと思います。==

[![](https://webnation.co.jp/wp-content/uploads/2023/09/image-1024x472.png)](https://webnation.co.jp/wp-content/uploads/2023/09/image-1024x472.png)

## ==**ステップ6: 学習済みモデルのダウンロード**==

==早速、画像生成を試したいところですが高クォリティな画像を生成するにはSteableDeffusionに学習済みのモデルファイルを読み込ませる必要があります。==  
==学習済みモデルは[Civitai](https://civitai.com/)というモデルファイルのインデックスサービスから無料で公開されているものが沢山ありますのでそちらから検索してダウンロードすることをお勧めします。==  
==今回は、[BreakDomain](https://civitai.com/models/126259?modelVersionId=164360)というアニメ調の画像生成に特化したモデルを利用させていただきます。==

==ダウンロードボタンを押すとbreakdomainxl_V05g.safetensorsというファイルがダウンロードできますので落としたファイルをstable-diffusion-webui->models->Stable-diffusionのフォルダの中に移動します。==

[![](https://webnation.co.jp/wp-content/uploads/2023/09/image-1-1024x334.png)](https://webnation.co.jp/wp-content/uploads/2023/09/image-1-1024x334.png)

==移動したら、ブラウザ上の画面上部のStable Diffusion checkpointに「breakdomainxl_V05g」が追加されているので選択してください。（ない場合、右側のリロードボタンを押してください）==

[![](https://webnation.co.jp/wp-content/uploads/2023/09/image-2.png)](https://webnation.co.jp/wp-content/uploads/2023/09/image-2.png)

## ==**ステップ7: プロンプト（呪文）を入力して生成**==

==さて、学習済みモデルも反映できましたので実際に画像を生成してみます。==  
==ブラウザ上の「Prompt」に生成したい画像の特徴「Negative prompt」に除外したい特徴を入力します。==  
==はじめは何を入力していいかよくわからないかと思いますがCivitaiの[BreakDomain](https://civitai.com/models/126259?modelVersionId=164360)のページに生成例が掲載してあるので参考にPromptを入力してみます。==

```
Prompt
1girl, hacker vibes, technology, future, grey vibes, blue details, pretty face , grey hair, perfect face, beautiful face, masterpiece

Negative prompt
easynegative, bad-artist-anime, bad-hands-5, (bad quality, low quality, worst quality), extra chest, deformed, bad anatomy,text,watermark,
```

==上記のプロンプトではサイバーな雰囲気の少女のイラストが生成されるはずです。==  
==「Generate」ボタンを押してみましょう。==

[![](https://webnation.co.jp/wp-content/uploads/2023/09/00002-1197459853.png)](https://webnation.co.jp/wp-content/uploads/2023/09/00002-1197459853.png)

==プロンプト通りのイラストが生成されました！==

==ごらんのみなさまも生成できましたでしょうか？==  
==意外と簡単に環境構築ができますね。==  
==以上、Windows11環境へのSteableDeffusionWebUI（画像生成AI）の構築方法でした。==

==この記事を書いた人==

==株式会社ウェブネーションのウェブデザイナー兼フロントエンドエンジニアです。最近はAIチャットやAI画像生成の研究などもしています。==