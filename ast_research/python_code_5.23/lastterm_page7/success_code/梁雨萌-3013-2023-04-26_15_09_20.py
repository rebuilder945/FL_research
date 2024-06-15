item  =  input()  or  "ok"
dic  =  {}
key=[]
Value=[]
while(item  !="ok"):
        country,  GDP  =  item.split()
        GDP  =  eval(GDP)
        dic[country]  =  GDP
        key.append(country)
        Value.append(GDP)
        item  =  input()  or  "ok"
        
key.sort()
print(key)

Value.sort()
print(Value)
        
if "India" not in key:
    print('No')
else:
    print("Yes")
    
print(sum(Value))
