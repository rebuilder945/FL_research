s = input()
sub = input()

# 将字符串拆分成子串列表
sub_list = s.split(sub)

# 将子串列表重新合并成字符串
new_s = "".join(sub_list)

# 输出结果
print(new_s)
