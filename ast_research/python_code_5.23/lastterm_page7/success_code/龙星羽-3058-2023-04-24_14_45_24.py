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
danum=max(dic.keys())
dashu=max(dic.values())   
print(danum,dashu,end=' ')
