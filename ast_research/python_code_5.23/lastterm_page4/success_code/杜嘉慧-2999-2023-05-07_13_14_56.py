lst = input().split(' ')
n, m = [int(x) for x in input().split(' ')]
a = lst[n]
lst[n] = lst[m]
lst[m] = a
print(lst)


