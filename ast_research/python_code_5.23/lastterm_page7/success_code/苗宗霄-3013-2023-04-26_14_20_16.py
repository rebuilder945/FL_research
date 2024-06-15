gdp = {
    'USA': 95,
    'China': 80,
    'Japan': 50
}

# 1. 请从标准输入录入多个国家的名字和对应的gdp，存入gdp字典中
while True:
    input_str = input()
    if input_str == 'ok':
        break
    country, gdp_val = input_str.split()  # 解包关键词
    gdp[country] = int(gdp_val)  # 将输入的值转换为int类型

# 2. 获取所有的key值，存储在列表里
keys = sorted(list(gdp.keys()))
print(keys)

# 3. 获取所有的value值，存储在列表里
values = sorted(list(gdp.values()))
print(values)

# 4. 判断键'india' 是否在字典中
if 'India' in gdp:  # 大小写不敏感，按照题目要求输出 no
    print('yes')
else:
    print('no')

# 5. 获得字典里所有value的和
total_gdp = sum(gdp.values())
print(total_gdp)

