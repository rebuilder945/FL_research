lst = input().split()
n,m = eval(input())
s = lst[n]
lst[n] = lst[m]
lst[m] = s
print(lst)

