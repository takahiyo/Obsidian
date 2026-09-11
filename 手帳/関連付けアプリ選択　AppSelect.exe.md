---
notion-id: 17d37ce628718000af4fcfc2d8839b11
更新されました: Invalid date
作成日時: Invalid date
ファイル&メディア:
  - "[[appselect.rar]]"
  - "[[08_Storage/Attachments/実行アプリ選択ダイアログ表示/AppSelect_Settings.json]]"
  - "[[08_Storage/Attachments/実行アプリ選択ダイアログ表示/appselect.pyw]]"
---
# 概要

- このアプリを経由してファイルを起動すると、パスを送るファイルを選べる
- 選択しなかった場合、4秒でダイアログは閉じる
- 空欄をShitを押しながらクリックすることで、実行ファイルを登録できる
	- exeと同じパスに「AppSelect_Settings.json」として設定は保存される

# exeファイル出力用コード

```jsx
pyinstaller --onefile --noconsole --add-data "AppSelect_Settings.json;." appselect.pyw
```

- 「appselect.pyw」のパスフォルダでCMDを開き実行する

# 何故か関連付けが正常に働かない

1. `.rar` ファイル拡張子とアプリケーションの関連付けを確認：
    
	```
	cmd
	コピーする編集する
	assoc .rar
	
	```
    
	出力が以下のようであることを確認：
    
	```
	コピーする編集する
	.rar=RarFile
	```
    
2. ファイルタイプ `RarFile` の動作を確認：
    
	```
	cmd
	コピーする編集する
	ftype RarFile
	
	```
    
	出力が以下のようであることを確認：
    
	```makefile
	makefile
	コピーする編集する
	RarFile="C:\Path\To\appselect.exe" "%1"
	```
    
3. 間違いがある場合、修正します：
    
	```
	cmd
	コピーする編集する
	assoc .rar=RarFile
	ftype RarFile="E:\Python\dist\appselect.exe" \"%1\"
	assoc .zip=ZipFile
	ftype ZipFile="E:\Python\dist\appselect.exe" \"%1\"
	```
    

# AppSelect.pywのコード

```jsx
import sys
import os
import subprocess
import tkinter as tk
import json
from tkinter import filedialog
from tkinter import simpledialog

def log_debug_info(message):
    # アプリへのパス受け渡しログ出力を無効化
    pass

def save_settings(apps):
    with open(settings_file_path, 'w', encoding='utf-8') as file:
        json.dump(apps, file, ensure_ascii=False, indent=4)
        log_debug_info(f"Settings saved: {apps}")

def load_settings():
    if not os.path.exists(settings_file_path):
        # 初期値で設定ファイルを作成
        default_settings = [{"path": None, "name": f"アプリ {i+1}"} for i in range(9)]
        save_settings(default_settings)
        log_debug_info("Default settings created.")
        return default_settings
    try:
        with open(settings_file_path, 'r', encoding='utf-8') as file:
            settings = json.load(file)
            log_debug_info(f"Settings loaded: {settings}")
            return settings
    except (json.JSONDecodeError, OSError) as e:
        log_debug_info(f"Error loading settings: {e}")
        default_settings = [{"path": None, "name": f"アプリ {i+1}"} for i in range(9)]
        save_settings(default_settings)
        return default_settings

def select_app(index):
    pause_timer()
    app_path = filedialog.askopenfilename()
    if app_path:
        apps[index]["path"] = app_path
        apps[index]["name"] = os.path.basename(app_path)
        buttons[index].config(text=apps[index]["name"], command=lambda p=app_path: open_app(p))
        save_settings(apps)
        log_debug_info(f"App selected: index={index}, path={app_path}")
    resume_timer()

def change_button_name(index):
    pause_timer()
    new_name = simpledialog.askstring("ボタン名の変更", "新しいボタン名を入力してください:")
    if new_name:
        apps[index]["name"] = new_name
        buttons[index].config(text=new_name)
        save_settings(apps)
        log_debug_info(f"Button name changed: index={index}, new_name={new_name}")
    resume_timer()

def open_app(app_path):
    log_debug_info(f"Attempting to open app: {app_path}")
    if app_path and os.path.exists(app_path):
        try:
            # ファイルパスを正規化し、余計な引用符を削除
            resolved_file_path = os.path.normpath(file_path.strip('"'))
            log_debug_info(f"Resolved file path before validation: {resolved_file_path}")

            # ファイルパスが正しく構成されているかチェック
            if not os.path.isfile(resolved_file_path):
                error_message = f"Resolved file path is not valid: {resolved_file_path}"
                log_debug_info(error_message)
                tk.messagebox.showerror("エラー", error_message)
                return

            # コマンドと引数をリスト形式で渡す
            command = [app_path, resolved_file_path]
            log_debug_info(f"Executing command: {command}")
            subprocess.Popen(command, shell=False)
            root.destroy()
        except Exception as e:
            error_message = f"アプリの実行中にエラーが発生しました: {e}"
            tk.messagebox.showerror("エラー", error_message)
            log_debug_info(error_message)
    else:
        error_message = "アプリが見つかりません！"
        tk.messagebox.showerror("エラー", error_message)
        log_debug_info(error_message)

def pause_timer():
    global timer_id
    if timer_id:
        root.after_cancel(timer_id)
        timer_id = None

def resume_timer():
    global timer_id
    timer_id = root.after(4000, root.destroy)  # タイマー再開

# JSON パスを定義
if getattr(sys, 'frozen', False):
    # .exe で動作している場合
    settings_file_path = os.path.join(os.path.dirname(sys.executable), 'AppSelect_Settings.json')
else:
    # Python スクリプトで動作している場合
    settings_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'AppSelect_Settings.json')

# sys.argv の処理を改善
if len(sys.argv) > 1:
    file_path = " ".join(sys.argv[1:]).strip('"')  # 複数の引数を結合して処理
else:
    file_path = ""
log_debug_info(f"Initial file_path after processing: {file_path}")

apps = load_settings()

root = tk.Tk()
root.withdraw()

main_dialog = tk.Toplevel(root)
main_dialog.title("ランチャー")

buttons = []
for i in range(9):  # 9つのボタンを作成
    app = apps[i]
    button = tk.Button(main_dialog, text=app["name"], command=lambda p=app["path"]: open_app(p))
    button.grid(row=i // 3 + 1, column=i % 3)
    buttons.append(button)

def set_dialog_position(event):
    x, y = main_dialog.winfo_pointerx(), main_dialog.winfo_pointery()
    main_dialog.geometry(f"+{x}+{y}")

def handle_button_click(event):
    index = buttons.index(event.widget)
    if event.state & 1:  # Shiftキーが押されているかチェック
        select_app(index)
    elif event.state & 4:  # Ctrlキーが押されているかチェック
        change_button_name(index)

main_dialog.bind('<Visibility>', set_dialog_position)
main_dialog.bind('<Button-1>', handle_button_click)

timer_id = root.after(4000, root.destroy)  # タイマー開始

root.mainloop()
```