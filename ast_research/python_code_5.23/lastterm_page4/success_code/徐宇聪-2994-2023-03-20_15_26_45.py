lst = input().split(',')
n, m = map(int, input().split(','))
if abs(n) > len(lst):
    print('error')
else:
    num = lst[n-1]
    lst.extend([num]*m)
    print(lst)
