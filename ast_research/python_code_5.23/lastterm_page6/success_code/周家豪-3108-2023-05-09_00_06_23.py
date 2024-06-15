lst=eval(input())
dic0={}
lst2=[]
for x in lst:
    for y in x:
        dic0[y]=dic0.get(y,0)+1
for k,v in dic0.items():
    lst2.append([k,v])
lst2.sort(reverse=False)
for x in lst2:
    print('%s,%s'%(x[0],x[1]))
