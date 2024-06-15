list=eval(input())
count={}
for str in list:
    for lst in str:
        count[lst]=count.get(lst,0)+1
for i in sorted(count.keys()):
    print('%s,%d'%(i,count[i]))

