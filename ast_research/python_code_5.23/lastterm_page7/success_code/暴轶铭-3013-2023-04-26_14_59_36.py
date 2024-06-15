#读取输入并存入字典
gdp = {}
while True:
    input_str = input()
    if input_str == 'ok':
        break
    else:
        country, gdp = input_str.split()
        gdp[country] = int(gdp)

#排序获得key列表和value列表
key_list = sorted(gdp.keys())
val_list = sorted(gdp.values())

#判断'india'是否在字典中
is_exist_india = 'yes' if 'india' in gdp else 'no'

#获得value和
val_sum = sum(val_list)

#输出结果
print(key_list)
print(val_list)
print(is_exist_india)
print(val_sum)

