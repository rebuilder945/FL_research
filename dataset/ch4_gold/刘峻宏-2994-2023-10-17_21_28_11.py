from posixpath import split


a=list(map(int,input().split(',')))
n,m=eval(input())
if n<len(a):
    if n>0:
        for i in range(m):
            a.append(a[n])
        print(a)
    else:
        for i in range(m):
            a.append(a[n])
            n-=1
        print(a)
else:
    print("error")
