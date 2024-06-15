ls=list(eval(input()))
ls.reverse()
a=[]
for i in ls:
    if not i in a:
        a.append(i)
a.reverse()
print(a)
