list = eval(input())
n,m = eval(input())
c = len(list)
i = n
if i>= 0 and m>=n and m<=c:
    while n>= 0 and m<=c:
        if n == m:
            break
        del list[n]
        n = n+1
    print(list)
else:
    print('error')
