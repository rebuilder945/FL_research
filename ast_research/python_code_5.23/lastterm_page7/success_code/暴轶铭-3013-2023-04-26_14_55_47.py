# 读入多行输入，直到读入"ok"
gdp = {}
while True:
    line = input().strip()
    if line == "ok":
        break
    data = line.split()
    gdp[data[0]] = int(data[1])
# 获取所有的key值，存储在列表里
keys = list(gdp.keys())
keys.sort()
print(keys)
# 获取所有的value值，存储在列表里
values = list(gdp.values())
values.sort()
print(values)
# 判断 键'india' 是否在字典中
if 'india' in gdp.keys():
    print('yes')
else:
    print('no')
# 获得字典里所有value 的和
sum_value = sum(gdp.values())
print(sum_value)

