a=input().split()
c=list(set(a))
b={}
for i in c:
    b[i]=a.count(i)
lst1=list(b.items())
lst1.sort(key=lambda x:x[1])
for x in lst1:
    if x[1]==lst1[-1][1]:
        print(x[0],x[1])
