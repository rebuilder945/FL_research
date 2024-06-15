GDP={}
item=input()
while (item!='ok'):
    k,v=item.split()
    v=eval(v)
    GDP[k]=v
key_list = list(GDP.keys())
print(key_list)
value_list=list(GDP.values())
print(value_list)
print(GDP.get('India','no'))
print(sum(GDP.values()))
