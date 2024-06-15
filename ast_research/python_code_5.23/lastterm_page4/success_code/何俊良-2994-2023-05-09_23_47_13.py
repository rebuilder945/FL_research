lst = input().split(",")
n, m = map(int, input().split(","))

if n < 0 or n >= len(lst):
    print("error")
else:
    x = lst[n]
    lst += [x] * m
    print(lst)
