ls=eval(input())
for i in ls:
    for j in range(2:int(i)):
        if i%j==0:
            ls.remove(j)
print(ls)
