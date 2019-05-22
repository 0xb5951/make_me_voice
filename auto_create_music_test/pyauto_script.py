##PyAutoGUIのモジュール
import pyautogui

##プロセスを制御するためにOS周りのモジュール
import sys
import time
import json
import random


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
    tuto_path = "../../../AppData/Local/Programs/Python/Python36/Lib/site-packages/FoxDot/demo/16_auto_create_music.py"

    # 再生しているファイルをリストで読み込む
    with open(tuto_path, 'r', encoding="utf-8") as mf:
        mf_lines = mf.readlines()
        print(mf_lines)

    # 音源コードを読み込む
    with open("sound_source.json", 'r') as f:
        source_data = json.load(f)  # JSON形式で読み込む

    while(1):
        time.sleep(30)

        # 各音源に対して更新ループを回す
        for index, source in enumerate(mf_lines, start=0):
            print(index, source)
            # 音源を更新するときの処理
            if random.random() > 0.7:
                # 楽器の変数を取得
                ms_vr = source.split('>>')[0]
                print(ms_vr)
                if "Clock.bpm" in ms_vr:
                    continue
                ms_count = len(source_data[ms_vr])
                print(ms_count)

                # ランダムな要素を選択する
                rp = random.randint(0, ms_count-1)
                print(rp)
                # 更新するコード
                mf_lines[index] = ms_vr + ">>" + source_data[ms_vr][rp] + "\n"
                print("更新後のコード")
                print(mf_lines)

        # 更新したファイルを結合して、ソースにする
        output_code = ''.join(mf_lines)
        # output_code += "\nClock.bpm = 140"
        print("出力するコード")
        print(output_code)

        # 実際にコードを書き込む
        with open(tuto_path, mode='w') as f:
            f.write(output_code)

        # ファイルを更新する
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

        # tutorialタブの位置に戻す
        pyautogui.moveRel(0, -420, 2)
