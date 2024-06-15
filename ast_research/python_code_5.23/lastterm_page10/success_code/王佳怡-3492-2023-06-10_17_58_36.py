a=input()
l=[]
if len(a)!=0:
    for i in a:
        if a.count(i)==1:
            l.append(i)
    print(l[0])
else:
    print("None")

