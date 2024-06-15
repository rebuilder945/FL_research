a=eval(input())
n,m=eval(input())
if n<=len(a):
    for x in range(n,m):
        b=a.pop(x)
    print(b)
else:
    print("error")

