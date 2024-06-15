ls=eval(input())
n=len(ls)
ls1=ls.copy
for i in range(len(ls)):
    if ls[i] in ls1[-1:i-n]:
        ls.remove(i)
print(ls)
