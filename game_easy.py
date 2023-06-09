import random, tmp_save
def game_easy(cnt, c_figure):                                                   #イージーゲーム内容処理関数
    win_or_lose = ["「当たり!!」", "「残念、はずれ」"]
    if cnt == 1:
        c_figure = random.randint(0,9)
        print("...コンピュータが数字を選びました。")
    else:
        pass
    y_figure = int(input("数字を選んでね。\n>>>"))
    if c_figure == y_figure:
        print("結果は", win_or_lose[0])
        print("あなたは", cnt, "回で当たりました。")
        tmp_save.kiroku[0] = cnt
        cnt = 1
        easy = 1
        return easy
    else:
        print("結果は", win_or_lose[1])
        cnt = cnt + 1
        if c_figure > y_figure:                                                 #ヒントの表示
            print("ヒント：コンピュータの数字の方が大きいです。")
        else:
            print("ヒント：コンピュータの数字の方が小さいです。")
        return game_easy(cnt, c_figure)