a=eval(input())
n,m=int(input())
if n in a and m in a:
    a.remove(n,m)
    print(a)
else:
    print("error")
