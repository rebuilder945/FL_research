string = input()

if not string:
    print("None")  # 输入为空字符串，输出 "None"
else:
    found = False
    for x in string:
        if string.count(x) == 1:
            print(x)
            found = True
            break

    if not found:
        print("None")  # 没有没有重复的字符，输出 "None"

