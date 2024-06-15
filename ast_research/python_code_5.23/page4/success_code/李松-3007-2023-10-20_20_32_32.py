l=eval(input())
n,m=eval(input())
if n>len(1)-1 or m>len(1)-1:
    print("error")
else:
    if n<=m:
        del 1[n:m]
    else:
        del 1[n:m:-1]
    print(1)
