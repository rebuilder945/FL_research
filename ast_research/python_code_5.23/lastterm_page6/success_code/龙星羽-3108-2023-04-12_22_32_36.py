ls=eval(input())
lm={}
for str in ls:
    for s in str:
        lm[s]=lm.get(s,0)+1
for i in sorted(lm.keys()):
    print('%s,%d'%(i,lm[i]))

