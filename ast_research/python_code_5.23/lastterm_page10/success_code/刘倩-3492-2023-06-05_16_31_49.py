string = input()

if not string:
    print("None")  # 输入为空字符串，输出 "None"
else:
    found = False
    for char in string:
        if string.count(char) == 1:
            print(char)
            found = True
            break

    if not found:
        print("None")  # 没有没有重复的字符，输出 "None"

