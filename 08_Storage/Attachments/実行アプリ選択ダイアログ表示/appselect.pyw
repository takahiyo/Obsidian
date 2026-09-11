import sys
import os
import subprocess
import tkinter as tk
import json
from tkinter import filedialog
from tkinter import simpledialog

def save_settings(apps):
    with open(settings_file_path, 'w') as file:
        json.dump(apps, file)

def load_settings():
    if not os.path.exists(settings_file_path):
        save_settings([{"path": None, "name": f"アプリ {i+1}"} for i in range(9)])  # 初期値で設定ファイルを作成
    with open(settings_file_path, 'r') as file:
        return json.load(file)

def select_app(index):
    pause_timer()
    app_path = filedialog.askopenfilename()
    apps[index]["path"] = app_path
    apps[index]["name"] = os.path.basename(app_path)
    buttons[index].config(text=apps[index]["name"], command=lambda p=app_path: open_app(p))
    save_settings(apps)
    resume_timer()

def change_button_name(index):
    pause_timer()
    new_name = simpledialog.askstring("ボタン名の変更", "新しいボタン名を入力してください:")
    if new_name:
        apps[index]["name"] = new_name
        buttons[index].config(text=new_name)
        save_settings(apps)
    resume_timer()

def open_app(app_path):
    normalized_file_path = os.path.normpath(file_path)
    subprocess.Popen([app_path, normalized_file_path])
    root.destroy()

def pause_timer():
    global timer_id
    if timer_id:
        root.after_cancel(timer_id)
        timer_id = None

def resume_timer():
    global timer_id
    timer_id = root.after(4000, root.destroy)  # タイマー再開

file_path = sys.argv[1]
settings_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'AppSelect_Settings.json')
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
