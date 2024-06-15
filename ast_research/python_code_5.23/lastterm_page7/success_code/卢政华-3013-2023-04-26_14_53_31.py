GDP = {}

# 输入国家名字和对应的 GDP，存入 GDP 字典中
while True:
    line = input().split()
    if line[0] == 'ok':
        break
    GDP[line[0]] = int(line[1])

# 获取所有的 key 值，存储在列表里并升序排列
keys = list(GDP.keys())
keys.sort()

# 获取所有的 value 值，存储在列表里并升序排列
values = list(GDP.values())
values.sort()

# 判断键 'India' 是否在字典中，并输出结果
if 'India' in keys:
    print('yes')
else:
    print('no')
