a=list(eval(input()))
m=[]
for x in a:
    if a.count(x)==1:
        m.append(x)
        m.sort()
    else:
        print('false')

