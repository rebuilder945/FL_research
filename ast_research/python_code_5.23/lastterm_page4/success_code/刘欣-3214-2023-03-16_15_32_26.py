ls=eval(input())
for i in ls:
    if i==0:
        while i in ls:
            ls.remove(i)
            ls.append(i)
print(ls)


