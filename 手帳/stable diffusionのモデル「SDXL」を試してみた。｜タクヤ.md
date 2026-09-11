---
notion-id: dcf294fbd64b46d986ace036dcc07b5c
URL: https://note.com/zztakuya/n/n1619f88ba080
更新されました: Invalid date
作成日時: Invalid date
---
![[rectangle_large_type_2_559e4bcfe9ed4bbcf56cda8593bd372f.png]]

stable diffusionの画像をより綺麗にできるという「SDXL」モデルで画像を生成してみました。

今回は実際にどのくらい綺麗になるのか、検証してみたいと思います。

## SDXLを導入する方法

### 導入前に確認すること

導入にあたり条件として、「**stable diffusion**」のバージョンが「**1.6**」以上であることが条件になります。

もしも、バージョンが「**1.6**」以前の場合は「コマンドプロンプト(macの場合はターミナル)」のstable diffuisonのディレクトリで、「**git pull**」と入力することで、バージョンを更新できます。

git pullコマンドの実行

![[1705759976188-kZBA9D5MrB.png]]

![[1705760021802-cBC5NyNUzr.png]]

上記の様に出たら、「**stable diffusion**」を起動して、画面の最下部のバージョンを確認します。

「1.6」以上のバージョンになっていればオッケーです。

一番左がバージョン

![[1705760147842-Q4bu0VMSEI.png]]

### 用意するもの

「SDXL」の導入にあたって必要なものが3つ(1つは任意)あります。

ダウンロードは以下のサイトで行えます。

1. baseモデル
    
	https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/tree/main
    
2. reflineモデル
    
	https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/tree/main
    
3. VAE
    
	https://huggingface.co/stabilityai/sdxl-vae/tree/main
    

それぞれのダウンロードが完了したら、「**stable diffusion**」の以下のフォルダに保存していきます。

・baseモデル、reflineモデル

「stable-diffusion-webui\models\stable-diffusion」以下にダウンロードした「Model」を入れてください。

・VAE

「stable-diffusion-webui\models\VAE」以下にダウンロードした「VAE」を入れてください。

### 使い方

今回は「txt2img」を使って、「SDXL」を試してみます。

モデルにダウンロードした「base」モデルを設定します。

![[1705760675327-FWOCn0XUDw.png]]

次に「Settings」タブの中の左側のメニューの中に「VAE」とあるので選択します。

「SD VAE」という選択項目があるので、ダウンロードした「VAE」を選択します。

選択後「Apply settings」を押して準備完了です。

![[1705760813384-3GBvwletiQ.png]]

「txt2img」タブに移動して、プロンプトを入力します。

次に「Refliner」という項目があるので、選択します。

ここで、先ほどダウンロードした「refline」モデルを設定します。

「SDXL」で出力するときの画像サイズは「1024 x 1024」が良いそうです。

以下が実際に出力してみた画像です。

ポジティブプロンプト  
best quality, masterpiece, ultra high res, robot, beam saber, gundam, flying, wing parts, blue body, beam rifle, shield, shot rifle, fighting, fighting stance, planet

ネガティブプロンプト  
worst quality, ugly, bad anatomy, jpeg artifacts, nsfw, text, watermark, bad hands, extra digit, fewer digits, bad anatomy, long_body, mutated hands, missing arms, extra_arms, extra_legs, bad hands, missing_limb, disconnected_limbs, extra_fingers, missing fingers, liquid fingers, ugly face, deformed eyes, cropped

以下が実際に生成された画像です。

カッコいいですね！！

ライジングフリーダムみたい。

ちなみに「VAE」をきちんと設定しないと画像が乱れてしまうので、「SDXL」を使うときは、必ず対応ものを選択してください。

以下は失敗例です。

## SDXLと通常のモデルを比較してみた

### 人物

SDXL

ふつくしい

[v1-5pruned-emaonly.safetensors](https://v1-5pruned-emaonly.safetensors/)(Hires.fixを使用)

ポジティブプロンプト  
best quality, masterpiece, ultra high res, 1 lady, from front, cowboy shot, enjoy, sparkle (in the eyes), beautiful detailed eyes, open mouth, tiara, hair accessory, side ponytail, long hair, blunt bangs, blue hair, wizard, dress, standing, starry pond

ネガティブプロンプト  
worst quality, ugly, bad anatomy, jpeg artifacts, nsfw, text, watermark, bad hands, extra digit, fewer digits, bad anatomy, long_body, mutated hands, missing arms, extra_arms, extra_legs, bad hands, missing_limb, disconnected_limbs, extra_fingers, missing fingers, liquid fingers, ugly face, deformed eyes, cropped

### 風景

SDXL

これリアル写真じゃないの…

[v1-5pruned-emaonly.safetensors](https://v1-5pruned-emaonly.safetensors/)(Hires.fixを使用)

ポジティブプロンプト  
best quality, masterpiece, ultra high res, (background only:1.5), mountain, lake, snow, day

ネガティブプロンプト  
worst quality, ugly, bad anatomy, jpeg artifacts, nsfw, text, watermark, bad hands, extra digit, fewer digits, bad anatomy, long_body, mutated hands, missing arms, extra_arms, extra_legs, bad hands, missing_limb, disconnected_limbs, extra_fingers, missing fingers, liquid fingers, ugly face, deformed eyes, cropped

### 動物

SDXL

可愛い

[v1-5pruned-emaonly.safetensors](https://v1-5pruned-emaonly.safetensors/)(Hires.fixを使用)

寝なかったかー

ポジティブプロンプト  
best quality, masterpiece, ultra high res, cat, brown color, american short hair, indoors, sleeping, morning

ネガティブプロンプト  
worst quality, ugly, bad anatomy, jpeg artifacts, nsfw, text, watermark, bad hands, extra digit, fewer digits, bad anatomy, long_body, mutated hands, missing arms, extra_arms, extra_legs, bad hands, missing_limb, disconnected_limbs, extra_fingers, missing fingers, liquid fingers, ugly face, deformed eyes, cropped

モデルが違うので、比較にならないかもですが、「SDXL」の場合は画像がおかしくなることがほとんどありませんでした。

また、どちらも高画質になりましたが、「SDXL」に対応した他のモデルを使った場合はまた別の結果が出るかもしれません。

設定もほとんど変えていないので、設定次第では更に高画質なイラストを生成することができそうです！

## 使ってみた感想

めちゃくちゃ高画質になってドキドキしました。

ただ、今使っているPCのグラボのVRAMが12GBしかないので、グラボを買い替えたくなりますね。

今のところ止まったりはしていないので、高画質な画像を出すために使い倒したいと思います！

それでは皆様楽しい創作ライフを…。