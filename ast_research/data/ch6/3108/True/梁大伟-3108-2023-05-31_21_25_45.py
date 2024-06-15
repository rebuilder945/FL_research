lst=eval(input())
d={}
for i in lst:
    for t in i:
        d[t]=d.get(t,0)+1
lst1=[]
for k,v in d.items():
    lst1.append([k,v])
lst1.sort(key=lambda x:x[0])
for s in range(len(lst1)):
    print(str(lst1[s][0])+','+str(lst1[s][1]))
