a=list(eval(input()))
for i in a:
    if i==0:
        a.pop(i)
        a.append(i)
        print(a)
