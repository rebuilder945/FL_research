a=eval(input())
a.reverse()
ls=[]
for x in a:
    if x not in ls:
        ls.append(x)
ls.reverse()
print(ls)
