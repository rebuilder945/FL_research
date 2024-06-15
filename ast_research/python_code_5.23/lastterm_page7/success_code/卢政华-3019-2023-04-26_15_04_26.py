gdp = {}
while True:
    line = input().strip()
    if line == 'ok':
        break
    name, value = line.split()
    gdp[name] = int(value)

# 获取所有的key值并排序
key_list = list(gdp.keys())
key_list.sort()

# 获取所有的value值并排序
value_list = list(gdp.values())
value_list.sort()

# 判断 India 是否在字典中
if 'India' in gdp:
    print('yes')
else:
    print('no')

# 获取字典里所有值的和并输出
total_gdp = sum(gdp.values())
print(total_gdp)

# 输出结果
print(key_list)
print(value_list)
