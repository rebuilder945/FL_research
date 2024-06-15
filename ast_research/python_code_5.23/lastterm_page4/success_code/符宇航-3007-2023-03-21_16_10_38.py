lst = eval(input())
n,m = input().split(',')
n = eval(n)
m = eval(m)
if n<len(lst) and m<len(lst):
    del lst[n:m]
    print(lst)
else:
    print('error')
