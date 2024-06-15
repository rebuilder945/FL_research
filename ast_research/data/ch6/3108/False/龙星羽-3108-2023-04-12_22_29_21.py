ls=eval(input())
lm=[]
for str in ls:
    for s in str:
        lm.append(s)
for i in lm:
    print('%s,%d'%(i,lm.count(i)))

