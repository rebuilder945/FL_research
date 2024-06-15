ls=eval(input())
ls1=ls[:]
for i in ls1:
    while ls.count(i)!=1:
        ls.remove(i)
print(ls)

