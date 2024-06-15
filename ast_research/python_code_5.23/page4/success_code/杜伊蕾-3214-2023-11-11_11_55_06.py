a=eval(input())
n,m=map(int,input().split(","))
if n <= len(a):
    for x in range(n,m):
        b=a.pop(x)
    print(a)
else:
    print("error")



