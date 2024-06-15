a=input()
if a=="":
    print("None")
else:
    k=len(a)
    for i in a:
        b=[]
        if a.count(i)==1:
            b.append(i)
            for i in b:
                if a.index(i)<=k:
                    k=a.index(i)
                    print(a[k])


