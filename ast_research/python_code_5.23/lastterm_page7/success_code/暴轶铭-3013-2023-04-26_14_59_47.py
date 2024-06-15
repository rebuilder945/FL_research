gdp = {
    'usa': 95,
    'china': 80,
    'japan': 50
}
keys = []
values = []
while True:
    s = input()
    if s == "ok":
        break
    key, value = s.split()
    keys.append(key)
    values.append(int(value))
gdp = {k: v for k, v in zip(keys, values)}
    
sorted_keys = sorted(list(gdp.keys()))

sorted_values = sorted(list(gdp.values()))

# 4、判断 键'india' 是否在字典中
india_existence = "yes" if "india" in gdp else "no"

# 5、获得字典里所有value 的和
sum_values = sum(gdp.values())

# 输出结果
print(sorted_keys)
print(sorted_values)
print(india_existence)
print(sum_values)

