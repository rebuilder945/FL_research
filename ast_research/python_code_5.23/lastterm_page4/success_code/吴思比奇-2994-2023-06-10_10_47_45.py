a=map(int,input().split(","))
n,m=map(int,input().split(','))
a=list(a)
if n >len(a):
    print('error')
else :
    i=0
    x=a[n]
    while i<m:
        a.append(x)
        i=i+1
print(a)
