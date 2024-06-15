keys=input()
dict1={}
while keys!="q":
    dict1[keys]=dict1.get(keys,0)+1
    keys=input()
key_list={}
value_list={}
for key,value in dict1.items():
    key_list.append(key)
    value_list.append(value)
a=max(dict1.values())
key_=value_list.index(a)
print(key_,a)
