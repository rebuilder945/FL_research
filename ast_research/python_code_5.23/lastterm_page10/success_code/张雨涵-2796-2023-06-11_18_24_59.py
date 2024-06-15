a = list(input())
b=["1","2","3","4","5","6","7","8","9","0"]
c = [0]*len(a)
for i in range(len(a)) :
    if a[i] in b:
        c[i] = 1
for x in range(len(c)) :
    if x ==0:
        if c[0]==1:
            c[0]=1
    elif x >=1:
        if c[x-1] >= 1 and c[x]>=1:
            c[x]=c[x-1]+1
m = max(c)
c=c[::-1]
for i in c:
    if i == m:
        k = c.index(max(c))
c=c[::-1]
k=len(c)-k
ls1=a[k-m:k]
print("".join(ls1))
