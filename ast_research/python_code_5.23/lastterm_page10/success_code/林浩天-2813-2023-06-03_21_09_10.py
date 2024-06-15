# 获取输入
s = input()
sub = input()

# 删除所有子串
if sub in s:
    s = s.remove(sub)

# 输出结果
print(s)

