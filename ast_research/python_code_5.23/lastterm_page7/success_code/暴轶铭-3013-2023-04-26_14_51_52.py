# 题目描述

# 存储国家gdp的字典结构如下：

gdp = {
    'usa': 95,
    'china': 80,
    'japan': 50
}

# 题目要求：
# 1、请从标准输入录入多个国家的名字和对应的gdp，存入gdp字典中。(字典不为空)
keys = []
values = []
while True:
    s = input()
    if s == "ok":
        break
    key, value = s.split()
    keys.append(key)
    values.append(int(value))
gdp = {k: v for k, v in zip(keys, values)}
    
# 2、获取所有的key值，存储在列表里
sorted_keys = sorted(list(gdp.keys()))

# 3、获取所有的value值，存储在列表里
sorted_values = sorted(list(gdp.values()))

# 4、判断 键'india' 是否在字典中
india_existence = "yes" if "india" in gdp else "no"

# 5、获得字典里所有value 的和
sum_values = sum(gdp.values())

# 输出结果
print(sorted_keys)
print(sorted_values)
print(india_existence)
print(sum_values)

