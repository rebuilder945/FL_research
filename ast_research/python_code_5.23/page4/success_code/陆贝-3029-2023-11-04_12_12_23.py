a=input().split(sep=",")
b=eval(input())
l=len(b)
ii=[]
for i in range(l):
    n=a[i]
    m=b[i]
    t=[]
    t.append(n)
    t.append(m)
    ii.append(t)
print(ii)
