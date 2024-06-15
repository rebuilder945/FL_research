ls=eval(input())
for i in ls:
    if i==0:
        ls.remove(i)
        ls.append(i)
print(ls)
