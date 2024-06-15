n=int(input())
l=[]
for i in range(n):
    l.append(i)
l2=[]
for x in l:
    if x<n:
        l2[x]=l[x+1]
    elif x==n:
        l2[x]=1
print(l2)
