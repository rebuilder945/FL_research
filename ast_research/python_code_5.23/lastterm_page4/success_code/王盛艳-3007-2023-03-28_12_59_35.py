lst = list(eval(input()))
n,m = input().split(',')
n = int(n)
m = int(m)
if n in lst and m in lst:
    if n < m:
        del lst[n:m]
        print(lst)
    else:
        del lst[m+1:n+1]
        print(lst)
else:
    print("error")
