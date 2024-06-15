gdp = {}
while true:
    line = input()
    if line == 'ok':
        break
    country, gdp = line.split()
    gdp[country] = int(gdp)

# 2. 获取所有的key值，存储在列表里
keys = sorted(list(gdp.keys()))

# 3. 获取所有的value值，存储在列表里
values = sorted(list(gdp.values()))

# 4. 判断 键'india' 是否在字典中
if 'india' in gdp:
    print('yes')
else:
    print('no')

# 5. 获得字典里所有value 的和
value_sum = sum(gdp.values())

print(keys)
print(values)
print(value_sum)

