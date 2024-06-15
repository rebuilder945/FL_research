dic={}
while True:
    a=input()
    if a=="q":
        break
    else:
        if a not in dic:
            dic[a]=1
        else:
            dic[a]+=1
b=max(dic.values())
for key,value in dic.items():
    if(value==b):
        print(key+" %d"%(value))
