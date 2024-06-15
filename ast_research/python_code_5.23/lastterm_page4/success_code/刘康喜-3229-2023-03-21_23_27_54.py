a=eval(input())
b=a.copy()
d=[]
for i in range (0,len(a)):
    if a.count(a[i])==1:
        d.append(a[i])
d.sort()
for j in d:
    print(j,end=',')
