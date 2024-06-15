a=input().split(',')
b=input().split(',')
c=list(map(int,b))
d=[]
for x in range(len(a)):
    d.append([a[x],b[x]])
d.sort(key=lambda x:x[1])
print(d)
