lst = eval(input(''))
n,m = eval(input(''))
n = int(n)
m = int(m)

if n < 0 or m > len(lst) or n>=m:
    print('error')
else:
    for x in range(n,m):
        del lst[x]
        print(lst)
    


