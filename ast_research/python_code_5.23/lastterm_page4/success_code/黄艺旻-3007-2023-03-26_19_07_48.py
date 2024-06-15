lst = eval(input())
n,m = eval(input())
n = int(n)
m = int(m)
if n in lst and m in lst and n<=m:
    del lst[n:m]
    print(lst)
else:
    print('error')
