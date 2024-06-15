GDP = {}
while True:
    country = input("请输入国家名称：")
    if not country:
        break
    gdp = float(input("请输入该国家的GDP："))
    GDP[country] = gdp
keys = list(GDP.keys())
values = list(GDP.values())
if 'India' in GDP:
    print("India 在字典中")
else:
    print("India 不在字典中")
total_gdp = sum(GDP.values())
print("所有国家的GDP总和为:", total_gdp)

