n,m,l=map(int,input().split(','))
a=[n]
b=n+l*(m-1)
while n<b:
    n+=l
    a.append(n)
print(a)
