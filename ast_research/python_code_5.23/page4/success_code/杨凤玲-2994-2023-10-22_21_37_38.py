a=list(map(int,input().split(',')))
n,m=eval(input())
b=a[n]
for i in range(m):
    a.append(b)
print(a)

