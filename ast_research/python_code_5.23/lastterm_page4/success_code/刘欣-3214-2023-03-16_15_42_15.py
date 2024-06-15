ls=eval(input())
for i in range(len(ls)-1):
    if ls[i]==0:
        a=ls.pop(i)
        ls.append(a)
print(ls)


