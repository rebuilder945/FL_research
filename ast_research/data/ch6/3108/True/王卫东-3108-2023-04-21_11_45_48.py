a=list(input())
count={}
for x in a:
    for y in x:
        if ord(y)>=97 and ord(y)<=122:
            count[y]=count.get(y,0)+1
for x in sorted(count.keys()):
    print("%s,%d"%(x,count[x]))            
    
                              

