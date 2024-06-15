# 定义一个空字典用来存储数据
gdp = {}

# 循环读取输入，直到遇到 "ok" 结束
while true:
    data = input().strip()
    if data == "ok":
        break
    # 获取国家和 gdp 数据
    country, gdp = data.split()
    # 将国家和 gdp 存入字典
    gdp[country] = int(gdp)

# 获取所有的 key 值，升序排列
keys = sorted(list(gdp.keys()))
print(keys)

# 获取所有的 value 值，升序排列
values = sorted(list(gdp.values()))
print(values)

# 判断键 'india' 是否在字典中
if 'india' in gdp:
    print('yes')
else:
    print('no')

# 所有 value 值的和
sum_values = sum(gdp.values())
print(sum_values)

