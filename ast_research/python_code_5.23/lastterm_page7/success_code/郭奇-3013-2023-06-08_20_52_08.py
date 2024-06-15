gdp_dict = {}
while True:
    input_str = input().strip()
    if input_str == "ok":
        break
    country, gdp = input_str.split()
    gdp_dict[country] = int(gdp)

# 2、获取所有的key值，存储在列表里
key_list = list(gdp_dict.keys())

# 3、获取所有的value值，存储在列表里
value_list = list(gdp_dict.values())
print(sorted(key_list))
print(sorted(value_list))
# 4、判断 键'India' 是否在字典中
if 'India' in gdp_dict:
    print('yes')
else:
    print('no')

# 5、获得字典里所有value 的和
sum_value = sum(gdp_dict.values())
print(sum_value)
