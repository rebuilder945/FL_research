c={}
while True:
    a=input()
    if a=="q":
        break
    if a not in c.:
        c["a"]=1
    else:
        c["a"]+=1
top={}
for v,t in c.items():
    top[t]=v
m=max(list(top.keys()))
print(top[m],m)



    









            
