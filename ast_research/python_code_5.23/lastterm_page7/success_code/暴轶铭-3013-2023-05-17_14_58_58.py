GDP = {
    'USA': 95,
    'China': 80,
    'Japan': 50
}

# 1. 从标准输入中录入国家的名字和对应的GDP，并添加到字典 GDP 中
while True:
    # 输入国家名称和 GDP 值，以空格分隔
    input_str = input("请输入国家名称和 GDP，以空格分隔，若输入“exit”则退出输入：")
    if input_str == "exit":
        break
    country, gdp_value = input_str.split()
    GDP[country] = int(gdp_value)

# 2. 获取所有 key 值，存储在列表里
key_list = list(GDP.keys())

# 3. 获取所有 value 值，存储在列表里
value_list = list(GDP.values())

# 4. 判断键'India' 是否在字典中
if 'India' in GDP:
    print("India 的 GDP 值为：", GDP["India"])
else:
    print("India 不在 GDP 字典中")

# 5. 获得字典里所有 value 的和
sum_gdp = sum(GDP.values())
print("GDP 总和为：", sum_gdp)
