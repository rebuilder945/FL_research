a=list(str(input()))
b="abcdefghijklmnopqrstuvwxyz"
for x in b:
    i=0
    for o in a:
        if o==x:
            i=i+1
    if i>0:
        print("%s,%i\n"%(x,i))
