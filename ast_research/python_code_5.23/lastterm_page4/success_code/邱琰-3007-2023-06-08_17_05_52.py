ls=eval(input())
n,m=eval(input())
if n>m or n>len(ls)-1 or m>len(ls)-1:
    print('error')
else:
    del ls[n,m]
    print(ls)
