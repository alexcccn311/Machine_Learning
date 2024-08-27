def girl_reponse(high):
    match high:
        case _ if high >= 180:
            return'帅哥，今晚有空么？'
        case _ if 173<= high < 180:
            return'别离我这么近，滚远点。'
        case _ if 173>high:
            return'贱人，给我跪下。你也配站在我面前？'
high=int(input('请输入你的身高：'))
result = girl_reponse(high)
print(result)