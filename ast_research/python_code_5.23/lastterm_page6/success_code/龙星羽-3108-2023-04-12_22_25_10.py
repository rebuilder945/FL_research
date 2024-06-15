ls=eval(input())
count={}
for str in ls:
    for s in str:
        count[s]=count.get(s,0)+1
for i in sorted(count.keys()):
    print('%s,%d'%(i,count[i]))
