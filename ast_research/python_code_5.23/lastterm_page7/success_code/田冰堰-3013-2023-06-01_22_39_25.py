item=input() or "ok"
GDP={}
while (item!="ok"):
    k,v=item.split()
    v=eval(v)
    GDP[k]=v
    item=input() or "ok"
key_list = list(GDP.keys())
key_list.sort()
print(key_list)
value_list=list(GDP.values())
value_list.sort()
print(value_list)
print('yes'if 'India'in key_list else 'no')
print(sum(GDP.values()))
