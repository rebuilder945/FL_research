a=input().split(",")
b=[int(a[i]) for i in range(0,len(a))]
n,m=eval(input())
if n >=len(a):
    print('error')
else:
    c=b+[b[n]]*m
    print(c)
