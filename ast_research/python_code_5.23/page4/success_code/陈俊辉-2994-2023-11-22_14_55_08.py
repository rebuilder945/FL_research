a=map(int,input().split(','))
n,m=map(int,input().split(','))
b=[]
if n-1<len(a):
 while m>0:
    b.append(a[n-1])
    m-=1
for i in range(b):
    a.append(b[i])
    print(a)
else:
    print("error")
