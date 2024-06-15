st = input()
s = {}
for x in st:
    for i in x:
        if i not in s:
            s[i] = 1
        else:
            s[i] += 1

# 使用正确的关键字参数 key，而不是 ke
s_sorted = sorted(s.items(), key=lambda x: x[0])

# 将 s 重新赋值为了排序后的结果，但是 sorted() 函数返回的是一个新的排序列表，而不会修改原始列表，
# 因此，应该将排序后的结果赋给一个新的变量，而不是覆盖原来的 s 字典。
s_sorted = [list(x) for x in s_sorted]
for x in s_sorted:
    print("%s,%d" % (x[0], x[1]))