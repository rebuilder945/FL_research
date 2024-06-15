GDP = {}
while True:
    a=input()
    if a == 'ok':
        break
    k, v = a.split(' ')
    GDP[k] = int(v)

dict_keys = list(GDP.keys())    
dict_values = list(GDP.values())
dict_keys.sort()
dict_values.sort()
print(dict_keys)
print(dict_values)
print('yes' if 'India' in dict_keys else 'no')
print(sum(dict_values))
