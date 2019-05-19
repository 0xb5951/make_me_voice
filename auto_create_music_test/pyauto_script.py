##PyAutoGUIのモジュール
import pyautogui

##プロセスを制御するためにOS周りのモジュール
import sys
import time


# 画面サイズの取得
screen_x, screen_y = pyautogui.size()

# その場所をクリック
def click_this_point():
    # 現在のマウス位置の取得
    tmp_cur_x, tmp_cur_y = pyautogui.position()  # 現在のマウスのxとy座標を返す
    print(tmp_cur_x, tmp_cur_y)
    # その場所でマウスを左クリックする
    pyautogui.click(tmp_cur_x, tmp_cur_y)

if __name__ == "__main__":
    time.sleep(10)

    click_this_point()

    # もし画面内カーソルにあればTrueを返す
    # cursor_flag = pyautogui.onScreen(tmp_cur_x, tmp_cur_y)
    # print(cursor_flag)

    # 現在のマウスカーソルの座標から(xOffset,yOffset)だけtime秒で移動する．
    pyautogui.moveRel(0, 420, 2)

    # ファイルを選択。
    click_this_point()

    # 全選択。
    pyautogui.hotkey('ctrl', 'a')

    # 音源を再生
    pyautogui.hotkey('ctrl', 'enter')

