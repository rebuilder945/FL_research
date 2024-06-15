ls=eval(input())
for i in ls:
    while ls.count(i)>2:
        ls.remove(i)
print(ls)
