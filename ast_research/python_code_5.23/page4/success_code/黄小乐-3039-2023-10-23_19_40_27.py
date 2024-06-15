ls = list(eval(input()))
m = max(ls)
n = min(ls)
while m in ls or n in ls:
    ls.remove(m)
    ls.remove(n)
print(ls)
