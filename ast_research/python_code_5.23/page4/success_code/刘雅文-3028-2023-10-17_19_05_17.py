n,m,l=map(int,input().split(','))
q=[]
for x in range(m):
    y=n+l*x
    q.append(y)
print(q)
