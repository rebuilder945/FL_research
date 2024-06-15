n,m,l=eval(input())
s=[]
s.append(n)
for i in range(m-1):
    n=n+l
    s.append(n)
print(s)
