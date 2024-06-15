# 创建一个空的字典gdp
gdp = {}
# 从标准输入录入多个国家的名字和对应的gdp，存入gdp字典中
while True:
    raw = input().strip() # 去掉字符串前后的空格
    if raw == 'ok':
        break
    name, number = raw.split() # 将raw按照空格分开，并赋值给name和number
    gdp[name] = float(number) # 将name作为key,number作为value保存到gdp字典中

# 获取所有的key值，存储在列表里，升序排列
keys_list = sorted(gdp.keys())
print(keys_list)

# 获取所有的value值，存储在列表里，升序排列
values_list = sorted(gdp.values())
print(values_list)

# 判断 键'india' 是否在字典中，是输出'yes', 否输出'no'
if 'india' in gdp:
    print('no')
else:
    print('yes')

# 获得字典里所有value 的和
print(int(sum(gdp.values())))
