GDP = {'USA': 95, 'China': 80, 'Japan': 50}
# 从标准输入录入多个国家的名字和对应的GDP，存入GDP字典中（不考虑数据格式的错误）
while True:
    s = input("请输入国家和GDP(以空格隔开,输入q结束):")
    if s == 'q':
        break
    country, gdp = s.split()
    GDP[country] = int(gdp)
# 获取所有的key值，存储在列表里
keys = list(GDP.keys())
# 获取所有的value值，存储在列表里
values = list(GDP.values())
# 判断键'India'是否在字典中
if 'India' in GDP:
    print("India的GDP为:", GDP['India'])
else:
    print("GDP字典中没有India这个键")
# 获得字典里所有value的和
total_gdp = sum(GDP.values())
print("GDP字典中所有国家的GDP总和为:", total_gdp)
