l=eval(input())
n,m=eval(input())
if n<=len(l)-1 or m<=len(l)-1:
    if n<=m:
        del l[n:m]
        print(l)
    else:
        print('error')
else:
    print('error')
