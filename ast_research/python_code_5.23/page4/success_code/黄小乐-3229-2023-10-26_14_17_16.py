ls = list(eval(input()))
ls2 = []
for x in ls:
    if ls.count(x)==1:
        ls2.append(x)
ls2.sort()
result = ','.join(str(i) for i in ls2)
if len(ls2)==0:
    print(False)
else:
    print(result)




