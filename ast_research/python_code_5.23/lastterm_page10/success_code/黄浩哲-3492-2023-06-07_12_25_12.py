s = input().strip()  # 输入字符串并去除两端空格

# 统计每个字符出现次数
count = {}
for c in s:
    count[c] = count.get(c, 0) + 1

# 找到第一个出现次数为1的字符
for c in s:
    if count[c] == 1:
        print(c)
        break
else:
    print("None") 
