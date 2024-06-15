GDP={}
while True:
    input_str=input()
    if input_str=='ok':
        break
    k,v=input_str.split('')
    GDP[k]=v
key_list = list(GDP.keys())
print(key_list)
value_list=list(GDP.values())
print(value_list)
print(GDP.get('India','no'))
print(sum(GDP.values()))
