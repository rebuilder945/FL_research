ls=eval(input())
ls1=ls[:]
for i in range(len(ls1)):
    if ls[i] == 0:
        a=ls.pop(i)
        ls.append(a)
print(ls)

