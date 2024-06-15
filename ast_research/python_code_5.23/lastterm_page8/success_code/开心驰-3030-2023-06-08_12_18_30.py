a=input().split(',')
b=int(input().split(','))
c=len(a)
d=[]
for i in range(c):
    f=list((a[i],b[i]))
    d.append(f)
d.sort(key=lambda x:(x[1]))
print(d)
