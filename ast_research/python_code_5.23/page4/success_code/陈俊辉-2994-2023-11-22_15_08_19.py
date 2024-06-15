a=map(int,input().split(','))
n,m=map(int,input().split(','))
a=list(a)
b=[]
if n-1<=len(a):
    for x in range(m):
     b.append(a[n])
    a=a+b
    #for i in range(len(b)):
       # a.append(b[i])
    print(a)
else:
    print("error")

