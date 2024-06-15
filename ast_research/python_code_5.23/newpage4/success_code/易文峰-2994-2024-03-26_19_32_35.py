lst = input().split(",")
n, m = map(int, input().split(","))

if abs(n) > len(lst):
    print("error")
else:
    element = lst[n - 1]
    lst += [element] * m

print(lst)
