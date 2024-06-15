s = input().split()           # 读取未指定个数的字符串并用分割符分割
d = {}                        # 构建一个空字典
for i in s:                   # 遍历所有输入数据
    d[i] = d.get(i, 0) + 1    # 统计每个字符串出现的次数
max_count = max(d.values())   # 找到出现次数最多的值
result = []                   # 记录结果的List
for key, value in d.items():  # 遍历字典中的键值对
    if value == max_count:    # 如果当前键对应的值等于出现次数最多的值
        result.append(key)    # 记录当前键到结果List
result.sort()                 # 结果列表升序排序
for i in result:              # 遍历结果输出结果
    print(i, max_count)

