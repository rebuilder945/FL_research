a=list(map(eval,input().split(',')))
n,m=eval(input())
if abs(n) >=len(a):
    print('error')
else:
    b=a[n]
    for i in range(m):
        a.append(b)
print(a)
