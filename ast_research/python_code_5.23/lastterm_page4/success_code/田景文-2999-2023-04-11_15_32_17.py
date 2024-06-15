lst = input().split()
m, n = list(map(int, input().strip().split()))
lst[m], lst[n] = lst[m], lst[m]
print(lst)
