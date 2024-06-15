gdp = {
    'usa': 95,
    'china': 80,
    'japan': 50
}

# 1. 请从标准输入录入多个国家的名字和对应的gdp，存入gdp字典中
while True:
    input_str = input()
    if input_str == 'ok':
        break
    country, gdp = input_str.split()
    gdp[country] = int(gdp)

# 2. 获取所有的key值，存储在列表里
keys = sorted(list(gdp.keys()))
print(keys)

# 3. 获取所有的value值，存储在列表里
values = sorted(list(gdp.values()))
print(values)

# 4. 判断键'india' 是否在字典中
if 'india' in gdp:
    print('yes')
else:
    print('no')

# 5. 获得字典里所有value的和
total_gdp = sum(gdp.values())
print(total_gdp)

