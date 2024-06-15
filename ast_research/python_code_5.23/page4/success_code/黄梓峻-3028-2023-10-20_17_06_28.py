m,n,l=map(int,input().split(','))
d=[]
for x in range(n):
    m=m+l*x
    d.append(m)
print(d)
