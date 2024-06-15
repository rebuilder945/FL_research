a=eval(input())
n,m=map(int,input().split(','))
if n<=len(a):
    b=[]
    for i in range(n):
        b.append(a[i])
    for x in range(m,len(a)):
        b.append(a[x])
    print(b)
else:
    print("error")
