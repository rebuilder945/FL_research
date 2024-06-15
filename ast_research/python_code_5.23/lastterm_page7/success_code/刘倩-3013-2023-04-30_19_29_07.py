# 初始化字典GDP
GDP = {}

# 从标准输入录入多个国家的名字和对应的GDP，存入GDP字典中
while True:
    input_str = input().strip()
    if input_str == "ok":
        break
    country, gdp = input_str.split()
    GDP[country] = int(gdp)

# 获取所有的key值，存储在列表里，升序排列
keys = sorted(list(GDP.keys()))

# 获取所有的value值，存储在列表里，升序排列
values = sorted(list(GDP.values()))



# 获得字典里所有value的和
sum_value = sum(GDP.values())

# 输出结果
print(keys)
print(values)
# 判断键'India'是否在字典中，是输出'yes'，否输出'no'
if 'India' in GDP:
    print('yes')
else:
    print('no')
print(sum_value)

