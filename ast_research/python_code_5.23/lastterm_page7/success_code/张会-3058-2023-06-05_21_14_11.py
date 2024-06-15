s=input() or 'q'
dic={}
while(s!='q'):
    dic[s]=dic.get(s,0)+1
    s=input() or 'q'
ls=[]
for k,v in dic.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[1],reverse=True)
m=ls[0]
print(m[0],m[1])
