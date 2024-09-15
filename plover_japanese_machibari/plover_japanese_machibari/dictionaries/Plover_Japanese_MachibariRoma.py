#正規表現(Regex)を有効化すると宣言するよ
import re

#打鍵が続けられる長さを指定するよ (Plover Python dictionary)
LONGEST_KEY = 1

def lookup(key):
    assert len(key) <= LONGEST_KEY
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
    "": ["a","i","","e","o","ya","yu","yo"],
    "K": ["ka","ki","ku","ke","ko","kya","kyu","kyo"],
    "S": ["sa","shi","su","se","so","sha","shu","sho"],
    "T": ["ta","ti","tu","te","to","cha","chu","cho"],
    "TH": ["na","ni","nu","ne","no","nya","nyu","nyo"],
    "H": ["ha","hi","fu","he","ho","hya","hyu","hyo"],
    "ST": ["ma","mi","mu","me","mo","mya","myu","myo"],
    "SH": ["ra","ri","ru","re","ro","rya","ryu","ryo"],
    "KH": ["wa","","u","","wo","","",""],
    "SK": ["ga","gi","gu","ge","go","gya","gyu","gyo"],
    "STK": ["za","zi","zu","ze","zo","ja","ju","jo"],
    "TK": ["da","di","du","de","do","dhi","dhu","dexe"],
    "SKH": ["ba","bi","bu","be","bo","bya","byu","byo"],
    "STH": ["pa","pi","pu","pe","po","pya","pyu","pyo"],
    "TKH": ["xa","xi","xu","xe","xo","xya","xyu","xyo"],
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
                        resultL = resultL +  "ro"
            elif LeftADkana == "kt":
                        resultL = resultL +  resultL
            elif LeftADkana == "nh":
                        if LeftVowel == "A":
                                resultL = resultL +  "a"
                        elif LeftVowel == "I":
                                resultL = resultL +  "e"
                        elif LeftVowel == "":
                                resultL = resultL +  "i"
                        elif LeftVowel == "AO":
                                resultL = resultL +  "e"
                        elif LeftVowel == "O":
                                resultL = resultL +  "i"
                        elif LeftVowel == "IA":
                                resultL = resultL +  "a"
                        elif LeftVowel == "IAO":
                                resultL = resultL +  "i"
                        elif LeftVowel == "IO":
                                resultL = resultL +  "i"
                        else:
                            raise KeyError
            elif LeftADkana == "th":
                        resultL = resultL +  "inn"
            elif LeftADkana == "knth":
                        resultL = resultL +  ""
            elif LeftADkana == "k":
                        resultL = resultL +  "ri"
            elif LeftADkana == "n":
                        resultL = resultL +  "re"
            elif LeftADkana == "t":
                        resultL = resultL +  "ru"
            elif LeftADkana == "h":
                        resultL = resultL +  "ra"
            elif LeftADkana == "":
                        resultL
            else:
                        raise KeyError
        #＊がなかったらこっち！
        else:
            if LeftADkana == "kn":
                    resultL = resultL +  "ki"
            elif LeftADkana == "kt":
                    resultL = resultL +  "xtu"
            elif LeftADkana == "nh":
                    if LeftVowel == "A":
                            resultL = resultL +  "i"
                    elif LeftVowel == "I":
                            resultL = resultL +  "i"
                    elif LeftVowel == "":
                            resultL = resultL +  "u"
                    elif LeftVowel == "AO":
                            resultL = resultL +  "i"
                    elif LeftVowel == "O":
                            resultL = resultL +  "u"
                    elif LeftVowel == "IA":
                            resultL = resultL +  "i"
                    elif LeftVowel == "IAO":
                            resultL = resultL +  "u"
                    elif LeftVowel == "IO":
                            resultL = resultL +  "u"
                    else:
                            raise KeyError
            elif LeftADkana == "th":
                    resultL = resultL +  "ti"
            elif LeftADkana == "knth":
                    resultL = resultL +  ""
            elif LeftADkana == "k":
                    resultL = resultL +  "ku"
            elif LeftADkana == "n":
                    resultL = resultL +  "nn"
            elif LeftADkana == "t":
                    resultL = resultL +  "tu"
            elif LeftADkana == "h":
                    resultL = resultL +  "-"
            elif LeftADkana == "":
                    resultL
            else:
                    raise KeyError
    #RightADkanaになにかあるときに
    if re.match("k?n?t?h?",RightADkana):
    #RightAsteriskに＊があるか見るよ　なかったらelseだよ
        if "*" in RightAsterisk:
            if RightADkana == "kn":
                        resultR = resultR +  "ro"
            elif RightADkana == "kt":
                        resultR = resultR +  resultR
            elif RightADkana == "nh":
                    if RightVowel == "A":
                                resultR = resultR +  "a"
                    elif RightVowel == "I":
                                resultR = resultR +  "e"
                    elif RightVowel == "":
                                resultR = resultR +  "i"
                    elif RightVowel == "AO":
                                resultR = resultR +  "e"
                    elif RightVowel == "O":
                                resultR = resultR +  "i"
                    elif RightVowel == "IA":
                                resultR = resultR +  "a"
                    elif RightVowel == "IAO":
                                resultR = resultR +  "i"
                    elif RightVowel == "IO":
                                resultR = resultR +  "i"
                    else:
                        raise KeyError
            elif RightADkana == "th":
                        resultR = resultR +  "inn"
            elif RightADkana == "knth":
                        resultR = resultR +  ""
            elif RightADkana == "k":
                        resultR = resultR +  "ri"
            elif RightADkana == "n":
                        resultR = resultR +  "re"
            elif RightADkana == "t":
                        resultR = resultR +  "ru"
            elif RightADkana == "h":
                        resultR = resultR +  "ra"
            elif RightADkana == "":
                        resultR
            else:
                    raise KeyError
        #＊がなかったらこっち！
        else:
            if RightADkana == "kn":
                    resultR = resultR +  "ki"
            elif RightADkana == "kt":
                    resultR = resultR +  "xtu"
            elif RightADkana == "nh":
                    if RightVowel == "A":
                            resultR = resultR +  "i"
                    elif RightVowel == "I":
                            resultR = resultR +  "i"
                    elif RightVowel == "":
                        resultR = resultR +  "u"
                    elif RightVowel == "AO":
                        resultR = resultR +  "i"
                    elif RightVowel == "O":
                        resultR = resultR +  "u"
                    elif RightVowel == "IA":
                        resultR = resultR +  "i"
                    elif RightVowel == "IAO":
                        resultR = resultR +  "u"
                    elif RightVowel == "IO":
                        resultR = resultR +  "u"
                    else:
                        raise KeyError
            elif RightADkana == "th":
                    resultR = resultR +  "ti"
            elif RightADkana == "knth":
                    resultR = resultR +  ""
            elif RightADkana == "k":
                    resultR = resultR +  "ku"
            elif RightADkana == "n":
                    resultR = resultR +  "nn"
            elif RightADkana == "t":
                    resultR = resultR +  "tu"
            elif RightADkana == "h":
                    resultR = resultR +  "-"
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
