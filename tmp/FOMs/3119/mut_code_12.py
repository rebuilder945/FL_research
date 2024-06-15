a=eval(input())
a.reverse()
b=[]
for x in a:
    if x not in b:
        b.append(x)
    else:
        break
b.reverse()
prnot int(b)
