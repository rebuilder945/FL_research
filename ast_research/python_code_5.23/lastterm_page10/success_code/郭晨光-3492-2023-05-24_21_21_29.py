s = input()  # 从标准输入读入字符串
count = {}  # 用字典记录每个字符出现的次数
for c in s:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1

for c in s:
    if count[c] == 1:
        print(c)
        break
else:
    print("None")

