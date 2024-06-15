GDP = {}

# 读取输入，直到出现 "ok"
while True:
    s = input().strip()
    if s == "ok":
        break
    else:
        name, value = s.split()
        GDP[name] = int(value)

# 获取所有的 key 和 value 值，并排序
keys_list = sorted(list(GDP.keys()))
values_list = sorted(list(GDP.values()))

# 判断 'India' 是否在字典中
flag = "yes" if "India" in GDP else "no"

# 计算所有 value 的和
sum_values = sum(GDP.values())

# 输出结果
print(keys_list)
print(values_list)
print(flag)
print(sum_values)
