import menu, game_difficult, game_easy, game_nomal, game_hard, watch_rule, tmp_save
if __name__ == '__main__':
                                                                   #初期設定、初期化
    
    cnt = 1
    easy = 0
    nomal = 0
    c_figure = 0

    print("数字当てゲームへようこそ!!")                                             #メインの処理、最初の挨拶
    print("**** 入力は数字のみでお願い致します。****")

    while True:                                                                        #while文でメニューを表示
        menu_mode = menu.menu()
        if menu_mode == 1:                                                          #ゲームモードの選択
            difficult = game_difficult.game_difficult()
            if difficult == 1:
                easy = game_easy.game_easy(cnt, c_figure)
            elif difficult == 2:
                nomal = game_nomal.game_nomal(cnt, c_figure)
            elif difficult == 3:
                game_hard.game_hard(cnt, easy, nomal)
            else:
                pass 
        elif menu_mode == 2:                                                        #ルールの選択、表示
            watch_rule.watch_rule()
        elif menu_mode == 3:                                                        #前回、遊んだ時の最短クリア回数（ゲームモード別）
            print("前回の記録[イージー, ノーマル, ハード] =",tmp_save.kiroku)
        elif menu_mode == 4:                                                        #ゲームの終了
            break

    if (tmp_save.kiroku[0] > 0) and (tmp_save.kiroku[1] > 0) and (tmp_save.kiroku[2] > 0):                     #すべてのゲームモードをクリアした時の処理
        print("Congratulation!! すべてクリアおめでとう!!")
    else:
        pass
    print("Thank you for playing !! また、遊んでね!!")                             #最後の挨拶
