dic = {}
while 1:
    string = input()
    if string == "q":
        break
    try:
        value = dic[string]
    except KeyError:
        value = 0
    dic[string] = value + 1
print(max(dic, key=dic.get), max(dic.values()))


