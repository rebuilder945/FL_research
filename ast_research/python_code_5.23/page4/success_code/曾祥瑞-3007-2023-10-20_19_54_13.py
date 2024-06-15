a=eval(input())
n,m=eval(input())
if n in a and m in a:
    a.remove(n,m)
    print(a)
else:
    print("error")
