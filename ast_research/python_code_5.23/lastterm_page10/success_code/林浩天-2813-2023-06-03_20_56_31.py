# 获取输入
s = input().strip()
sub = input().strip()

# 删除所有子串
for sub in s:
    s = s.replace(sub, "")

# 输出结果
print(s)

