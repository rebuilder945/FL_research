ls=eval(input())
for i in ls:
    if ls.count(i)>=2:
        ls.remove(i)
print(ls)
