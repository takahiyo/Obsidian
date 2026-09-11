---
notion-id: 15e37ce6287181dcaad7db8364128607
URL: https://huggingface.co/aipicasso/emi-3
更新されました: Invalid date
作成日時: Invalid date
---
[![](https://huggingface.co/aipicasso/emi-3/resolve/main/eyecatch.jpg)](https://huggingface.co/aipicasso/emi-3/resolve/main/eyecatch.jpg)

# はじめに

Emi 3 (Ethereal master of illustration 3) は、 オプトアウト済みモデルStable Diffusion 3.5 Largeをベースに AI Picasso社が開発したAIアートに特化した画像生成AIです。 このモデルの特徴として、Danbooruなどにある無断転載画像を追加に学習していないことがあげられます。

# 使い方

本格的に利用する人は[ここ](https://huggingface.co/aipicasso/emi-3/blob/main/emi3.safetensors)からモデルをダウンロードできます。 簡易的に[ここ](https://huggingface.co/spaces/aipicasso/emi-3)からデモを利用することができますが、 出来がイマイチなので、ローカルで使うことをおすすめします。

# モデルの出力向上について

- プロンプトとして約200単語の自然言語を使うことができます。また、AnimagineXLと同じプロンプトを使うこともできます。
- ChatGPTを用いてプロンプトを洗練すると、自分の枠を超えた作品に出会えます。

# シンプルな作品例

大規模言語モデルでプロンプトの作成を補助しています。

[![](https://huggingface.co/aipicasso/emi-3/resolve/main/sample1.jpg)](https://huggingface.co/aipicasso/emi-3/resolve/main/sample1.jpg)

```
positive: 1girl with the speech bubble saying "Happy Holidays!", upper body, sivler short hair, blue eyes, warm wear, outdoor, snow
negative: photo
```

[![](https://huggingface.co/aipicasso/emi-3/resolve/main/sample2.jpg)](https://huggingface.co/aipicasso/emi-3/resolve/main/sample2.jpg)

```
positive: manga style, monochrome, an aerial view of Tokyo's cityscape. The scene captures the sunset view with dense clusters of modern skyscrapers in Shinjuku and Shibuya. The intricate network of illuminated streets and highways is visible, showcasing the unique landscape where traditional low-rise buildings coexist with contemporary architecture. Mount Fuji's silhouette can be seen in the distant background, while soft evening lights from office buildings and streets envelop the entire city. The image should be ultra high-resolution and photorealistic, composed as if shot with a wide-angle lens from approximately 1,000 feet altitude.
negative:
```

[![](https://huggingface.co/aipicasso/emi-3/resolve/main/sample3.jpg)](https://huggingface.co/aipicasso/emi-3/resolve/main/sample3.jpg)

```
positive: Full body shot of a mysterious teenage boy in anime style, with wild spiky red and orange hair that seems to flicker like flames. He's wearing a black sleeveless top with red accents and dark baggy pants with flame patterns along the hem. His amber eyes glow with inner fire, and wisps of flame dance around his outstretched hands. His pose is dynamic, suggesting movement, with one hand raised commanding the fire. The lighting is dramatic, with the flames he controls casting warm orange light across his determined expression. The art style is clean and sharp, reminiscent of modern action anime. Background shows subtle smoke effects and ember particles floating in the air."
negative: photo, bad hands, bad anatomy, low quality
```

# 法律について

本モデルは日本にて作成されました。したがって、日本の法律が適用されます。 本モデルの学習は、著作権法第30条の4に基づき、合法であると主張します。 また、本モデルの配布については、著作権法や刑法175条に照らしてみても、 正犯や幇助犯にも該当しないと主張します。詳しくは柿沼弁護士の[見解](https://twitter.com/tka0120/status/1601483633436393473?s=20&t=yvM9EX0Em-_7lh8NJln3IQ)を御覧ください。 ただし、ライセンスにもある通り、本モデルの生成物は各種法令に従って取り扱って下さい。

# 連絡先

support@aipicasso.app

以下、一般的なモデルカードの日本語訳です。

## モデル詳細

- **モデルタイプ:** フローベースの text-to-image 生成モデル
- **言語:** 日本語
- **ライセンス:** [Stabilityai AI Community](https://huggingface.co/aipicasso/emi-3/blob/main/LICENSE.md)
- **モデルの説明:** このモデルはプロンプトに応じて適切な画像を生成することができます。アルゴリズムは [Rectified Flow Transformer](https://stability.ai/news/stable-diffusion-3-research-paper) と [OpenCLIP-ViT/G](https://github.com/mlfoundations/open_clip)、[CLIP-L](https://github.com/openai/CLIP) 、[T5](https://arxiv.org/abs/1910.10683) です。
- **補足:**

## モデルの使用例

Stable Diffusion 3.5 Largeと同じ使い方です。 たくさんの方法がありますが、2つのパターンを提供します。

- ComfyUI (おすすめ)
- Diffusers

### ComfyUIの場合 (おすすめ)

Stable Diffusion 3.5 Large の使い方と同じく、safetensors形式のモデルファイルを使ってください。 詳しいインストール方法は、[こちらの記事](https://tensorflow.classcat.com/2024/10/23/sd35-large-colab-comfyui/)を参照してください。

### Diffusersの場合

[🤗's Diffusers library](https://github.com/huggingface/diffusers) を使ってください。

まずは、以下のスクリプトを実行し、ライブラリをいれてください。

```
pip install -U diffusers
```

次のスクリプトを実行し、画像を生成してください。

```
import torch
from diffusers import StableDiffusion3Pipeline

pipe = StableDiffusion3Pipeline.from_pretrained("aipicasso/emi-3", torch_dtype=torch.bfloat16)
pipe = pipe.to("cuda")

image = pipe(
    "anime style, 1girl, looking at viewer, serene expression, gentle smile, multicolored hair, rainbow gradient hair, wavy long hair, heterochromia, purple left eye, blue right eye, pastel color scheme, magical girl aesthetic, white text overlay \"Emi 3\", centered text, modern typography, ethereal lighting, soft glow, fantasy atmosphere, rainbow gradient background, dreamy atmosphere, sparkles, light particles, magical effects, depth of field, bokeh effect",
    num_inference_steps=40,
    guidance_scale=4.5,
).images[0]
image.save("emi3.png")
```

複雑な操作は[デモのソースコード](https://huggingface.co/spaces/aipicasso/emi-3/blob/main/app.py)を参考にしてください。

### 想定される用途

- イラストや漫画、アニメの作画補助
	- 商用・非商用は問わない
- 依頼の際のクリエイターとのコミュニケーション
- 画像生成サービスの商用提供
	- 生成物の取り扱いには注意して使ってください。
- 自己表現
	- このAIを使い、「あなた」らしさを発信すること
- 研究開発
	- ファインチューニング（追加学習とも）
		- LoRA など
	- 他のモデルとのマージ
	- 本モデルの性能をFIDなどで調べること
- 教育
	- 美大生や専門学校生の卒業制作
	- 大学生の卒業論文や課題制作
	- 先生が画像生成AIの現状を伝えること
- Hugging Face の Community にかいてある用途
	- 日本語か英語で質問してください

### 想定されない用途

- 物事を事実として表現するようなこと
- 先生を困らせるようなこと
- その他、創作業界に悪影響を及ぼすこと

# 使用してはいけない用途や悪意のある用途

- マネー・ロンダリングに用いないでください
- デジタル贋作 ([Digital Forgery](https://arxiv.org/abs/2212.03860)) は公開しないでください（著作権法に違反するおそれ）
- 他人の作品を無断でImage-to-Imageしないでください（著作権法に違反するおそれ）
- わいせつ物を頒布しないでください (刑法175条に違反するおそれ）
	- いわゆる業界のマナーを守らないようなこと
- 事実に基づかないことを事実のように語らないようにしてください（威力業務妨害罪が適用されるおそれ）
	- フェイクニュース

## モデルの限界やバイアス

### モデルの限界

- 人間の手がきれいに生成することが難しいです。

### バイアス

- 日本のイラスト風の画像を生成していることに向いていますが、写真のような画像を生成することには向いていません。

## 学習

**学習データ**

- Stable Diffusion と同様のデータセットからDanbooruの無断転載画像を取り除いて手動で集めた約3000枚の画像
- Stable Diffusion と同様のデータセットからDanbooruの無断転載画像を取り除いて自動で集めた約40万枚の画像
- **学習プロセス**
- **ハードウェア:** A6000

## 評価結果

第三者による評価を求めています。

## 環境への影響

- **ハードウェアタイプ:** A6000
- **使用時間（単位は時間）:** 500
- **学習した場所:** 日本

## 参考文献

```
@misc{esser2024scalingrectifiedflowtransformers,
      title={Scaling Rectified Flow Transformers for High-Resolution Image Synthesis},
      author={Patrick Esser and Sumith Kulal and Andreas Blattmann and Rahim Entezari and Jonas Müller and Harry Saini and Yam Levi and Dominik Lorenz and Axel Sauer and Frederic Boesel and Dustin Podell and Tim Dockhorn and Zion English and Kyle Lacey and Alex Goodwin and Yannik Marek and Robin Rombach},
      year={2024},
      eprint={2403.03206},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2403.03206},
}
```