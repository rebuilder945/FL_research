ls=eval(input())
for i in ls:
    while ls.count(i)>1:
        ls.remove(i)
print(ls)
