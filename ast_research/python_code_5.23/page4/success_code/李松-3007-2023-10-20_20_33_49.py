l=eval(input())
n,m=eval(input())
if n>len(l)-1 or m>len(l)-1:
    print("error")
else:
    if n<=m:
        del 1[n:m]
    else:
        del 1[n:m:-1]
    print(l)
