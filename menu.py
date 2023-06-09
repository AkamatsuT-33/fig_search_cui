def menu():                                                                     #メニュー関数
    print("\nメニューを選んでね。")
    try:
        menu = int(input("1.ゲームを始める 2.ルール 3.記録 4.終了\n>>>"))
        return menu
    except:
        print('数字で入力してください！')

    