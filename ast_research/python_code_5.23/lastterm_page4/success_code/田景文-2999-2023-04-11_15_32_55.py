lst = input().split()
m, n = list(map(int, input().strip().split()))
lst[m], lst[n] = lst[n], lst[m]
print(lst)
