dic={}
lst2=[]
lst3=[]
lst5=[]
lst=input().split("")
for x in lst:
    dic[x]=dic.get(x,0)+1
for y in dic.keys():
    lst2.append(y)
for z in dic.values():
    lst3.append(z)
lst4=[]
m=len(lst2)
for n in range(m):
    lst4=lst4+[[lst2[n],lst3[n]]]
a=max(lst3)
for t in range(m):
    if lst4[t][1]==a:
        lst5.append(lst4[t])
i=len(lst5)
lst5.sort(key=lambda x:x[0])
if i==1:
    print("%s %d"%(lst5[0][0],lst5[0][1]))
else:
    for v in range(i):
        print("%s %d"%(lst5[v][0],lst5[v][1]))
        print()

