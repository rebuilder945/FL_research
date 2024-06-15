# 存储国家 GDP 的字典
GDP = {}

# 从标准输入录入多个国家的名字和对应的 GDP，存入 GDP 字典中
while True:
    input_str = input('请输入国家和对应的 GDP（以空格分隔），输入 ok 结束：')
    if input_str == 'ok':
        break
    country, gdp = input_str.split()
    GDP[country] = int(gdp)

# 获取所有的 key 值，存储在列表里
key_list = list(GDP.keys())
key_list.sort()

# 获取所有的 value 值，存储在列表里
value_list = list(GDP.values())
value_list.sort()

# 判断键 'India' 是否在字典中
if 'India' in GDP:
    print('yes')
else:
    print('no')

# 获得字典里所有 value 的和
sum_value = sum(value_list)

# 输出结果
print('所有的 key 值为：', key_list)
print('所有的 value 值为：', value_list)
print('字典里所有 value 的和为：', sum_value)

