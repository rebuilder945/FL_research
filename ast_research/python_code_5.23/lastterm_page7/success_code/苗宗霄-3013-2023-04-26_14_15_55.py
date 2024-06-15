# 定义字典
gdp = {
    'usa': 95,
    'china': 80,
    'japan': 50
}

# 获取输入
while True:
    try:
        country_gdp = input().split()
        # 输入ok结束
        if country_gdp[0] == "ok":
            break
        gdp[country_gdp[0]] = int(country_gdp[1])
    except:
        break
        
# 获取所有key并排序
keys = sorted(gdp.keys())

# 获取所有value并排序
values = sorted(gdp.values())

# 判断'india'是否在字典中，并输出结果
if 'india' in gdp:
    print("yes")
else:
    print("no")

# 计算所有value的和，并输出结果
print(sum(values))

# 输出列表keys和values
print(keys)
print(values)

