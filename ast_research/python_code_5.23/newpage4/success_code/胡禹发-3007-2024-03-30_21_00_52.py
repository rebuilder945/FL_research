a=list(eval(input()))
b=a.copy()
n,m=eval(input())
if n in range(len(a)):
    if m==n:
        print(a)
    elif m in range(len(a)):
        for i in range(n,m):
            a.remove(b[i])
        print(a)
    else:
        print("error")
else:
    print("error")
