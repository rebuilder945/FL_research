a=eval(input())
n,m=map(int,input().split(','))
if n<=len(a):
    b=[]
    for x in range(n):
        b.append(x)
    for i in range(m,len(a)):
        b.append(a[i])
    print(b)
else:
    print("error")
