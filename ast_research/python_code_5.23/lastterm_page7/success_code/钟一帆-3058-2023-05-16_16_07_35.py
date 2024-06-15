dic={}
s=input()
while (s!='q'):
    dic[s]=dic.get(s,0)+1
    s=input()
   
d=list(dic.items())
d.sort(key=lambda x:x[1],reverse=True)
print('%s %d'%(d[0][0],d[0][1]))

