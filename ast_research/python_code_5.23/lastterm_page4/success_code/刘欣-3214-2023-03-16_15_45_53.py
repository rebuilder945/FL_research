ls=eval(input())
for i in range(0,len(ls)):
    if ls[i]==0:
        a=ls.pop(i)
        ls.append(a)
print(ls)


