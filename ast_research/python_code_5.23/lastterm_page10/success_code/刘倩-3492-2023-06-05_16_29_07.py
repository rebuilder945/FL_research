string = input()

if not string:
    print("None")  # 输入为空字符串，输出 "None"
else:
    count = {}  # 使用字典记录字符出现的次数
    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in string:
        if count[char] == 1:
            print(char)
            break

    if all(count[char] > 1 for char in string):
        print("None")  # 没有没有重复的字符，输出 "None"

