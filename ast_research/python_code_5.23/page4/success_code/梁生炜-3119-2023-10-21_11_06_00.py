ls=eval(input())
ls1=ls.copy
for i in range(len(ls)):
    if ls[i] in ls1[-1:i-len(ls1)]:
        ls.remove(i)
print(ls)
