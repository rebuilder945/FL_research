GDP={}
while True:
    s=input()
    if s=="ok":
        break
    c,g=input().split(" ")
    GDP[c]=int(g)
dict_keys=list(GDP.keys())
dict_values=list(GDP.values())
print('yes' if 'India' in dict_keys else 'no')
print(sum(dict_values))
