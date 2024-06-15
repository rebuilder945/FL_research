lst = eval(input())

# 统计每个字母出现的次数
count = {}
for s in lst:
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

# 按照字母顺序输出结果
for c in sorted(count.keys()):
    print("%s, %d" % (c, count[c]))
