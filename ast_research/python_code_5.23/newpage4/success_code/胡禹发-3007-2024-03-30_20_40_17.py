a=list(eval(input()))
n,m=eval(input())
if n-1 in a:
    if m-1 in a:
        for i in range(n,m):
            a.remove(i)
        print(a)
    else:
        print("error")
else:
    print("error")
