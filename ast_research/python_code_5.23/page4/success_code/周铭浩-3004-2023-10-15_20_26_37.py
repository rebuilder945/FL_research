ls=eval(input())
for x in ls:
    for i in range(1,x):
        if x%i==0:
            ls.remove(x)
        else:
            continue
print(ls)

