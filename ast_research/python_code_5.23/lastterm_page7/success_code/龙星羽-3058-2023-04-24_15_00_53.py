dic={}
while True:
    x=input()
    if x !='q':
        if x in dic:
            dic[x]+=1
        else :
            dic[x]=1
    else:
        break
v=max(dic,key=dic.get)
k=max(dic.values())
print(v,k,end=' ')
