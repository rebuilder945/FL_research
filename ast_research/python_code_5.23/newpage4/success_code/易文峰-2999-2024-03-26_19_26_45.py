lst = input().split()
n, m = map(int, input().split())
if 0 <= n < len(lst) and 0 <= m < len(lst):
    lst[n], lst[m] = lst[m], lst[n]
    print(lst)
else:
    print("error")
