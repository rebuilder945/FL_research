lst = input().split()
n, m = eval(input())
lst1 = lst[:]
lst[n] = lst[m]
lst[m] = lst1[n]
print(lst)
