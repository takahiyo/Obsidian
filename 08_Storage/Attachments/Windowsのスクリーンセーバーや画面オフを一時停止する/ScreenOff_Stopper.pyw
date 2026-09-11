from pystray import Icon, Menu, MenuItem
from PIL import Image
import ctypes
import sys
import os
import time

# グローバル変数で状態を保持
toggle_state = False
icon = None
lock_file = 'app.lock'

# アイコン画像の生成
def create_icon_image(color):
    return Image.new('RGB', (16, 16), color=color)

def set_thread_execution_state(state):
    """
    Windows API SetThreadExecutionState を使用して画面オフやスクリーンセーバーを防止/解除します。
    """
    ctypes.windll.kernel32.SetThreadExecutionState(state)

def toggle_screen_off(icon, item):
    """
    画面オフ/スクリーンセーバー防止の状態を切り替える関数。
    """
    global toggle_state
    toggle_state = not toggle_state

    if toggle_state:
        # 画面オフ防止を有効にする
        set_thread_execution_state(0x80000002)
        icon.icon = create_icon_image((255, 0, 0))  # 赤色アイコン
        icon.notify('画面オフ防止が有効になりました')
    else:
        # 通常の動作に戻す
        set_thread_execution_state(0x80000000)
        icon.icon = create_icon_image((0, 0, 255))  # 青色アイコン
        icon.notify('画面オフ防止が解除されました')

def exit_app(icon, item):
    """
    アプリケーションの終了処理。
    """
    # 通常の動作に戻す
    set_thread_execution_state(0x80000000)
    icon.stop()
    if os.path.exists(lock_file):
        os.remove(lock_file)
    sys.exit()

def check_existing_instance():
    """
    プロセスが既に実行されているか確認し、存在する場合は終了をトリガーする。
    """
    # シンプルなファイルベースのロックを使用して、他のインスタンスが実行中かを確認
    if os.path.exists(lock_file):
        # 他のインスタンスが実行中であれば終了
        sys.exit()
    else:
        # 実行中でない場合、ロックファイルを作成
        with open(lock_file, 'w') as f:
            f.write(str(os.getpid()))

def main():
    global icon
    check_existing_instance()

    # 初期アイコンを設定（画面オフ有効時は青色）
    image = create_icon_image((0, 0, 255))

    # メニューを設定
    menu = Menu(
        MenuItem('画面オフ防止の切り替え', toggle_screen_off),
        MenuItem('終了', exit_app)
    )

    # アイコンを作成してタスクトレイに常駐
    icon = Icon('ScreenOffToggle', image, menu=menu)
    icon.run()

if __name__ == "__main__":
    # ファイルの拡張子を .pyw にすることで、Windows環境でCUIのコンソールウィンドウを非表示にすることができます。
    main()
