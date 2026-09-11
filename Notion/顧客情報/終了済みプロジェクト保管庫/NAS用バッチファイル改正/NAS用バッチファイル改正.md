---
notion-id: 50066567-a0de-42a0-9138-afa1e738b05d
base: "[[終了済みプロジェクト保管庫.base]]"
親プロジェクト: []
サブアイテム: []
親アイテム: []
サブプロジェクト: []
オーナー:
  - 66100a62-9433-4e55-ac9b-3527ba280718
営業段階: 納品・アフター
ステータス: 未着手
補足: ""
担当者: []
日付: 2023-11-06 to 2023-12-28
次のプロジェクトを保留中：: []
次のプロジェクトにより保留中：: []
---
# 履歴

> [!note]+ 2024/03/29
> ```javascript
> @echo off
> setlocal enabledelayedexpansion
> 
> :: 現在の日付をYYYYMMDD形式で取得します
> for /f "tokens=2 delims==" %%i in ('wmic OS Get localdatetime /value') do set "currentDateTime=%%i"
> set "backupDate=!currentDateTime:~0,8!"
> 
> :: 変数の設定
> set "source=\\192.168.1.250\Share"
> set "baseDestination=\\192.168.1.250\WeeklyCopy_Share"
> set "logDir=\\192.168.1.250\WeeklyCopy_Share\Logs"
> set "destination=!baseDestination!\!backupDate!"
> set "logFile=!logDir!\backup_!backupDate!.log"
> 
> :: バックアップとログディレクトリが存在しない場合、ディレクトリを作成します
> if not exist "!destination!" mkdir "!destination!"
> if not exist "!logDir!" mkdir "!logDir!"
> 
> :: バックアップを実行します
> robocopy "!source!" "!destination!" /MIR /LOG:"!logFile!"
> 
> :: 古いバックアップを削除します（最新4つのバックアップのみを保持）
> for /f "skip=4 eol=: delims=" %%i in ('dir "!baseDestination!" /b /ad /o-d') do (
>     rmdir /s /q "!baseDestination!\%%i"
> )
> 
> endlocal
> ```
> 
> ```javascript
> @echo off
> setlocal
> 
> :: 変数の設定
> set "source=G:\マイドライブ\エンカウント"
> set "destination=\\192.168.1.250\backup"
> 
> :: バックアップの実行
> robocopy "%source%" "%destination%" /MIR
> 
> endlocal
> 
> ```
> 
> ```javascript
> @echo off
> setlocal enabledelayedexpansion
> 
> :: 現在の日付をYYYYMMDD形式で取得
> for /f "tokens=2 delims==" %%i in ('wmic OS Get localdatetime /value') do set "currentDateTime=%%i"
> set "backupDate=!currentDateTime:~0,8!"
> 
> :: 変数の設定
> set "source=\\192.168.1.250\backup"
> set "baseDestination=\\192.168.1.250\WeeklyCopy_Backup"
> set "destination=!baseDestination!\!backupDate!"
> 
> :: バックアップ先のディレクトリが存在しなければ作成
> if not exist "!destination!" mkdir "!destination!"
> 
> :: バックアップの実行
> robocopy "!source!" "!destination!" /MIR
> 
> :: 最新8つのバックアップを保持し、9つ目を作成したら最も古いものを削除
> set "count=0"
> for /f "delims=" %%a in ('dir "!baseDestination!" /b /ad /o-d') do (
>     set /a count+=1
>     if !count! gtr 8 (
>         echo 古いバックアップを削除しています: %%a
>         rmdir /s /q "!baseDestination!\%%a"
>     )
> )
> 
> endlocal
> 
> ```

> [!note]+ メール：武内さま
> NTT西日本ビジネスフロント 平八重さま
> 
> いつもお世話になっております。
> 
> エンカウントの武内です。
> 
> 今日はありがとうございました。
> 
> 事務所で拝見していました。
> 
> 割り当てがうまくいってないのと、
> 
> 削除がエラー出てるな と傍観しておりました。
> 
> 今回はバッファローへのコピーの検証と実行と思っていましたら、削除の段階を進めていて、少し驚きました。
> 
> NAS内の「WeeklyCopy_Share」内に1週間分。
> 
> 外付けHDD（バッファロー）内に4週間分残すことを想定しています。
> 
> 次の手段としてミラーリングは良いのですが、
> 
> ミラーリング中にトラブった時にデータに不具合が残るのが怖いので、
> 
> ①「WeeklyCopy_Share」をバッファロー内へコピーして、
> 
> ②「WeeklyCopy_Share」を「Share」とミラーリングして更新、
> 
> ③バッファロー内の4週間分を超えるものを削除
> 
> なら、ミラーリングでいけるかもですね。
> 
> ご検討いただけたらと思います。
> 
> お手数をおかけしますが、
> 
> よろしくお願いします。
> 
> 2023年12月18日(月) 13:47 平八重 貴裕 <
> 
> [takahiro.hirahae.gw@west.ntt.co.jp](mailto:takahiro.hirahae.gw@west.ntt.co.jp)
> 
> >:

[[ファイル操作用コード作成用]]


![[Untitled 12.webp]]

![[Untitled 13.webp]]


![[Untitled 14.webp]]

11:33

set ospro=\\192.168.1.250 set datename=%date:~0,4%%date:~5,2%%date:~8,2% mkdir %ospro%\DailyCopy_Backup\%datename% robocopy %ospro%\backup\ %ospro%\DailyCopy_Backup\%datename%\ *.* /mir /r:3 /w:5 /copy:dt >\\192.168.1.250\DailyCopy_Backup\%datename%.txt @rem デイリーコピーフォルダ内から30日以上経過したフォルダを削除する forfiles /p "y:\" /D -6 /c "cmd /c IF @isdir==TRUE rmdir /S /Q @file"