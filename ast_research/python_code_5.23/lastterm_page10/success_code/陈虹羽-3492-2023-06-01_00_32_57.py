a=input()
c=[]
if a=='':
    print('None')
else:
    dic={}
    for i in a:
        dic[i]=dic.get(i,0)+1
    for k,v in dic.items():
        if v==1:
            c.append(k)
for i in a:
    if i in c:
        print(i)
        break
