lst=eval(input())
count={}
for i in lst:
    for n in i:
        count[n]=count.get(n,0)+1
for a in sorted(count):
    print("%s,%d"%(a,count[a]))
