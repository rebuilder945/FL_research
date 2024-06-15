# 从标准输入读入多个国家的名字和对应的GDP，存入GDP字典中
GDP = {}
while True:
    line = input().strip()
    if line == 'ok':
        break
    country, gdp = line.split()
    GDP[country] = int(gdp)
# 获取所有的key值，并将其存储在一个列表中，并按照字母顺序排序
keys = sorted(list(GDP.keys()))
# 获取所有的value值，并将其存储在一个列表中，并按照升序排列
values = sorted(list(GDP.values()))
# 判断键'India'是否在字典中，如果是输出'yes'，否则输出'no'
if 'India' in GDP:
    print('yes')
else:
    print('no')
# 计算字典里所有value的和，并输出结果
print(sum(GDP.values()))
# 输出结果
print(keys)
print(values)


