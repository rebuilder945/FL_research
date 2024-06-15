ls=eval(input())
lst=ls[:]
for i in lst:
    while ls.count(i)!=1:
        ls.remove(i)
print(ls)
