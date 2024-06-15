ls=eval(input())
ls1=ls[:]
for i in range(len(ls1)):
    while ls.count(ls[i])!=1:
        del ls[i]
print(ls)

