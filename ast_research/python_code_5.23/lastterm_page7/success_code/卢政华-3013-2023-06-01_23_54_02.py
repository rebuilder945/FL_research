GDP = {}
while True:
    line = input()
    if line == "ok":
        break
    name, gdp_str = line.split(" ")
    GDP[name] = int(gdp_str)
keys_list = list(GDP.keys())
keys_list.sort()
values_list = list(GDP.values())
values_list.sort()

sum_of_values = sum(values_list)
print(keys_list)
print(values_list)
if "india" in GDP:
    print('yes')
else:
    print('no')
print(sum_of_values)
