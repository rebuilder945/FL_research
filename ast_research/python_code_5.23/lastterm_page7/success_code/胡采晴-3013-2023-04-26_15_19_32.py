GDP = {}
while True:
    user_input = input()
    if user_input == 'ok':
        if not GDP:
            continue
        break
    nation,gdp = user_input.split()
    GDP[nation] = int(gdp)

   
    dict_keys = list(GDP.keys())
    dict_values = list(GDP.values)
    dict_keys.sort()
    dict_values.sort()

print(dict_keys)
print(dict_values)
print('yes' if 'India' in dict_keys else 'no')
print(sum(dict_values))
