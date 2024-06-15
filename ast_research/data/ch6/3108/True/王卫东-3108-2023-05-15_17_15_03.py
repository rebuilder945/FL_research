a=eval(input())
b={}
for x in a:
    for y in x:
        b[y]=b.get(y,0)+1
for i in sorted(b.keys()):
    print("%s,%d"%(i,b[i]))        

