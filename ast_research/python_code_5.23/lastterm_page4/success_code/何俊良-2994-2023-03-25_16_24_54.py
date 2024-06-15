lst = input().split(',')
n, m = map(int, input().split(','))
if abs(n) > len(lst):
    print('error')
else:
    idx = n if n >= 0 else len(lst) + n
    lst = lst[:idx] + [lst[idx]] * m + lst[idx+1:]
    print(lst)

