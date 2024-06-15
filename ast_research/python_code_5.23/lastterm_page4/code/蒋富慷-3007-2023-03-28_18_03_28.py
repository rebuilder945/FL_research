l = eval(input())
n,m = eval(input())
if n > len(l)-1 or m > len(l)-1:
    print('error')
else:
    del l(n:m)
    print(l)
