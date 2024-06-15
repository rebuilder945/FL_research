list = eval(input())
n,m = eval(input())
if(n > -1 and n < len(list) and m > -1 and m < len(list) and n <= m):
    del list[n:m]
    print(list)
else:
    print('error')
