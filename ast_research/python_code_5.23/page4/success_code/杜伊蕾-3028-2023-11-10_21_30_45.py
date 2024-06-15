'''a=input().split(',')
a=list(a)
b=eval(input())
m=[]
for x in range(len(a)):
    n=[]
    n.append(a[x])
    n.append(b[x])
    m.append(n)
print(m)'''

n,m,l=map(int,input().split(','))
c=[]
for x in range (m):
    n=n+l
    c.append(n)
print(c)
