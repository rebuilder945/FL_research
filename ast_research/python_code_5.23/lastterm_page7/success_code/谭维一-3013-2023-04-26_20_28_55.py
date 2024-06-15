GDP={}
while True:
    s=input()
    if s=="ok":
        break
    c,g=input().split(" ")
    GDP[c]=int(g)
dict_keys=list(GDP.keys())
dict_values=list(GDP.values())
dict_keys.sort()
dict_values.sort()
print(dict_keys)
print(dict_values)
print('yes' if 'India' in dict_keys else 'no')
print(sum(GDP.values()))
