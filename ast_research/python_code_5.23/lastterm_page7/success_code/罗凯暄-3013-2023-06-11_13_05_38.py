# 初始化字典
GDP = {
    'USA': 95,
    'China': 80,
    'Japan': 50
}

# 从标准输入录入多个国家的名字和对应的GDP，存入GDP字典中
while True:
    input_str = input()
    if input_str == 'ok':
        break
    country, gdp = input_str.split()
    GDP[country] = int(gdp)

# 获取所有的key值，存储在列表里
keys = list(GDP.keys())
keys.sort()

# 获取所有的value值，存储在列表里
values = list(GDP.values())
values.sort()

# 判断 键'India' 是否在字典中
if 'India' in GDP:
    print('yes')
else:
    print('no')

# 获得字典里所有value 的和
total_gdp = sum(values)

# 输出结果
print(keys)
print(values)
print(total_gdp)

