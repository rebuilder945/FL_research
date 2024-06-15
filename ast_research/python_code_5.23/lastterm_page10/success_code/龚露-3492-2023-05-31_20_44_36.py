a=input()
d=[]
if a =='':
    print('None')
else:
    for x in a:
        if a.count(x)==1:
            d.append(x)
print(d[0])



