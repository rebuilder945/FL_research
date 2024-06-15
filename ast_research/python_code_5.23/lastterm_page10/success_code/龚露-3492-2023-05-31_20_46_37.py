a=input()
d=[]
if len(a)==0:
    print('None')
else:
    for x in a:
        if a.count(x)==1:
            d.append(x)
    print(d[0])



