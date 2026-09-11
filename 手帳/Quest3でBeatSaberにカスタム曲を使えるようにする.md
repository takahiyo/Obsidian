---
notion-id: cd60e44150d046968205ccfc7a4596b2
URL: https://harusdia.hatenablog.com/entry/2023/11/13/012650
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - Quest3
  - ゲーム
---
# 具体的な流れ

1. Quest3で開発者モードを有効にする
	1. https://orentame.com/how-to-enable-developer-mode/
2. パソコンにSideQuestをインストールする
	1. 以降の作業の間は開発者モードのQuest3とWindowsは接続したままで良い
3. SideQuestで「**QuestAppVersionSwitcher**」を検索しインストールする
4. BeatSaberのバージョンを確認する
5. Quest3の提供元不明から**QuestAppVersionSwitcher**を**実行する**
	1. Tool＆Option　でログインする
	2. Downgrade　からBeatSaberのMOD対応版を探し、ダウンロードする
		1. MOD対応バージョンは1.28.0_4124311467
			1. 2024/01/22時点
	3. ダウンロードが終わったら、Install Versionsを実行する
	4. Step1として、現BeatSaberのアンインストールを求められるのでアンインストールする
	5. 画面に従いContinue、App Installと勧める
	6. インストールが終わったら実行し、足元でバージョンを確認する
		1. 以降、起動時に「更新する」といったメッセージが出るので押さないこと
			1. もし押した場合は、アプリを終了してから手順5に戻る
	7. BeatSaberを終了しておく
6. パソコンで、[QuestPatcherをダウンロード](https://github.com/Lauriethefish/QuestPatcher/releases/tag/2.6.1)・インストールする
7. QuestPatcherを実行する
	1. 画面に従い、Patchingを行う
	2. Modの有効・無効を切り替えられる一覧画面が出る
	3. [コアModをダウンロード](https://computerelite.github.io/tools/Beat_Saber/questmods.html)・インストールする
	4. 同様に必要なModを探してきてインストールし、有効化する
8. この時点でMod化できているはずだが多少時間がかかることがある
	1. パソコンとの接続をそのままにして、Mod化でBeatSaberが実行できることを確認した方が安心