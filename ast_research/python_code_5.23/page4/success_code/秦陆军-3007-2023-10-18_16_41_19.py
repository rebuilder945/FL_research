lst = eval(input(''))
n, m = eval(input(''))
n = int(n)
m = int(m)
if abs(m) > len(lst) or n >= m or abs(n) > len(lst):
    print('error')
else:
    for x in range(n, m):
        del lst[x]
    print(lst)
