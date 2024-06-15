a=list(input())
b=len(a)
l=[]
if b==0:
    print("None")
else:
    for i in a:
        c=a.count(i)
        if c==1:
            l.append(i)
    print(l[0])
            

