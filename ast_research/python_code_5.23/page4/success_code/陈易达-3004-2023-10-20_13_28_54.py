ls = eval(input())
for x in ls:
    for i in range(2,x):
        if x%i == 0:
            ls.remove(x)
print(ls)
