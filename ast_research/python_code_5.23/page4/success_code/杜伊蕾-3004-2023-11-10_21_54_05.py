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

'''n,m,l=map(int,input().split(','))
c=[]
for i in range (m):
    d=n+l*i
    c.append(d)
print(c)'''

'''a=eval(input())
n,m=map(int,input().split(','))
if n<=len(a):
    for x in range (n,m):
        b=a.pop(x)
    print(a)
else:
    print('error')'''

a=eval(input())
b=[]
for i in a:
    if i >=2:
        for j in range(2,i,1):
            if i%j==0:
                break
            else:
                b.append(i)
print(b)
