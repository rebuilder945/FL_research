l=eval(input())
count={}
for i in l:
    for j in i:
        count[j]=count.get(j,0)+1
for k in sorted(count.keys()):
    print('%s,%d'%(k,count[k]))
    
