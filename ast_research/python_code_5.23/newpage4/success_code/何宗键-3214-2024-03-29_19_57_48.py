a=list(eval(input()))
for i in a:
    if i==0:
        del a[i]
        a.append(i)
        print(a)
