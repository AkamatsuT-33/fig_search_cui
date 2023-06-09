import random, tmp_save
def game_nomal(cnt, c_figure):                                                  #ノーマルゲーム内容処理関数
    win_or_lose = ["「当たり!!」", "「残念、はずれ」"]
    if cnt == 1:
        c_figure = random.randint(0,9)
        print("...コンピュータが数字を選びました")
    else:
        pass
    y_figure = int(input("数字を選んでね。\n>>>"))
    if c_figure == y_figure:
        print("結果は", win_or_lose[0])
        print("あなたは", cnt, "回で当たりました。")
        tmp_save.kiroku[1] = cnt
        cnt = 1
        nomal = 1
        return nomal
    else:
        print("結果は", win_or_lose[1])
        cnt = cnt + 1
        return game_nomal(cnt, c_figure)