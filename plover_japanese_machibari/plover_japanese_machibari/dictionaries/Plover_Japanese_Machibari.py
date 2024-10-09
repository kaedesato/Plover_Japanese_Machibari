#pythonの基本らしいけど、なんか各行文字列の最初の空白（インデント）によってコードの内容が変化するみたいだよ
#改変するときは気をつけてね（100敗）

#正規表現(Regex)を有効化すると宣言するよ
import re

#打鍵が続けられる長さを指定するよ (Plover Python dictionary)
LONGEST_KEY = 1

#おまじない　自分もよくわかってないよ
def lookup(key):
    assert len(key) <= LONGEST_KEY
    #keyを0にしないとこのコードはPloverで動かないらしいよ　Plover外で確認するときはこの数字を入力する文字の数以上にしたら動いた記憶があるよ
    stroke = key[0]

#ストロークが*か*-*か#のときにKeyErrorを出すよ    
    if stroke == "*" or stroke == "*-*" or stroke == "#":
        raise KeyError

    #打鍵されたキーを正規表現で見て、グループ化するよ
    regex = re.compile(r"(\*?)(S?T?K?H?)(I?A?O?)(k?n?t?h?)(\-?#?)(\*?)(S?T?K?H?)(I?A?O?)(k?n?t?h?)")
    regex_groups = re.search(regex, stroke)

    #グループ化したキーの呼び方を決めてるよ、グループは1から始まるよ
    LeftAsterisk = regex_groups.group(1)
    LeftConsonant = regex_groups.group(2)
    LeftVowel = regex_groups.group(3)
    LeftADkana = regex_groups.group(4)
    MiddleHyphen = regex_groups.group(5)
    RightAsterisk = regex_groups.group(6)
    RightConsonant = regex_groups.group(7)
    RightVowel = regex_groups.group(8)
    RightADkana = regex_groups.group(9)

    #↓のprintって書いてあるやつは、デバッグ用のコンソールに表示されるよ
    print("LeftAsterisk\tLeftConsonant\tLeftVowel\tLeftADkana")
    print(LeftAsterisk + "\t\t" + LeftConsonant + "\t\t" + LeftVowel + "\t\t" + LeftADkana)

    print("RightAsterisk\tRightConsonant\tRightVowel\tRightADkana")
    print(RightAsterisk + "\t\t" + RightConsonant + "\t\t" + RightVowel + "\t\t" + RightADkana)

    #return

    #子音のリストを作るよ　「あ　い　う　え　お　ゃ　ゅ　ょ」
    Consonantlist = {
    "": ["あ","い","","え","お","や","ゆ","よ"],
    "K": ["か","き","く","け","こ","きゃ","きゅ","きょ"],
    "S": ["さ","し","す","せ","そ","しゃ","しゅ","しょ"],
    "T": ["た","ち","つ","て","と","ちゃ","ちゅ","ちょ"],
    "TH": ["な","に","ぬ","ね","の","にゃ","にゅ","にょ"],
    "H": ["は","ひ","ふ","へ","ほ","ひゃ","ひゅ","ひょ"],
    "ST": ["ま","み","む","め","も","みゃ","みゅ","みょ"],
    "SH": ["ら","り","る","れ","ろ","りゃ","りゅ","りょ"],
    "KH": ["わ","","う","","を","","",""],
    "SK": ["が","ぎ","ぐ","げ","ご","ぎゃ","ぎゅ","ぎょ"],
    "STK": ["ざ","じ","ず","ぜ","ぞ","じゃ","じゅ","じょ"],
    "TK": ["だ","ぢ","づ","で","ど","でぃ","でゅ","でぇ"],
    "SKH": ["ば","び","ぶ","べ","ぼ","びゃ","びゅ","びょ"],
    "STH": ["ぱ","ぴ","ぷ","ぺ","ぽ","ぴゃ","ぴゅ","ぴょ"],
    "TKH": ["ぁ","ぃ","ぅ","ぇ","ぉ","ゃ","ゅ","ょ"],
    "STKH": ["","","","","","","",""]
    }
    result = ""


    #左の母音を見るよ　ちなみに==は比較するための記号だよ
    #イコールがただ単に倍になっただけじゃないので注意！！
    if LeftVowel == "A":
        resultL = Consonantlist[LeftConsonant][0]
    elif LeftVowel == "I":
        resultL = Consonantlist[LeftConsonant][1]
    elif LeftVowel == "":
        resultL = Consonantlist[LeftConsonant][2]
    elif LeftVowel == "AO":
        resultL = Consonantlist[LeftConsonant][3]
    elif LeftVowel == "O":
        resultL = Consonantlist[LeftConsonant][4]
    elif LeftVowel == "IA":
        resultL = Consonantlist[LeftConsonant][5]
    elif LeftVowel == "IAO":
        resultL = Consonantlist[LeftConsonant][6]
    elif LeftVowel == "IO":
        resultL = Consonantlist[LeftConsonant][7]
    else :
        raise KeyError

    #右の母音を見るよ
    if RightVowel == "A":
        resultR = Consonantlist[RightConsonant][0]
    elif RightVowel == "I":
        resultR = Consonantlist[RightConsonant][1]
    elif RightVowel == "":
        resultR = Consonantlist[RightConsonant][2]
    elif RightVowel == "AO":
        resultR = Consonantlist[RightConsonant][3]
    elif RightVowel == "O":
        resultR = Consonantlist[RightConsonant][4]
    elif RightVowel == "IA":
        resultR = Consonantlist[RightConsonant][5]
    elif RightVowel == "IAO":
        resultR = Consonantlist[RightConsonant][6]
    elif RightVowel == "IO":
        resultR = Consonantlist[RightConsonant][7]
    else:
        raise KeyError

    #LeftADkanaになにかあるときに
    if re.match("k?n?t?h?",LeftADkana):
        #LeftAsteriskに＊があるか見るよ　なかったらelseだよ
        if "*" in LeftAsterisk:
            if LeftADkana == "kn":
                        resultL = resultL +  "ろ"
            elif LeftADkana == "kt":
                        resultL = resultL +  resultL
            elif LeftADkana == "nh":
                        if LeftVowel == "A":
                                resultL = resultL +  "あ"
                        elif LeftVowel == "I":
                                resultL = resultL +  "え"
                        elif LeftVowel == "":
                                resultL = resultL +  "い"
                        elif LeftVowel == "AO":
                                resultL = resultL +  "え"
                        elif LeftVowel == "O":
                                resultL = resultL +  "い"
                        elif LeftVowel == "IA":
                                resultL = resultL +  "あ"
                        elif LeftVowel == "IAO":
                                resultL = resultL +  "い"
                        elif LeftVowel == "IO":
                                resultL = resultL +  "い"
                        else:
                            raise KeyError
            elif LeftADkana == "th":
                        resultL = resultL +  "いん"
            elif LeftADkana == "knth":
                        resultL = resultL +  ""
            elif LeftADkana == "k":
                        resultL = resultL +  "り"
            elif LeftADkana == "n":
                        resultL = resultL +  "れ"
            elif LeftADkana == "t":
                        resultL = resultL +  "る"
            elif LeftADkana == "h":
                        resultL = resultL +  "ら"
            elif LeftADkana == "":
                        resultL
            else:
                        raise KeyError
        #＊がなかったらこっち！
        else:
            if LeftADkana == "kn":
                    resultL = resultL +  "き"
            elif LeftADkana == "kt":
                    resultL = resultL +  "っ"
            elif LeftADkana == "nh":
                    if LeftVowel == "A":
                            resultL = resultL +  "い"
                    elif LeftVowel == "I":
                            resultL = resultL +  "い"
                    elif LeftVowel == "":
                            resultL = resultL +  "う"
                    elif LeftVowel == "AO":
                            resultL = resultL +  "い"
                    elif LeftVowel == "O":
                            resultL = resultL +  "う"
                    elif LeftVowel == "IA":
                            resultL = resultL +  "い"
                    elif LeftVowel == "IAO":
                            resultL = resultL +  "う"
                    elif LeftVowel == "IO":
                            resultL = resultL +  "う"
                    else:
                            raise KeyError
            elif LeftADkana == "th":
                    resultL = resultL +  "ち"
            elif LeftADkana == "knth":
                    resultL = resultL +  ""
            elif LeftADkana == "k":
                    resultL = resultL +  "く"
            elif LeftADkana == "n":
                    resultL = resultL +  "ん"
            elif LeftADkana == "t":
                    resultL = resultL +  "つ"
            elif LeftADkana == "h":
                    resultL = resultL +  "ー"
            elif LeftADkana == "":
                    resultL
            else:
                    raise KeyError
    #RightADkanaになにかあるときに
    if re.match("k?n?t?h?",RightADkana):
    #RightAsteriskに＊があるか見るよ　なかったらelseだよ
        if "*" in RightAsterisk:
            if RightADkana == "kn":
                        resultR = resultR +  "ろ"
            elif RightADkana == "kt":
                        resultR = resultR +  resultR
            elif RightADkana == "nh":
                    if RightVowel == "A":
                                resultR = resultR +  "あ"
                    elif RightVowel == "I":
                                resultR = resultR +  "え"
                    elif RightVowel == "":
                                resultR = resultR +  "い"
                    elif RightVowel == "AO":
                                resultR = resultR +  "え"
                    elif RightVowel == "O":
                                resultR = resultR +  "い"
                    elif RightVowel == "IA":
                                resultR = resultR +  "あ"
                    elif RightVowel == "IAO":
                                resultR = resultR +  "い"
                    elif RightVowel == "IO":
                                resultR = resultR +  "い"
                    else:
                        raise KeyError
            elif RightADkana == "th":
                        resultR = resultR +  "いん"
            elif RightADkana == "knth":
                        resultR = resultR +  ""
            elif RightADkana == "k":
                        resultR = resultR +  "り"
            elif RightADkana == "n":
                        resultR = resultR +  "れ"
            elif RightADkana == "t":
                        resultR = resultR +  "る"
            elif RightADkana == "h":
                        resultR = resultR +  "ら"
            elif RightADkana == "":
                        resultR
            else:
                    raise KeyError
        #＊がなかったらこっち！
        else:
            if RightADkana == "kn":
                    resultR = resultR +  "き"
            elif RightADkana == "kt":
                    resultR = resultR +  "っ"
            elif RightADkana == "nh":
                    if RightVowel == "A":
                            resultR = resultR +  "い"
                    elif RightVowel == "I":
                            resultR = resultR +  "い"
                    elif RightVowel == "":
                        resultR = resultR +  "う"
                    elif RightVowel == "AO":
                        resultR = resultR +  "い"
                    elif RightVowel == "O":
                        resultR = resultR +  "う"
                    elif RightVowel == "IA":
                        resultR = resultR +  "い"
                    elif RightVowel == "IAO":
                        resultR = resultR +  "う"
                    elif RightVowel == "IO":
                        resultR = resultR +  "う"
                    else:
                        raise KeyError
            elif RightADkana == "th":
                    resultR = resultR +  "ち"
            elif RightADkana == "knth":
                    resultR = resultR +  ""
            elif RightADkana == "k":
                    resultR = resultR +  "く"
            elif RightADkana == "n":
                    resultR = resultR +  "ん"
            elif RightADkana == "t":
                    resultR = resultR +  "つ"
            elif RightADkana == "h":
                    resultR = resultR +  "ー"
            elif RightADkana == "":
                    resultR
            else:
                    raise KeyError

    #どちらかのresultがなかったら片方のを返すようにしてるよ
    if resultL is None:
        resultR = result
    elif resultR is None:
        resultL = result
    elif resultL and resultR is None:
        raise KeyError
    else:
        result = resultL + resultR
    #↓、デバッグ用のコンソールに表示されるよ
    print(result)
    #↓、「{^^}」でスペースをなくす出力をしてるよ
    return "{^" + result + "^}"
