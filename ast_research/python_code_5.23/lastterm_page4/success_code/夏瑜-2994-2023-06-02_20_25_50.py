a=list(map(int,input().split(",")))
n,m=eval(input())
d=[]
if 0<=n<=len(a):
    d.append(a[n])
    c=d*3
    e=a+c
    print(e)
else:
    print("error")


