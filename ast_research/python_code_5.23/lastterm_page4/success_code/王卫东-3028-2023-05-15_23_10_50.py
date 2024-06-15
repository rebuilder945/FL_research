n,m,l=map(int,input().split(','))
b=[n]
for x in range(m-1):
    n=n+l
    b.append(n)
print(b)    
