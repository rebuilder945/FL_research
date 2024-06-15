a=eval(input())
a.sort()
n,m=eval(input())
if n in a and m in a and n<<m:
    del a[n:m]
    print(a)
else:
    print("error")
