n,m,l=map(int,input().split(','))
a=['1','1']
a.pop()
a.pop()
while m>0:
    a.append(n)
    n+=l
    m-=1
print(a)

