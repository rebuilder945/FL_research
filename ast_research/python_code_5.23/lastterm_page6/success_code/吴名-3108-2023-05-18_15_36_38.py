l=eval(input())
a=''
for i in l:
    a+=i
a=list(a)
b=[]
for i in a:
    if i not in b:
        b.append(i)
b.sort()
for i in b:
    x=0
    for c in a:
        if c==i:
            x+=1
    print("%s,%d"%(i,x))
