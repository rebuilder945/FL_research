ls = eval(input())
for x in ls:
    a = ls.count(x)
    while a>1:
        ls.remove(x)
print(ls)
