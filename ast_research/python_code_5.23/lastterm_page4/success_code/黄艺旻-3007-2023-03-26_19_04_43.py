lst = eval(input())
n,m = eval(input())
if n in lst and m in lst and n<=m:
    del lst[n:m]
    print(lst)
else:
    print('error')
