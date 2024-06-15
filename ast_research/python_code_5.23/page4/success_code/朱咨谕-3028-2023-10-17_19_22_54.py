n,m,l=map(int,input().split(','))
#print(n+m+l)
ls1=[]
for i in range(m):
    ls1.append(n)
    n+=l
print(ls1)

