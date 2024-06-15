list = eval(input())
n,m = eval(input())
c = len(list)
i = n
if i>= 0 and m>=n and m<=c:
    while n>= 0 and m<=c:
        del list[n]
        n = n+1
        if n == m:
            break
    print(list)
else:
    print('error')
