a=list(map(int,input().split(',')))
m,n=eval(input())
for i in range(n):
    a.append(a[m])
print(a)
