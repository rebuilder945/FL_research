lst = input().split(',')
n, m = map(int, input().split(','))

if abs(n) < len(lst):
    element = lst[abs(n)]
    lst += [element] * m
    print(lst)
else:
    print("error")
