a=input().split(',')
a=list(a)
b=eval(input())
m=[]
for i in range (len(a)):
    n=[]
    n.append(a[i])
    n.append(b[i])
    m.append(n)
print(m)

