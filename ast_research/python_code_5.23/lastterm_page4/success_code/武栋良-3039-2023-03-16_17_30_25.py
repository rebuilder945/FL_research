ls = eval(input("请输入列表："))
a = max(ls)
b = min(ls)
while a in ls:
    ls.remove(a)
while b in ls:
    ls.remove(b)
print(ls)
