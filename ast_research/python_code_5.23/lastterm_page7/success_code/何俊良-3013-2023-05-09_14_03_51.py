# 初始化字典
GDP = {'USA': 95, 'China': 80, 'Japan': 50}

# 输入多个国家的GDP，存储到字典中
while True:
    inputs = input().split()
    if inputs[0] == 'ok':
        break
    else:
        GDP[inputs[0]] = int(inputs[1])

# 获取所有的key值，存储在列表里
keys = list(GDP.keys())

# 获取所有的value值，存储在列表里
values = list(GDP.values())

# 判断键'India'是否在字典中
if 'India' in GDP:
    print('yes')
else:
    print('no')

# 获得字典里所有value的和
total_GDP = sum(values)

print(keys)
print(values)
print(total_GDP)


