stringList = eval(input())

# 统计每个字母出现的次数
count = [0] * 26  # 初始化为0
for string in stringList:
    for char in string:
        if char.islower():
            count[ord(char) - ord('a')] += 1

# 输出结果
for i in range(26):
    if count[i] > 0:
        print(chr(ord('a') + i) + "," + str(count[i]))

