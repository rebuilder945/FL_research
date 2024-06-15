lst = input().split(',')
n, m = map(int, input().split(','))

if 0 <= abs(n) < len(lst):
    element = lst[n]
    lst += [element] * m
    print(lst)
else:
    print("error")
