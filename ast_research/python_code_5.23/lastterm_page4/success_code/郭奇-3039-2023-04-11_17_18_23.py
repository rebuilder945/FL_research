ls = eval(input())
a = max(ls)
b = min(ls)
n = ls.index(a)
m = ls.index(b)
del ls[n]
del ls[m]
print(ls)
