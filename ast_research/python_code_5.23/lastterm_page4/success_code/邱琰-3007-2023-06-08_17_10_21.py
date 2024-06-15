ls=eval(input())
n,m=eval(input())
if n>len(ls)-1 or m>len(ls)-1:
    print('error')
else:
    if n>m:
        print('error')
    else:
        del ls[n:m]
        print(ls)
