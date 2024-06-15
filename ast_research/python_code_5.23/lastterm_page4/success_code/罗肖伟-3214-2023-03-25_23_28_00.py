ls=eval(input())
for i in ls:
    if i==0:
        ls.remove(0)
        ls.append(0)
    else:
        ls=ls
print(ls)
