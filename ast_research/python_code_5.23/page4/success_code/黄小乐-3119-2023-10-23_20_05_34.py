ls = list(eval(input()))
for x in ls:
    while ls.count(x)>1:
        ls.remove(x)
print(ls)

