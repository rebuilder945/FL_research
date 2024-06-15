a=input().split(',')
b=eval(input()).split(',')
c=len(a)
d=[]
for i in range(c):
    f=list((a[i],b[i]))
    d.append(f)
d.sorted(key=lambda x:([1]))
print(d)
