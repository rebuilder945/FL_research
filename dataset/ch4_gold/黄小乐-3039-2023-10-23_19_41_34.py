ls = list(eval(input()))
m = max(ls)
n = min(ls)
while m in ls:
    ls.remove(m)
while m in ls:
    ls.remove(n)
print(ls)
