import rule
def watch_rule():                                                               #ルール選択関数
    print("どの難易度のルールを見る？")
    difficlt_rule = int(input("1.イージー 2.ノーマル 3.ハード\n>>>"))
    rule.rule(difficlt_rule)
