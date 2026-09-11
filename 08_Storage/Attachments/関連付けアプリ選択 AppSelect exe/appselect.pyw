import sys
import os
import subprocess
import tkinter as tk
import json
from tkinter import filedialog
from tkinter import simpledialog

def save_settings(apps):
    with open(settings_file_path, 'w', encoding='utf-8') as file:
        json.dump(apps, file, ensure_ascii=False, indent=4)

def load_settings():
    if not os.path.exists(settings_file_path):
        # 初期値で設定ファイルを作成
        save_settings([{"path": None, "name": f"\u30a2\u30d7\u30ea {i+1}"} for i in range(9)])
    try:
        with open(settings_file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        # ファイルが壊れている場合の対処
        save_settings([{"path": None, "name": f"\u30a2\u30d7\u30ea {i+1}"} for i in range(9)])
        return load_settings()

def select_app(index):
    pause_timer()
    app_path = filedialog.askopenfilename()
    if app_path:
        apps[index]["path"] = app_path
        apps[index]["name"] = os.path.basename(app_path)
        buttons[index].config(text=apps[index]["name"], command=lambda p=app_path: open_app(p))
        save_settings(apps)
    resume_timer()

def change_button_name(index):
    pause_timer()
    new_name = simpledialog.askstring("\u30dc\u30bf\u30f3\u540d\u306e\u5909\u66f4", "\u65b0\u3057\u3044\u30dc\u30bf\u30f3\u540d\u3092\u5165\u529b\u3057\u3066\u304f\u3060\u3055\u3044:")
    if new_name:
        apps[index]["name"] = new_name
        buttons[index].config(text=new_name)
        save_settings(apps)
    resume_timer()

def open_app(app_path):
    if app_path and os.path.exists(app_path):
        normalized_file_path = os.path.normpath(file_path)
        subprocess.Popen([app_path, normalized_file_path])
        root.destroy()
    else:
        tk.messagebox.showerror("\u30a8\u30e9\u30fc", "\u30a2\u30d7\u30ea\u304c\u898b\u3064\u304b\u308a\u307e\u305b\u3093\uff01")

def pause_timer():
    global timer_id
    if timer_id:
        root.after_cancel(timer_id)
        timer_id = None

def resume_timer():
    global timer_id
    timer_id = root.after(4000, root.destroy)  # \u30bf\u30a4\u30de\u30fc\u518d\u958b

# JSON \u30d1\u30b9\u3092\u5b9a\u7fa9
if getattr(sys, 'frozen', False):
    # .exe \u3067\u52d5\u4f5c\u3057\u3066\u3044\u308b\u5834\u5408
    settings_file_path = os.path.join(os.path.dirname(sys.executable), 'AppSelect_Settings.json')
else:
    # Python \u30b9\u30af\u30ea\u30d7\u30c8\u3067\u52d5\u4f5c\u3057\u3066\u3044\u308b\u5834\u5408
    settings_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'AppSelect_Settings.json')

file_path = sys.argv[1] if len(sys.argv) > 1 else ""
apps = load_settings()

root = tk.Tk()
root.withdraw()

main_dialog = tk.Toplevel(root)
main_dialog.title("\u30e9\u30f3\u30c1\u30e3\u30fc")

buttons = []
for i in range(9):  # 9\u3064\u306e\u30dc\u30bf\u30f3\u3092\u4f5c\u6210
    app = apps[i]
    button = tk.Button(main_dialog, text=app["name"], command=lambda p=app["path"]: open_app(p))
    button.grid(row=i // 3 + 1, column=i % 3)
    buttons.append(button)

def set_dialog_position(event):
    x, y = main_dialog.winfo_pointerx(), main_dialog.winfo_pointery()
    main_dialog.geometry(f"+{x}+{y}")

def handle_button_click(event):
    index = buttons.index(event.widget)
    if event.state & 1:  # Shift\u30ad\u30fc\u304c\u62bc\u3055\u308c\u3066\u3044\u308b\u304b\u30c1\u30a7\u30c3\u30af
        select_app(index)
    elif event.state & 4:  # Ctrl\u30ad\u30fc\u304c\u62bc\u3055\u308c\u3066\u3044\u308b\u304b\u30c1\u30a7\u30c3\u30af
        change_button_name(index)

main_dialog.bind('<Visibility>', set_dialog_position)
main_dialog.bind('<Button-1>', handle_button_click)

timer_id = root.after(4000, root.destroy)  # \u30bf\u30a4\u30de\u30fc\u958b\u59cb

root.mainloop()
