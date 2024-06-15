GDP = {}

# 从标准输入录入国家名字和对应的GDP，存入字典GDP中
while True:
    data = input().split()
    if data[0] == 'ok':
        break
    country = data[0]
    gdp = int(data[1])
    GDP[country] = gdp

# 获取所有的key值，存储在列表里，并按升序排列
keys = sorted(list(GDP.keys()))

# 获取所有的value值，存储在列表里，并按升序排列
values = sorted(list(GDP.values()))

# 判断键'India'是否在字典中
if 'India' in GDP:
    is_india_present = 'yes'
else:
    is_india_present = 'no'

# 获得字典里所有value的和
total_gdp = sum(GDP.values())

# 输出结果
print(keys)
print(values)
print(is_india_present)
print(total_gdp)

