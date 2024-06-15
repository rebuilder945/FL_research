dic={}
m=eval(input())
for x in m:
    if x=='q':
        break
    else:
        dic[x]=dic.get[x,0]+1
mm=[]
for k,v in dic.items():
    mm.append([k,v])
mm.sort(key=lambda x:x[1],reverse=True)
print(mm(0))
    
