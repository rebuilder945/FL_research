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
for i in range (m):
    d=n+l*i
    c.append(d)
print(c)
