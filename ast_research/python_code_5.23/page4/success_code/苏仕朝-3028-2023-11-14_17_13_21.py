n,m,l=map(int,input().split(','))
a=[]
while m>0:
    a.append(n)
    n+=l
    m-=1
print(a)


