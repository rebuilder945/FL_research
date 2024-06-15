GDP = {'USA': 95, 'China': 80, 'Japan': 50}

# 从标准输入录入多个国家的名字和对应的GDP，存入GDP字典中
while True:
    line = input()
    if line == "ok":
        break
    name, gdp_str = line.split(" ")
    GDP[name] = int(gdp_str)

# 获取所有的key值，存储在列表里
keys_list = list(GDP.keys())
keys_list.sort()

# 获取所有的value值，存储在列表里
values_list = list(GDP.values())
values_list.sort()

# 判断 键'India' 是否在字典中
india_is_in_dict = 'India' in GDP
if india_is_in_dict:
    print('yes')
else:
    print('no')

# 获得字典里所有value 的和
sum_of_values = sum(values_list)

print(keys_list)
print(values_list)
print(india_is_in_dict)
print(sum_of_values)
