lst = input()
n,m = eval(input())
a = lst[n]
b = lst[m]
lst[m] = a
lst[n] = b
print(lst)

