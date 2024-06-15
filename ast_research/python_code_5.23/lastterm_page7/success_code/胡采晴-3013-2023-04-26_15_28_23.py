GDP = {}
input_str = input()
k,v = input_str.split(' ')
while input_str != 'ok':
    GDP[k] = int(v)
    if input_str == 'ok':
        break
   
dict_keys = list(GDP.keys())
dict_values = list(GDP.values)
dict_keys.sort()
dict_values.sort()
print(dict_keys)
print(dict_values)
print('yes' if 'India' in dict_keys else 'no')
print(sum(dict_values))
