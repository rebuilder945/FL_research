a=list(eval(input()))
n,m=eval(input())
if n-1 in range(len(a)):
    if m-1 in range(len()):
        for i in range(n,m):
            a.remove(i)
        print(a)
    else:
        print("error")
else:
    print("error")
