ls=eval(input())
l=list(set(ls))
for i in l:
    while ls.count(i)>1:
        ls.remove(i)
print(ls)
