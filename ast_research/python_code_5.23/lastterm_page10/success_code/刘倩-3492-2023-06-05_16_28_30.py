string = input()

if not string:
    print("None")  # 输入为空字符串，输出 "None"
else:
    seen = set()  # 用集合来记录已经出现过的字符
    for char in string:
        if char not in seen:
            seen.add(char)  # 将第一次出现的字符加入集合
        else:
            seen.remove(char)  # 如果字符已经出现过，则从集合中移除

    if seen:
        print(seen.pop())  # 输出第一个没有重复的字符
    else:
        print("None")  # 没有没有重复的字符，输出 "None"

