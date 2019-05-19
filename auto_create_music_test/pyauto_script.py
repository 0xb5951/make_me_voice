##PyAutoGUIのモジュール
import pyautogui

##プロセスを制御するためにOS周りのモジュール
import sys
import time


# 画面サイズの取得
screen_x, screen_y = pyautogui.size()


if __name__ == "__main__":
    time.sleep(5)

    # 現在のマウス位置の取得
    tmp_cur_x, tmp_cur_y = pyautogui.position()  # 現在のマウスのxとy座標を返す
    print(tmp_cur_x, tmp_cur_y)


    # もし画面内カーソルにあればTrueを返す
    cursor_flag = pyautogui.onScreen(tmp_cur_x, tmp_cur_y)
    print(cursor_flag)

    # 現在のマウスカーソルの座標から(xOffset,yOffset)だけtime秒で移動する．
    pyautogui.moveRel(2, 2, 2)

    # 現在のマウス位置の取得
    tmp_cur_x, tmp_cur_y = pyautogui.position()  # 現在のマウスのxとy座標を返す
    print(tmp_cur_x, tmp_cur_y)

    # その場所でマウスを左クリックする
    pyautogui.click(tmp_cur_x, tmp_cur_y)
