a = list(eval(input()))
n,m = eval(input())
if n<=len(a)-1:
    b = a[n]
    a+=[b]*m
    print(a)
else:
    print('error')

