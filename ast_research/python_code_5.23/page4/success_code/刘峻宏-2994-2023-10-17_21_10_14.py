a=list(map(int,input().split(',')))
m,n=eval(input())
if n<=len(a):
    for i in range(n):
        a.append(a[m])
    print(a)
else:
    print("error")
