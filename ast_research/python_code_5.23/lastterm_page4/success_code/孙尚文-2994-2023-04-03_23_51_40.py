a=list(int,map(input().split(",")))
n,m=eval(input())
if n<len(a) or n>=len(a):
    print("error")
else:
    b=[a[n] for x in range(0,m)]
    print(a+b)
