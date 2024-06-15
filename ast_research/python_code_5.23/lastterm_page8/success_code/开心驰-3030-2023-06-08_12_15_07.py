a=input().split(',')
b=input().split(',')
c=len(a)
d=[]
for i in range(c):
    f=list((a[i],b[i]))
    d.append(f)
d.sort(key=lambda x:([1]),reverse=False)
print(d)
