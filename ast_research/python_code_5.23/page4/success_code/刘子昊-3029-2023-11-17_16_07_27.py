a=input().split(',')
b=eval(input())
a=list(a)
m=[]
for i in range(len(a)):
    n=[]
    n.append(a[i])
    n.append(b[i])
    m.append(n)
print(m)

